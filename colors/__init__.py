VERSION = (0, 0, 1, 'alpha', 0)


def get_git_revision():
    #TODO
    pass


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%s pre-alpha' % version
    else:
        if VERSION[3] != 'final':
            version = '%s %s %s' % (version, VERSION[3], VERSION[4])
    git_rev = get_git_revision()
    if git_rev:
        version = "%s %s" % (version, git_rev)
    return version
