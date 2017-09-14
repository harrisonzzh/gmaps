
import unittest

from .. import drawing, marker


class Drawing(unittest.TestCase):

    def test_default_overlays(self):
        layer = drawing.Drawing()
        assert layer.get_state()['overlays'] == []

    def test_with_overlays(self):
        marker_widget = marker.Marker()
        layer = drawing.Drawing(overlays=[marker_widget])
        overlays = layer.get_state()['overlays']
        assert len(overlays) == 1
        [serialized_marker] = overlays
        assert serialized_marker == 'IPY_MODEL_{}'.format(marker_widget.model_id)

    def test_adding_marker(self):
        layer = drawing.Drawing()
        message = {
            'event': 'OVERLAY_ADDED',
            'payload': {
                'overlayType': 'MARKER',
                'latitude': 25.0,
                'longitude': -5.0
            }
        }
        layer._handle_custom_msg(message, None)
        assert len(layer.overlays) == 1
        [new_marker] = layer.overlays
        assert new_marker.location == (25.0, -5.0)