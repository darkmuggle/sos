# Copyright (C) 2014 Red Hat, Inc., Bryn M. Reeves <bmr@redhat.com>
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from sos.plugins import Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin


class Ctdb(Plugin, DebianPlugin, UbuntuPlugin):
    """Samba Clustered TDB
    """
    packages = ('ctdb',)
    profiles = ('cluster', 'storage')
    plugin_name = "ctdb"

    def setup(self):
        self.add_copy_spec([
            "/etc/ctdb/public_addresses",
            "/etc/ctdb/static-routes",
            "/etc/ctdb/multipathd",
            "/var/log/log.ctdb"
        ])

        self.add_cmd_output([
            "ctdb ip",
            "ctdb ping",
            "ctdb status",
            "ctdb ifaces",
            "ctdb listnodes",
            "ctdb listvars",
            "ctdb statistics",
            "ctdb getdbmap"
        ])


class RedHatCtdb(Ctdb, RedHatPlugin):
    def setup(self):
        super(RedHatCtdb, self).setup()
        self.add_copy_spec("/etc/sysconfig/ctdb")

# vim: et ts=4 sw=4
