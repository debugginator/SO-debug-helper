import sublime
import sublime_plugin
import re


"""
Plugin command for Sublime Text. Should be used after an
unsuccessful build through the built in sublime build tool.
Plugin extracts the error line from the build results, then
searches stackoverflow using that line as a query in the
user's default web browser. It is recommended for one to
use a key binding for using this plugin. The default one
is ctrl+alt+b
"""


class SearchStackOverflowCommand(sublime_plugin.TextCommand):

    # Url to which to append a query for searching stackoverflow
    QUERY_URL = 'https://stackoverflow.com/search?tab=votes&q='
    # Minimal answer score to append to the query
    REQUIRED_SCORE = '+score:3'

    """
    Extracts an error from the build result panel and queryies stackoverflow
    for that error.
    """
    def run(self, edit):
        panel = sublime.active_window().find_output_panel("exec")
        if (panel is None):
            sublime.error_message("First build a file using the default " +
                                  "build tool, then run the debug helper in " +
                                  "case that build was unsuccessful.")

        traceback = panel.substr(sublime.Region(0, panel.size()))
        error_line = self.parseTraceback(traceback)
        self.getBestAnswer(error_line)
        # panel.insert(edit, panel.size(), "\n"+best_answer)

    """ Returns an extracted error line from the traceback

    Uses a regular expression to extract the line that will be used for
    querying stackoverflow.
    """
    def parseTraceback(self, traceback):
        p = re.compile(r'^(.*Error:.*)$\n\[Finished', re.MULTILINE)
        return p.findall(traceback)[0] \
                .replace('"', '') \
                .replace('[', '') \
                .replace(']', '')

    """
    Opens a web browser searching stackoverflow for the @param error.
    """
    def getBestAnswer(self, error):
        custom_url = self.QUERY_URL + error  # + self.REQUIRED_SCORE
        import webbrowser
        webbrowser.open(custom_url)
        # print(custom_url)
        # import requests
        # answers = requests.get(custom_url)
        # import urllib.request
        # response = urllib.request.urlopen(custom_url)
        # html = response.read()
        # print(html)
