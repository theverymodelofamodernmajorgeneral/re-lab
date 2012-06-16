# Copyright (C) 2007,2010,2011	Valek Filippov (frob@df.ru)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 3 or later of the GNU General Public
# License as published by the Free Software Foundation.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA
#

import gtk
import gobject
import tree
import hv2

class hexdump:
	def __init__(self):
		self.vpaned = gtk.VPaned()
		self.hdmodel, self.hdview, self.hdscrolled, self.hdrend = tree.make_view2()
		self.hbox0 =gtk.HBox()
		self.da = None
		self.hbox0.pack_start(self.hdscrolled)
		self.vpaned.add1(self.hbox0)
		self.hdscrolled.set_size_request(300, 300)
		self.version = None # to support vsdchunks for different versions
		self.width = 0
		self.height = 0
		
		self.hv = hv2.HexView()
		self.vpaned.add2(self.hv.table)

	def update():
		pass

