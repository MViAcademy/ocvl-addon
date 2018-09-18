#  ***** BEGIN GPL LICENSE BLOCK *****
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>
#  and write to the Free Software Foundation, Inc., 51 Franklin Street,
#  Fifth Floor, Boston, MA  02110-1301, USA..
#
#  All rights reserved.
#
#  Contact:      dawid.aniol@teredo.tech    ###
#  Information:  http://teredo.tech         ###
#
#  ***** END GPL LICENSE BLOCK *****
#

import sys


bl_info = {
    "name": "ocvl",
    "author": (
        "Dawid Aniol",
        "OCVL team",
        "Teredo team",
    ),
    "version": (1, 1, 0),
    "blender": (2, 7, 9),
    "location": "Nodes > CustomNodesTree > Add user nodes",
    "description": "Computer vision node-based programming",
    "warning": "",
    "wiki_url": "https://opencv-laboratory.readthedocs.io/en/latest/",
    "tracker_url": "https://github.com/feler404/ocvl/issues",
    "category": "Node"
}

if __name__ != "ocvl":
    sys.modules["ocvl"] = sys.modules[__name__]


def register():
    from ocvl import logger_conf
    from ocvl.core import node_tree
    from ocvl.core import sockets
    from ocvl import operatores
    from ocvl.core.register_utils import reload_ocvl_modules
    reload_ocvl_modules()
    node_tree.register()
    sockets.register()
    operatores.register()
    logger_conf.register()


def unregister():
    from ocvl.core import node_tree
    from ocvl.core import sockets
    from ocvl import operatores
    node_tree.unregister()
    sockets.unregister()
    operatores.unregister()
