# Copyright (c) 2020 Fiberhome Ltd.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging

from oslo_cache import core as cache
from oslo_config import cfg
from oslo_log import log

from torrent.conf import default

CONF = cfg.CONF


conf_modules = [
    default
]


def setup_logging():
    """Set up logging for the keystone package."""
    log.setup(CONF, 'torrent')
    logging.captureWarnings(True)


def configure(conf=None):
    if conf is None:
        conf = CONF

    for module in conf_modules:
        module.register_opts(conf)

    # add oslo.cache related config options
    cache.configure(conf)
