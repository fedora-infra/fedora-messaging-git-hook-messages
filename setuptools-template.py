#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from argparse import ArgumentParser, FileType

from setuptools.config.setupcfg import read_configuration

SUBSTITUTIONS = ["version", "description", "long_description"]


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-s",
        "--setup-file",
        default="setup.cfg",
        help="Path to the setup.cfg file if not in the current directory",
    )
    parser.add_argument("-o", "--output", default="-", type=FileType("w", encoding="UTF-8"))
    parser.add_argument("input", type=FileType("r"))
    return parser.parse_args()


def main():
    args = parse_args()
    conf_dict = read_configuration(args.setup_file)
    for line in args.input:
        for sub in SUBSTITUTIONS:
            line = line.replace(f"@@{sub.upper()}@@", conf_dict["metadata"][sub])
        args.output.write(line)


if __name__ == "__main__":
    main()
