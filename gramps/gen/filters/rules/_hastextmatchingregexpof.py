#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2002-2006  Donald N. Allingham
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

# -------------------------------------------------------------------------
#
# Gramps modules
#
# -------------------------------------------------------------------------
from . import HasTextMatchingSubstringOf


# -------------------------------------------------------------------------
# "HasTextMatchingRegexOf"
# -------------------------------------------------------------------------
class HasTextMatchingRegexpOf(HasTextMatchingSubstringOf):
    """
    Wrap HasTextMatchingSubstringOf to enable the regex_match parameter.
    """

    def __init__(self, list, use_regex=False, use_case=False):
        HasTextMatchingSubstringOf.__init__(self, list, use_regex, use_case)

    # FIXME: This needs to be written for an arbitrary object
    # if possible
