# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2024, Damian Birchler
#
# Licensed under the terms of the GNU General Public License v3
# ----------------------------------------------------------------------------
"""
Pytrnsys Plugin.
"""

# Third-party imports
from qtpy.QtGui import QIcon

# Spyder imports
from spyder.api.plugins import Plugins, SpyderDockablePlugin
from spyder.api.translations import get_translation

# Local imports
from spyder_pytrnsys.spyder.confpage import PytrnsysConfigPage
from spyder_pytrnsys.spyder.widgets import PytrnsysWidget

_ = get_translation("spyder_pytrnsys.spyder")


class Pytrnsys(SpyderDockablePlugin):
    """
    Pytrnsys plugin.
    """

    NAME = "spyder_pytrnsys"
    REQUIRES = []
    OPTIONAL = []
    WIDGET_CLASS = PytrnsysWidget
    CONF_SECTION = NAME
    CONF_WIDGET_CLASS = PytrnsysConfigPage
    TABIFY = [Plugins.Editor]
    FILE_EXTENSIONS = [".pytrndia"]

    # --- Signals

    # --- SpyderDockablePlugin API
    # ------------------------------------------------------------------------
    def get_name(self):
        return _("Pytrnsys")

    def get_description(self):
        return _("Pytrnsys GUI for Spyder")

    def get_icon(self):
        return QIcon()

    def on_initialize(self):
        widget = self.get_widget()
        

    def check_compatibility(self):
        valid = True
        message = ""  # Note: Remember to use _("") to localize the string
        return valid, message

    def on_close(self, cancellable=True):
        return True

    # --- Public API
    # ------------------------------------------------------------------------
