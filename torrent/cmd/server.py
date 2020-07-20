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

from flask import *

from oslo_config import cfg
from oslo_log import log

from torrent.conf import opts as opts_tool

conf = cfg.CONF


def run():
    # Use the global CONF instance
    conf = cfg.CONF
    log.register_options(conf)

    # NOTE(jeffrey4l): Overwrite the default vaule for
    # logging_context_format_string. Add project_id into it.
    conf.set_default('logging_context_format_string',
                     '%(asctime)s.%(msecs)03d %(process)d %(levelname)s'
                     ' %(name)s [%(request_id)s %(user_identity)s]'
                     ' [project_id:%(project_id)s] %(message)s')
    conf(project='torrent', prog='torrent-server')
    for group, opts in opts_tool.list_opts_by_group():
        conf.register_opts(opts, group=group)
    log.setup(conf, 'torrent')

    flask_app = Flask(__name__)
    flask_app.config.from_object(__name__)
    flask_app.run(host=conf.host, port=conf.port)
