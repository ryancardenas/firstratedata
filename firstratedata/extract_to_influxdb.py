#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
FILE: extract_to_influxdb.py
PROJECT: firstratedata
ORIGINAL AUTHOR: ryancardenas
DATE CREATED: 6/14/23

Extract downloaded market data zip files and load data into an InfluxDB time series database system.
"""

import glob
from pathlib import Path


def get_src_dir_from_user_input():
    max_loops = 10
    loop_ct = 0
    while True:
        src_dir = input("Enter path to top-level directory containing downloaded FirstRateData directories:\n")
        if Path.is_file(Path(src_dir).expanduser()):
            loop_ct += 1
            if loop_ct >= max_loops:
                raise StopIteration
            else:
                print('Please enter path to directory, not an individual file.')
        elif src_dir in ['', '.']:
            src_dir = Path.cwd()
            break
        else:
            src_dir = Path(src_dir).expanduser()
            break
    return src_dir


def get_list_of_zip_files():
    src_dir = get_src_dir_from_user_input()
    fn_list = glob.glob(str(src_dir) + '/**/*.zip', recursive=True)

    max_loops = 10
    loop_ct = 0
    while len(fn_list) == 0:
        loop_ct += 1
        if loop_ct > max_loops:
            raise StopIteration
        else:
            print(f"No zip files found in '{src_dir}' or lower directories. Is there a typo in your directory path?")
            src_dir = get_src_dir_from_user_input()
            fn_list = glob.glob(str(src_dir) + '/**/*.zip', recursive=True)
    print(f"Found {len(fn_list)} zip files.")
    return fn_list


if __name__=='__main__':
    fn_list = get_list_of_zip_files()


