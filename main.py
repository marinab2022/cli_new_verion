from ensurepip import version
from re import sub
import subprocess
from sys import stderr, stdout
import sys
from turtle import st

name_repo= 'hello'
version= ''
charts_original= 'https://www.kleinloog.ch/hello-helm/'
#version =input ("Enter version number: ")
subprocess.check_call(['helm','repo', 'add',name_repo , charts_original] )
subprocess.check_call(['helm','repo', 'update'] )
subprocess.check_call( ['helm','install','my-hello', 'hello/hello', '--version', '0.4.0-rc2'])





