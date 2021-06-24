# coding:utf-8

import pkg_resources
import click
from click_help_colors import HelpColorsGroup


#class MyCLI(click.MultiCommand):
class MyCLI(HelpColorsGroup):
	def __init__(self, *args, **kwargs):
		super(MyCLI, self).__init__(*args, **kwargs)
		self.entry_points = {}
		for entry_point in pkg_resources.iter_entry_points("Q2.plugins"):
			name = entry_point.name.split("-",1)[1]
			self.entry_points[name] = entry_point

	def list_commands(self, ctx):
		return sorted(self.entry_points)

	def get_command(self, ctx, name):
		return self.entry_points[name].load()


@click.command(cls=MyCLI, help_headers_color='yellow', help_options_color='blue')
def q2():
	pass

