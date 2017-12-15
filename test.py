#!/usr/bin/env python
#encoding=utf-8


from sys import argv
from argparse import ArgumentParser
from pprint import pprint

from zoomeye import ZoomEye


def login(func):
    def wrapper(args):
        z = ZoomEye(args.email, args.password)

        if not z.login():
            print('login error')
            return

        args.z = z
        return func(args)

    return wrapper


@login
def search(args):
    z = args.z
    for item in z.search(args.query, args.type, args.limit):
        print(item)


@login
def user_info(args):
    z = args.z
    pprint(z.user_info())


@login
def count(args):
    z = args.z
    pprint(z.count(args.query, args.type))


parser = ArgumentParser(argument_default=['-h'], add_help=True)
parser.add_argument('-e', '--email', help='email')
parser.add_argument('-p', '--password', help='password')

subparsers = parser.add_subparsers()

sp = subparsers.add_parser('search', help='Search')
sp.add_argument('-q', '--query', default='', help='keywords')
sp.add_argument('-t', '--type', default='host', help='type:web/host')
sp.add_argument('-l', '--limit', type=int, default=100, help='limitation')
sp.set_defaults(func=search)

cp = subparsers.add_parser('count', help='Count')
cp.add_argument('-q', '--query', default='', help='keywords')
cp.add_argument('-t', '--type', default='host', help='type:web/host')
cp.set_defaults(func=count)

up = subparsers.add_parser('user', help='User Information')
up.set_defaults(func=user_info)

args = parser.parse_args()
if len(argv) == 1:
    parser.print_help()
else:
    args.func(args)
