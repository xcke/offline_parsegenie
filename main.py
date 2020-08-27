#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project to parse Cisco outputs using the Genie library.
"""

from methods import *
from logzero import logger
import logzero
import logging
import re
import argparse
import json
__author__ = "Gabor, Kis-Hegedus"
__version__ = "0.1.0"
__license__ = "MIT"

""" Imports """
# //TODO: This is something I need to do.
"""Functions & Methods"""
""" Statics"""
# Disable Self-Signed Cert warning for demo urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning


def main(arg):
    if args.debug:
        logzero.loglevel(logging.DEBUG)
        logger.info("Verbose output.")
    else:
        logzero.loglevel(logging.INFO)
    logger.info("hello world!:-)")
    logger.info(args)
    logger.debug("Debug message!")
    """ Main program """
    with open(args.to_parse, 'r') as reader:
        parsed_data = parse(reader.read(), args.cmd, args.nos, args.platform)
        logger.info(json.dumps(parsed_data, indent=4))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("to_parse", help="File that includes the CLI output")
    # Required positional argument
    parser.add_argument("cmd", help="Command output to parse")

    # Optional argument flag which defaults to False
    parser.add_argument("-D", "--debug", action="store_true", default=False)

    # Optional argument to describe the platform (default: cisco)
    parser.add_argument("-p", "--platform", action="store",
                        dest="platform", default="cisco")
    # Optional argument to describe the network operation system (default: ios)
    parser.add_argument("-n", "--nos", action="store",
                        dest="nos", default="iosxe")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
