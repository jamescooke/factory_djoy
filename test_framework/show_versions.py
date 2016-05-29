import sys

from django import get_version


def versions():
    return '''
=== VERSIONS ======================
 Python = {python}
 Django = {django}
===================================
'''.format(
        python=sys.version.replace('\n', ' '),
        django=get_version(),
    )


if __name__ == '__main__':
    print(versions())
