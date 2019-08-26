#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(repository='migrations', url='postgresql://docker:docker@localhost:5432/postgres', debug='False')
