import sublime
import sublime_plugin
import re


class UnicodetocharacterCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		def toChartacter(word):
			return word.group(0).encode("utf-8").decode("unicode-escape")
		for region in self.view.sel():
			if not region.empty():
				r = self.view.substr(region)
				chartacters = re.sub(r'(\\[uU]\w{4})', toChartacter, r)
				self.view.replace(edit, region, chartacters)

