""" Adapted from https://github.com/borist/SublimePaneNavigation
"""

import sublime
import sublime_plugin


class NextPaneCommand(sublime_plugin.TextCommand):
    """
    Switch to the next group.
    """
    def run(self, view):
        change_pane(self, view, 1)

class PrevPaneCommand(sublime_plugin.TextCommand):
    """
    Switch to the previous group.
    """
    def run(self, view):
        change_pane(self, view, -1)

class NextViewInPaneCommand(sublime_plugin.TextCommand):
    """
    Switch to the next tab in the active pane.
    Like sublime's builtin next_view, but stays within the active pane
    """
    def run(self, view):
        change_tab_within_pane(self, view, 1)

class PrevViewInPaneCommand(sublime_plugin.TextCommand):
    """
    Switch to the previous tab in the active pane.
    Like sublime's builtin prev_view, but stays within the active pane
    """
    def run(self, view):
        change_tab_within_pane(self, view, -1)

def change_pane(self, view, direction):
    """
    Jump through all panes
    @param direction: 1 to navigate to next pane, -1 to navigate to
                        previous pane
    """
    window = self.view.window()
    group_index, view_index = window.get_view_index(window.active_view())
    group_index = group_index + direction
    if group_index < 0:
        group_index = window.num_groups() - 1
    elif group_index >= window.num_groups():
        group_index = 0
    window.focus_group(group_index)

def change_tab_within_pane(self, view, direction):
    """
    Jump to a tab within the current pane
    @param direction: 1 to navigate to next tab, -1 to navigate to
                        previous tab
    """
    window = self.view.window()
    group_index, view_index = window.get_view_index(window.active_view())
    views = window.views_in_group(group_index)
    window.focus_view(views[(view_index + direction) % len(views)])
