# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Custom configurations and functions for Google App Engine."""

__author__ = 'psimakov@google.com (Pavel Simakov)'

import os
import sys


# this is the official location of this app for computing of all relative paths
BUNDLE_ROOT = os.path.dirname(__file__)

# Default namespace name is '' and not None.
DEFAULT_NAMESPACE_NAME = ''

# Third-party library zip files.
THIRD_PARTY_LIBS = ['babel-0.9.6.zip', 'gaepytz-2011h.zip']

for lib in THIRD_PARTY_LIBS:
    thirdparty_lib = os.path.join(BUNDLE_ROOT, 'lib/%s' % lib)
    if not os.path.exists(thirdparty_lib):
        raise Exception('Library does not exist: %s' % thirdparty_lib)
    sys.path.insert(0, thirdparty_lib)
