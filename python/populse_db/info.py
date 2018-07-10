import sys

# populse_db current version
version_major = 0
version_minor = 0
version_micro = 1
version_extra = ""

# Expected by setup.py: string of form "X.Y.Z"
__version__ = "{0}.{1}.{2}".format(version_major, version_minor, version_micro)


# Expected by setup.py: the status of the project
CLASSIFIERS = ['Development Status :: 5 - Production/Stable',
               'Environment :: Console',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: SQL',
               'Natural Language :: English',
               'Topic :: Database',
              ]

# Project descriptions
NAME = 'populse_db'
DESCRIPTION = 'populse_db'
LONG_DESCRIPTION = '''
==========
populse_db 
==========

The meta-data storage and query system for Populse.
'''
# Populse project
PROJECT = 'populse'
brainvisa_build_model = 'pure_python'

# Other values used in setup.py
ORGANISATION = 'populse'
AUTHOR = 'Populse'
AUTHOR_EMAIL = 'https://github.com/populse/populse_db'
URL = 'http://populse.github.io/populse_db/'
LICENSE = 'CeCILL-B'
VERSION = __version__
CLASSIFIERS = CLASSIFIERS
PLATFORMS = 'OS Independent'
REQUIRES = [
    'python-dateutil',
    'sqlalchemy',
    'lark-parser'
]
EXTRA_REQUIRES = {
    'doc': [
        'sphinx>=1.0',
    ],
    'postgres': [
        'psycopg2-binary',
    ],
}

# tests to run
test_commands = ['%s -m populse_db.test' % sys.executable]
