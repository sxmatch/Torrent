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

from oslo_config import cfg

service_ip = cfg.StrOpt(
    'host_ip', default='127.0.0.1',
    help='Service IP')

port_ip = cfg.StrOpt(
    'port_ip', default='3306',
    help='Service Port')

db_conncection_user = cfg.StrOpt(
    'db_conncection_user', default='root',
    help='DB connection user')

db_conncection_password = cfg.StrOpt(
    'db_conncection_password', default='123456',
    help='DB connection password')

db_conncection_name = cfg.StrOpt(
    'db_conncection_name', default='torrent',
    help='DB name')

db_conncection_charset = cfg.StrOpt(
    'db_conncection_charset', default='utf8',
    help='DB connection charset')

GROUP_NAME = 'DEFAULT'
ALL_OPTS = [
    service_ip,
    port_ip,
    db_conncection_user,
    db_conncection_password,
    db_conncection_name,
    db_conncection_charset
]


def register_opts(conf):
    conf.register_opts(ALL_OPTS)


def list_opts():
    return {GROUP_NAME: ALL_OPTS}