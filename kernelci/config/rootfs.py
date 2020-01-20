# Copyright (C) 2019 Collabora Limited
# Author: Michal Galka <michal.galka@collabora.com>
#
# This module is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import yaml
import sys
from MyUtil import MyUtil

from kernelci.config import YAMLObject


class RootFS(YAMLObject):
    def __init__(self, name, rootfs_type):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        self._name = name
        self._rootfs_type = rootfs_type

    @classmethod
    def from_yaml(cls, rootfs, kw):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        return cls(**kw)

    @property
    def name(self):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        return self._name

    @property
    def rootfs_type(self):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        return self._rootfs_type


class RootFS_Debos(RootFS):
    def __init__(self, name, rootfs_type, debian_release=None,
                 arch_list=None, extra_packages=None,
                 extra_packages_remove=None,
                 extra_files_remove=None, script=""):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")

        super(RootFS_Debos, self).__init__(name, rootfs_type)
        self._debian_release = debian_release
        self._arch_list = arch_list or list()
        self._extra_packages = extra_packages or list()
        self._extra_packages_remove = extra_packages_remove or list()
        self._extra_files_remove = extra_files_remove or list()
        self._script = script

    @classmethod
    def from_yaml(cls, config, name):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        kw = name
        kw.update(cls._kw_from_yaml(
            config, ['name', 'debian_release', 'arch_list',
                     'extra_packages', 'extra_packages_remove',
                     'extra_files_remove', 'script']))
        return cls(**kw)

    @property
    def debian_release(self):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        return self._debian_release

    @property
    def arch_list(self):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        return list(self._arch_list)

    @property
    def extra_packages(self):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        return list(self._extra_packages)

    @property
    def extra_packages_remove(self):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        return list(self._extra_packages_remove)

    @property
    def extra_files_remove(self):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        return list(self._extra_files_remove)

    @property
    def script(self):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        return self._script


class RootFSFactory(YAMLObject):
    _rootfs_types = {
        'debos': RootFS_Debos
    }

    @classmethod
    def from_yaml(cls, name, rootfs):
        MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
        rootfs_type = rootfs.get('rootfs_type')
        kw = {
            'name': name,
            'rootfs_type': rootfs_type,
        }
        rootfs_cls = cls._rootfs_types[rootfs_type] if rootfs_type else RootFS
        return rootfs_cls.from_yaml(rootfs, kw)


def from_yaml(yaml_path):
    MyUtil.write_log(__file__,sys._getframe().f_lineno,__name__,"unixsocket")
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    rootfs_configs = {
        name: RootFSFactory.from_yaml(name, rootfs)
        for name, rootfs in data['rootfs_configs'].items()
    }

    config_data = {
        'rootfs_configs': rootfs_configs,
    }

    return config_data
