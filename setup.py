import os
import sys

sys.path.append ('Transcrypt/modules/org/transcrypt')
import __base__

from setuptools import setup

def read (*paths):
	with open (os.path.join (*paths), 'r') as aFile:
		return aFile.read()

setup (
	name = 'Transcrypt',
	version = __base__.__envir__.transpilerVersion,
	description = 'Python to JavaScript transpiler, supporting multiple inheritance and generating lean, highly readable code',
	long_description = (
		read ('README.rst') + '\n\n' +
		read ('license_reference.txt')
	),
	keywords = ['python', 'javascript', 'transpiler', 'compiler', 'browser', 'web', 'multiple inheritance', 'transcrypt', 'kivy', 'django'],
	url = 'http://www.transcrypt.org',	
	license = 'Apache 2.0',
	author = 'Jacques de Hooge',
	author_email = 'jacques.de.hooge@qquick.org',
	packages = ['Transcrypt'],	
	include_package_data = True,
	classifiers = [
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: Other/Proprietary License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.5',
	],
)
