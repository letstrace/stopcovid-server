from django.test import TestCase
import json
import os

from ..models import Track

with open(os.path.join(os.path.dirname(__file__), "fixtures/track.json")) as fh:
    TRACK_FIXTURE = json.load(fh)


class TracksViewsTest(TestCase):
    def test_track_create(self):
        self.assertEqual(Track.objects.count(), 0)

        response = self.client.post(
            "/api/v1/track", TRACK_FIXTURE, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

        track = Track.objects.all()[0]
        self.assertEqual(track.points, TRACK_FIXTURE["points"])

    def test_track_invalid_data(self):
        # missing tracks
        response = self.client.post(
            "/api/v1/track",
            {"tracks": []},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

        # missing timestamp
        response = self.client.post(
            "/api/v1/track",
            {"tracks": [{"latitude": 50.0, "longitude": 50.0}]},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

        # latitude out of range
        response = self.client.post(
            "/api/v1/track",
            {"tracks": [{"latitude": 50000.0, "longitude": 50.0, "timestamp": 123}]},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
