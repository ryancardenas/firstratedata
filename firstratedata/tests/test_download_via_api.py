#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
FILE: test_download_via_api.py
PROJECT: firstratedata
ORIGINAL AUTHOR: ryancardenas
DATE CREATED: 6/13/23

Tests for code in download_via_apy.py
"""

import pytest

import firstratedata.download_via_api as dva


@pytest.fixture(scope="module")
def uid():
    return 'foo'


def test_index(uid):
    index = dva.Index()
    assert index.api == 'index'
    assert len(index.hist_urls(uid)) == 5


def test_etf(uid):
    etf = dva.ETF()
    assert etf.api == 'etf'
    assert len(etf.hist_urls(uid)) == 312
    assert len(etf.metafiles(uid)) == 2


def test_forex(uid):
    fx = dva.Forex()
    assert fx.api == 'fx'
    assert len(fx.hist_urls(uid)) == 5


def test_stock(uid):
    stock = dva.Stock()
    assert stock.api == 'stock'
    assert len(stock.hist_urls(uid)) == 312
    assert len(stock.metafiles(uid)) == 4


def test_futures(uid):
    futures = dva.Futures()
    assert futures.api == 'futures'
    assert len(futures.hist_urls(uid)) == 10
    assert len(futures.metafiles(uid)) == 2


def test_crypto(uid):
    crypto = dva.Crypto()
    assert crypto.api == 'crypto'
    assert len(crypto.hist_urls(uid)) == 5


def test_tickers():
    apis = [dva.Index(), dva.ETF(), dva.Forex(), dva.Stock(), dva.Futures(), dva.Crypto()]
    for api in apis:
        assert api.api in api.tickers()
        assert api.tickers()[-4:] == '.txt'


def test_readme():
    apis = [dva.Index(), dva.ETF(), dva.Forex(), dva.Stock(), dva.Futures(), dva.Crypto()]
    for api in apis:
        assert api.api in api.readme()
        assert api.readme()[-4:] == '.txt'
