#!/usr/bin/env python
#encoding=utf-8


from __future__ import print_function, unicode_literals
from json import loads

from six.moves import input
from six.moves.urllib_parse import quote
from requests import session


class ZoomEye(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.access_token = ''
        self.s = session()

    def login(self):
        resp = self.s.post(
            'https://api.zoomeye.org/auth/login',
            json={
                'email': self.email,
                'password': self.password,
            },
        )

        if resp.status_code == 200:
            self.access_token = resp.json()['access_token']
            return True

        return False

    def search(self, query, type, limitation=100):
        assert self.access_token

        resp = self.s.get(
            'https://api.zoomeye.org/streaming/search?q={}&t={}&l={}'.format(
                quote(query),
                type,
                limitation,
            ),
            headers={
                'Authorization': 'JWT {}'.format(self.access_token),
            },
            stream=True,
        )

        for item in resp.iter_lines():
            yield loads(item)

        return

    def count(self, query, type):
        assert self.access_token

        resp = self.s.get(
            'https://api.zoomeye.org/search/count?q={}&t={}'.format(
                quote(query),
                type,
            ),
            headers={
                'Authorization': 'JWT {}'.format(self.access_token),
            },
        )

        return resp.json()

    def user_info(self):
        assert self.access_token

        resp = self.s.get(
            'https://api.zoomeye.org/user/info',
            headers={
                'Authorization': 'JWT {}'.format(self.access_token),
            },
        )

        return resp.json()

