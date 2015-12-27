# Copyright 2015 Kevin Reid <kpreid@switchb.org>
# 
# This file is part of ShinySDR.
# 
# ShinySDR is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# ShinySDR is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with ShinySDR.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division

from twisted.trial import unittest

from shinysdr.telemetry import TelemetryItem, Track, empty_track


class TestTrack(unittest.TestCase):
    def test_init_from_partial_json(self):
        self.assertEquals(
            empty_track._replace(
                latitude=TelemetryItem(1, 1000),
                longitude=TelemetryItem(2, 1000)),
            Track({
                u'latitude': {u'value': 1, u'timestamp': 1000},
                u'longitude': {u'value': 2, u'timestamp': 1000},
            }))
