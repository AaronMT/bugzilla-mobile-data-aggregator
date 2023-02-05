#! /usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse
import sys

from bz import BugzillaHelper


def parse_args(cmdline_args):
    parser = argparse.ArgumentParser(
        description='Query Bugzilla API for data on a given product.'
    )
    parser.add_argument(
        '--product',
        choices=['Fenix', 'Focus'],
        required=True,
        help='Provide a Bugzilla product name'
    )

    return parser.parse_args(args=cmdline_args)


def main():
    args = parse_args(sys.argv[1:])

    BugzillaHelperClient = BugzillaHelper()

    query = dict(product=args.product, component="UI Tests",
                 status="RESOLVED", resolution="FIXED")
    bugs = BugzillaHelperClient.query(query)

    for bug in bugs:
        print(bug.id)


if __name__ == '__main__':
    main()
