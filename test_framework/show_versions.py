import sys

from django import get_version


versions = '''
=== VERSIONS ======================
 Python = {python}
 Django = {django}
===================================
'''.format(
    python=sys.version.replace('\n', ' '),
    django=get_version(),
)


print(versions)
