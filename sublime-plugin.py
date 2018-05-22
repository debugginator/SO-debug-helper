import sublime
import sublime_plugin
import re


class SearchStackOverflowCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        panel = sublime.active_window().find_output_panel("exec")
        traceback = panel.substr(sublime.Region(0, panel.size()))
        error_line = self.parseTraceback(traceback)
        # search_stack_overflow_through_api(traceback)
        panel.insert(edit, panel.size(), "\n"+error_line)

    def parseTraceback(self, traceback):
        p = re.compile(r'^(.*Error:.*)$\n\[Finished', re.MULTILINE)
        return p.findall(traceback)[0]
