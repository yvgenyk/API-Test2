from distutils.core import setup
import py2exe

includes = ['docx','sip','collections.abc','requests']
packages =['lxml']

setup(
	options = {"py2exe":{"includes":includes,
						 "packages":packages}},
	windows = ['main.py']
)