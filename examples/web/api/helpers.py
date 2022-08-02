#!/usr/bin/env python
#
# -*- coding: iso-8859-15 -*-
#
# Copyright 2003-2015 CORE Security Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors:
#          Andres Blanco (6e726d)
#          Andres Gazzoli
#

from impacket import dot11

def get_channel_from_frame(frame):
    """
    It returns the channel in which the frame was received.
    """
    rt = dot11.RadioTap(frame)
    channel_pair = rt.get_channel()
    if channel_pair is None:
        return -1

    freq = channel_pair[0]

    try:
        ch = dot11.frequency[freq]
    except KeyError:
        ch = -1
    return ch
