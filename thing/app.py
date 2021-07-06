"""Module to say Hello"""
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--name')
    args = parser.parse_args()
    print(f'Hello {args.name} 👋')
