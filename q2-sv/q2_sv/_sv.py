import click
from click_help_colors import HelpColorsCommand

@click.command(cls=HelpColorsCommand,
               help_headers_color="yellow",
			   help_options_color="blue",
               short_help="calling SV")
@click.argument("bam_file")
@click.option("--verbose", is_flag=True, default=False)
def sv(bam_file, verbose):
	click.secho("[sv]", fg="red")
	click.secho("  bam_file: "+bam_file, fg="green")
	click.secho("  verbose: "+str(verbose), fg="green")

@click.command(cls=HelpColorsCommand,
               help_headers_color="yellow",
			   help_options_color="blue",
               short_help="calling SV by batch")
@click.argument("bam_file")
@click.option("--verbose", is_flag=True, default=False)
def sv_batch(bam_file, verbose):
	click.secho("[sv_batch]", fg="red")
	click.secho("  bam_file: "+bam_file, fg="green")
	click.secho("  verbose: "+str(verbose), fg="green")
