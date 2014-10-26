#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import os
import json

DEFAULT_OPTIONS = {
    'http_stream_server': "http://dm.tuna.moe/danmaku/stream",
    'font_family': "WenQuanYi Micro Hei",
    'font_size': 28,
    'speed_scale': 1.0,
}

_xdg_cfg_dir = os.environ.get(
    "XDG_CONFIG_HOME", os.path.join(os.path.expanduser("~"), ".config"))

_cfg_file = os.path.join(_xdg_cfg_dir, "gdanmaku", "config.json")


def load_config():
    options = dict(DEFAULT_OPTIONS.items())

    if os.path.exists(_cfg_file):
        try:
            with open(_cfg_file, 'r') as f:
                opts = json.load(f)
            options['font_family'] = opts['font_family']
            options['font_size'] = opts['font_size']
            options['speed_scale'] = opts['speed_scale']
            options['http_stream_server'] = opts['http_stream_server']
        except:
            options = dict(DEFAULT_OPTIONS.items())
            save_config(options)
    else:
        if not os.path.exists(os.path.dirname(_cfg_file)):
            os.makedirs(os.path.dirname(_cfg_file))
        save_config(options)

    return options


def save_config(options):
    with open(_cfg_file, 'wb') as f:
        json.dump(options, f, indent=4)

# vim: ts=4 sw=4 sts=4 expandtab
