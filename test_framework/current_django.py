from django import VERSION


def django_version():
    """
    Print string representation of the current version of Django. should tally
    with tox's opinion.
    """
    return('django{}{}'.format(VERSION[0], VERSION[1]))


if __name__ == '__main__':
    print(django_version())
