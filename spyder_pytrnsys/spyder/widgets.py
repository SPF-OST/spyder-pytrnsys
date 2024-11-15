# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2024, Damian Birchler
#
# Licensed under the terms of the GNU General Public License v3
# ----------------------------------------------------------------------------
"""
Pytrnsys Main Widget.
"""


# Third party imports
from qtpy.QtWidgets import QHBoxLayout, QLabel


# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.translations import get_translation

from spyder.api.widgets.main_widget import PluginMainWidget


# Localization
_ = get_translation("spyder_pytrnsys.spyder")


class PytrnsysActions:
    ExampleAction = "example_action"


class PytrnsysToolBarSections:
    ExampleSection = "example_section"


class PytrnsysOptionsMenuSections:
    ExampleSection = "example_section"


class PytrnsysWidget(PluginMainWidget):

    # PluginMainWidget class constants

    # Signals

    def __init__(self, name=None, plugin=None, parent=None):
        super().__init__(name, plugin, parent)

        # Create an example label
        self._example_label = QLabel("Example Label")

        # Add example label to layout
        layout = QHBoxLayout()
        layout.addWidget(self._example_label)
        self.setLayout(layout)

    # --- PluginMainWidget API
    # ------------------------------------------------------------------------
    def get_title(self):
        return _("Pytrnsys")

    def get_focus_widget(self):
        pass

    def setup(self):
        # Create an example action
        example_action = self.create_action(
            name=PytrnsysActions.ExampleAction,
            text="Example action",
            tip="Example hover hint",
            icon=self.create_icon("spyder"),
            triggered=lambda: print("Example action triggered!"),
        )

        # Add an example action to the plugin options menu
        menu = self.get_options_menu()
        self.add_item_to_menu(
            example_action,
            menu,
            PytrnsysOptionsMenuSections.ExampleSection,
        )

        # Add an example action to the plugin toolbar
        toolbar = self.get_main_toolbar()
        self.add_item_to_toolbar(
            example_action,
            toolbar,
            PytrnsysOptionsMenuSections.ExampleSection,
        )

    def update_actions(self):
        pass

    @on_conf_change
    def on_section_conf_change(self, section):
        pass

    # --- Public API
    # ------------------------------------------------------------------------
