import sublime
import sublime_plugin


class SearchStackOverflowCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        panel = sublime.active_window().find_output_panel("exec")
        traceback = panel.substr(sublime.Region(0, panel.size()))
        # search_stack_overflow_through_api(traceback)
        panel.insert(edit, panel.size(), "\nHello, World!")
