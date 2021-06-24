import click
from click_help_colors import HelpColorsGroup


@click.group(cls=HelpColorsGroup,
             help_headers_color="yellow",
			 help_options_color="blue",
             short_help="calling SNV")
def cli():
	pass

@cli.command()
@click.argument("bam_file")
@click.option("--thread", type=int, default=4)
def snv(bam_file, thread):
	click.secho("[snv]", fg="red")
	click.secho("  bam_file: "+bam_file, fg="green")
	click.secho("  thread: "+str(thread), fg="green")

@cli.command()
@click.argument("bam_file")
@click.option("--thread", type=int, default=4)
def batch(bam_file, thread):
	click.secho("[snv_batch]", fg="red")
	click.secho("  bam_file: "+bam_file, fg="green")
	click.secho("  thread: "+str(thread), fg="green")

