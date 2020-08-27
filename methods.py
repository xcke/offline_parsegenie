# Some methods to be used generally.
import os
import collections
import logzero
from logzero import logger
import yaml
import csv
from genie.conf.base import Device, Testbed
from genie.libs.parser.utils import get_parser
from genie import parsergen
from pyats.datastructures import AttrDict


def parse(raw_cli_output, cmd, nos, platform):
    # Boilerplate code to get the parser functional
    # tb = Testbed()
    if platform:
        device = Device("new_device", os=nos, platform=platform)
        device.custom.setdefault("abstraction", {})[
            "order"] = ["os", "platform"]
    else:
        device = Device("new_device", os=nos)
        device.custom.setdefault("abstraction", {})["order"] = ["os"]

    device.cli = AttrDict({"execute": None})

    # User input checking of the command provided. Does the command have a Genie parser?
    try:
        get_parser(cmd, device)
    except Exception as e:
        raise Exception(
            "parse_genie: {0} - Available parsers: {1}".format(
                e, "https://pubhub.devnetcloud.com/media/pyats-packages/docs/genie/genie_libs/#/parsers"
            )
        )

    try:
        parsed_output = device.parse(cmd, output=raw_cli_output)
        return parsed_output
    except Exception as e:
        raise Exception(
            "parse_genie: {0} - Failed to parse command output.".format(e
                                                                        )
        )
