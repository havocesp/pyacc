# -*- coding: utf-8 -*-
"""
 PyACC
"""
from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent  # type: Path
#
# sys.path.append(str(ROOT_DIR))
# sys.path.append(str(ROOT_DIR.parent))

README_FILE = ROOT_DIR.parent.joinpath('README.md')
REQUIREMENTS_FILE = ROOT_DIR.parent.joinpath('requirements.txt')
REQUIREMENTS = list()

if REQUIREMENTS_FILE.is_file():
    raw = REQUIREMENTS_FILE.read_text(encoding='utf8')

    for ch in ['=', '>', '<']:
        raw = raw.replace(ch, '@@@')

    lines = raw.split('\n') if raw and len(raw) else str()
    if len(lines):
        lines = [line.split('@@@')[0] for line in lines]
        REQUIREMENTS.extend(lines)
else:
    REQUIREMENTS_FILE.touch(exist_ok=True)

__project__ = __package__.title()
__author__ = 'Daniel J. Umpierrez'
__version__ = '0.1.2'
__license__ = 'UNLICENSE'
__site__ = 'https://github.com/havocesp/{}'.format(__package__)
__email__ = 'umpierrez@pm.me'
__description__ = __doc__
__requirements__ = REQUIREMENTS_FILE.read_text().split('\n')
__keywords__ = ''
__long_description__ = README_FILE.read_text()

__all__ = ['__project__', '__author__', '__keywords__', '__version__', '__license__', '__description__', '__email__',
           '__site__', '__keywords__', '__requirements__']
