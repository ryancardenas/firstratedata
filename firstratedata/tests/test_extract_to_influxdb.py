#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
FILE: test_extract_to_influxdb.py
PROJECT: firstratedata
ORIGINAL AUTHOR: ryancardenas
DATE CREATED: 6/15/23

Tests for code in extract_to_influxdb.py
"""

from pathlib import Path
import pytest

import firstratedata.extract_to_influxdb as eti


class Test_get_src_dir_from_user_input:
    """Checks that get_src_dir_from_user_input() meets the following expectations:
    - Returns active directory if user enters '' or '.'.
    - Raises StopIteration if user enters file path.
    - Output type is Path.
    """

    @pytest.mark.parametrize('entry', ['', '.'])
    def test_returns_active_directory_if_user_enters_cwd_pattern(self, monkeypatch, entry):
        monkeypatch.setattr('builtins.input', lambda _: entry)
        res = eti.get_src_dir_from_user_input()
        assert res == Path.cwd()

    def test_raises_exception_if_user_enters_file_path(self, monkeypatch, tmp_path):
        tmp_data = 'foo'
        tmp_file_path = tmp_path / 'tmp_file.txt'
        tmp_file_path.write_text(tmp_data)

        monkeypatch.setattr('builtins.input', lambda _: tmp_file_path)
        with pytest.raises(StopIteration) as exc_info:
            res = eti.get_src_dir_from_user_input()
        assert isinstance(exc_info.value, StopIteration)

    def test_output_type_is_path(self, monkeypatch, tmp_path):
        monkeypatch.setattr('builtins.input', lambda _: tmp_path)
        res = eti.get_src_dir_from_user_input()
        assert isinstance(res, Path)


class Test_get_list_of_zip_files:
    """Checks that get_list_of_zip_files() meets the following expectations:
    - Raises StopIteration if user enters directory that does not exist.
    - Raises StopIteration if user enters directory containing no zip files.
    - Returns list with correct number of paths.
    - Output type is list.
    """

    @pytest.mark.parametrize('missing_directory', ['does', 'not', 'exist'])
    def test_raises_exception_if_directory_does_not_exist(self, monkeypatch, tmp_path, missing_directory):
        monkeypatch.setattr('builtins.input', lambda _: str(tmp_path / missing_directory))
        with pytest.raises(StopIteration) as exc_info:
            res = eti.get_list_of_zip_files()
        assert isinstance(exc_info.value, StopIteration)

    @pytest.mark.parametrize(
        'files',
        [
            ('a', 'b', 'c', 'd', 'e', 'f'),
            ('1', '2', '3', '4'),
            ('larry', 'mo', 'curly'),
            (),
        ]
    )
    def test_raises_exception_if_directory_contains_no_zip_files(self, monkeypatch, tmp_path, files):
        for name in files:
            trg = tmp_path / f"{name}.not_a_zip_file"
            trg.write_text('')
        monkeypatch.setattr('builtins.input', lambda _: tmp_path)
        with pytest.raises(StopIteration) as exc_info:
            res = eti.get_list_of_zip_files()
        assert isinstance(exc_info.value, StopIteration)

    @pytest.mark.parametrize(
        'files',
        [
            ('a', 'b', 'c', 'd', 'e', 'f'),
            ('1', '2', '3', '4'),
            ('larry', 'mo', 'curly'),
        ]
    )
    def test_returns_correct_number_of_paths(self, monkeypatch, tmp_path, files):
        for name in files:
            trg = tmp_path / f"{name}.zip"
            trg.write_text('')
        monkeypatch.setattr('builtins.input', lambda _: tmp_path)
        res = eti.get_list_of_zip_files()
        assert len(res) == len(files)

    @pytest.mark.parametrize('files', [('a', 'b', 'c', 'd', 'e', 'f')])
    def test_output_type_is_list(self, monkeypatch, tmp_path, files):
        for name in files:
            trg = tmp_path / f"{name}.zip"
            trg.write_text('')
        monkeypatch.setattr('builtins.input', lambda _: tmp_path)
        res = eti.get_list_of_zip_files()
        assert isinstance(res, list)
