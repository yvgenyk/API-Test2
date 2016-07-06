from distutils.core import setup
from glob import glob
import py2exe

includes = ['docx','sip','collections.abc','requests']
packages =['lxml']
data_files = [("Microsoft.VC90.CRT", glob(r'C:\Windows\WinSxS\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.21022.218_none_34f1b3a4277681aa\*.*'))]

setup(
	options = {"py2exe":{"includes":includes,
						 "packages":packages}},
	windows = ['main.py'],
	data_files = data_files
)