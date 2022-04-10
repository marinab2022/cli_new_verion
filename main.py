import subprocess
import click


@click.command()
@click.option('--version', default='0.4.0-rc2', help='version: 0.4.0-rc1, 0.3.0, 0.2.0, 0.1.0')
@click.option('--charts', default='https://www.kleinloog.ch/hello-helm/', help='charts url')
@click.option('--repo', default='hello', help='repo name')
@click.option('--release', default='my-hello', help= 'release name')
def cli(version, charts, repo, release): 
    subprocess.check_call(['helm','repo', 'add', repo, charts] )
    subprocess.check_call(['helm','repo', 'update'] )
    subprocess.check_call( ['helm','install',release , 'hello/hello', '--version', version])


if __name__ == '__main__':
    cli()





