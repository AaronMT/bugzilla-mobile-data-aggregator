#! /usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import absolute_import

from lib.bugzilla_conn import BugzillaConn


class Bugzilla:
    def __init__(self) -> None:
        self.conn = BugzillaConn()

    def get_bugs(self, bug_ids: list) -> list:
        bugs = self.conn.bz_client.getbugs(bug_ids)
        return bugs

    def build_query(self, query: dict) -> dict:
        formatted_query = self.conn.bz_client.build_query(query)
        return formatted_query

    def query(self, query: dict) -> list:
        bugs = self.conn.bz_client.query(query)
        return bugs

    def get_query_from_url(self, url: str) -> dict:
        query = self.conn.bz_client.url_to_query(url)
        return query


class BugzillaHelper:
    def __init__(self) -> None:
        self.bugzilla = Bugzilla()

    def get_bugs(self, bugs: list) -> list:
        """Get a list of bugs from Bugzilla."""
        return self.bugzilla.get_bugs(bugs)

    def build_query(self, query: dict) -> dict:
        """Build a query for Bugzilla."""
        return self.bugzilla.build_query(query)

    def query(self, query: dict) -> list:
        """Query Bugzilla."""
        return self.bugzilla.query(query)

    def get_query_from_url(self, url: str) -> dict:
        """Get a query from a Bugzilla URL."""
        return self.bugzilla.get_query_from_url(url)
