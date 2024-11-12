# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2024, Damian Birchler
#
# Licensed under the terms of the GNU General Public License v3
# ----------------------------------------------------------------------------
"""
Pytrnsys Preferences Page.
"""
from spyder.api.preferences import PluginConfigPage
from spyder.api.translations import get_translation

_ = get_translation("spyder_pytrnsys.spyder")


class PytrnsysConfigPage(PluginConfigPage):

    # --- PluginConfigPage API
    # ------------------------------------------------------------------------
    def setup_page(self):
        pass
