# -*- coding: utf-8 -*-
# Copyright (c) 2015, imageio contributors
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

""" This subpackage provides the core functionality of imageio
(everything but the plugins).
"""

# flake8: noqa

from .util import Image, Dict, asarray, image_as_uint, urlopen
from .util import BaseProgressIndicator, StdoutProgressIndicator
from .util import string_types, text_type, binary_type, IS_PYPY
from .util import get_platform, appdata_dir, resource_dirs, has_module
from .findlib import load_lib
from .fetching import get_remote_file, InternetNotAllowedError, NeedDownloadError
from .request import Request, read_n_bytes, RETURN_BYTES
from .format import Format, FormatManager
