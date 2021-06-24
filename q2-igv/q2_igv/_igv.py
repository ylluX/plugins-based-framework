# coding:utf-8

import click
from click_help_colors import HelpColorsCommand


@click.command(cls=HelpColorsCommand, 
               help_headers_color="yellow", 
			   help_options_color="blue", 
			   short_help="show sv and snv by igv")
@click.argument("bam_file")
@click.option("-o", "--out")
def igv(bam_file, out):
	click.secho('[igv]', fg='red')
	click.secho('  bam_file: '+bam_file, fg='green')
	click.secho('  out: '+str(out), fg='green')

