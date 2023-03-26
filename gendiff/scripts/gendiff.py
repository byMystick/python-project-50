#!/usr/bin/env python3.10

import argparse
from gendiff.diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='path to first file')
    parser.add_argument('second_file', type=str, help='path to second file')
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output', default='stylish')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
