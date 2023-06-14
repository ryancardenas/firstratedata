#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
FILE: download_via_api.py
PROJECT: firstratedata
ORIGINAL AUTHOR: ryancardenas
DATE CREATED: 6/13/23

Connect to FirstRateData endpoints via provided API. Downloads zip and txt files to local drives.
"""

import os
from pathlib import Path
import requests
import string


class Index:
    """Class containing parameters for available index market data."""
    def __init__(self):
        self.api = "index"
        self.period = 'full'
        self.timeframes = ["1min", "5min", "30min", "1hour", "1day"]

    def hist_urls(self, uid):
        result = []
        for timeframe in reversed(self.timeframes):
            msg = (
                "https://firstratedata.com/api/data_file?"
                f"type={self.api}"
                f"&period={self.period}"
                f"&timeframe={timeframe}"
                f"&userid={uid}"
            )
            result.append(msg)
        return result

    def tickers(self):
        return 'https://firstratedata.com/api_ticker_files/index_ticker_dates_listing.txt'

    def readme(self):
        return 'https://firstratedata.com/_readme/index.txt'


class ETF:
    """Class containing parameters for available ETF market data."""
    def __init__(self):
        self.api = "etf"
        self.period = 'full'
        self.ticker_ranges = list(string.ascii_uppercase)
        self.timeframes = ["1min", "5min", "30min", "1hour", "1day"]
        self.adjustments = ["adj_split", "adj_splitdiv", "UNADJUSTED"]
        self.metafile_types = ["splits", "dividends"]

    def hist_urls(self, uid):
        result = []
        for ticker_range in self.ticker_ranges:
            for timeframe in reversed(self.timeframes):
                for adj in self.adjustments:
                    if adj == 'UNADJUSTED':
                        if timeframe in ['1min', '1day']:
                            msg = (
                                "https://firstratedata.com/api/data_file?"
                                f"type={self.api}"
                                f"&period={self.period}"
                                f"&ticker_range={ticker_range}"
                                f"&timeframe={timeframe}"
                                f"&adjustment={adj}"
                                f"&userid={uid}"
                            )
                            result.append(msg)
                    else:
                        msg = (
                            "https://firstratedata.com/api/data_file?"
                            f"type={self.api}"
                            f"&period={self.period}"
                            f"&ticker_range={ticker_range}"
                            f"&timeframe={timeframe}"
                            f"&adjustment={adj}"
                            f"&userid={uid}"
                        )
                        result.append(msg)
        return result

    def metafiles(self, uid):
        result = []
        for metafile in self.metafile_types:
            msg = f'https://firstratedata.com/api/meta_file?type={self.api}&metafile_type={metafile}&userid={uid}'
            result.append(msg)
        return result

    def tickers(self):
        return 'https://firstratedata.com/api_ticker_files/etf_ticker_dates_listing.txt'

    def readme(self):
        return 'https://firstratedata.com/_readme/etf.txt'


class Forex:
    """Class containing parameters for available forex market data."""
    def __init__(self):
        self.api = "fx"
        self.period = 'full'
        self.timeframes = ["1min", "5min", "30min", "1hour", "1day"]

    def hist_urls(self, uid):
        result = []
        for timeframe in reversed(self.timeframes):
            msg = (
                "https://firstratedata.com/api/data_file?"
                f"type={self.api}"
                f"&period={self.period}"
                f"&timeframe={timeframe}"
                f"&userid={uid}"
            )
            result.append(msg)
        return result

    def tickers(self):
        return 'https://firstratedata.com/api_ticker_files/fx_ticker_dates_listing.txt'

    def readme(self):
        return 'https://firstratedata.com/_readme/fx.txt'


class Stock:
    """Class containing parameters for available stock market data."""
    def __init__(self):
        self.api = "stock"
        self.period = 'full'
        self.ticker_ranges = list(string.ascii_uppercase)
        self.timeframes = ["1min", "5min", "30min", "1hour", "1day"]
        self.adjustments = ["adj_split", "adj_splitdiv", "UNADJUSTED"]
        self.metafile_types = ["splits", "dividends"]

    def hist_urls(self, uid):
        result = []
        for ticker_range in self.ticker_ranges:
            for timeframe in reversed(self.timeframes):
                for adj in self.adjustments:
                    if adj == 'UNADJUSTED':
                        if timeframe in ['1min', '1day']:
                            msg = (
                                "https://firstratedata.com/api/data_file?"
                                f"type={self.api}"
                                f"&period={self.period}"
                                f"&ticker_range={ticker_range}"
                                f"&timeframe={timeframe}"
                                f"&adjustment={adj}"
                                f"&userid={uid}"
                            )
                            result.append(msg)
                    else:
                        msg = (
                            "https://firstratedata.com/api/data_file?"
                            f"type={self.api}"
                            f"&period={self.period}"
                            f"&ticker_range={ticker_range}"
                            f"&timeframe={timeframe}"
                            f"&adjustment={adj}"
                            f"&userid={uid}"
                        )
                        result.append(msg)
        return result

    def metafiles(self, uid):
        result = [
            'https://f004.backblazeb2.com/file/frd-api/delisted_tickers_A-L_78jghsE.zip',
            'https://f004.backblazeb2.com/file/frd-api/delisted_tickers_M-Z_8jfu6Yh.zip',
        ]
        for metafile in self.metafile_types:
            msg = f'https://firstratedata.com/api/meta_file?type={self.api}&metafile_type={metafile}&userid={uid}'
            result.append(msg)
        return result

    def tickers(self):
        return 'https://firstratedata.com/api_ticker_files/stock_ticker_dates_listing.txt'

    def readme(self):
        return 'https://firstratedata.com/_readme/stock.txt'


class Futures:
    """Class containing parameters for available futures market data."""
    def __init__(self):
        self.api = "futures"
        self.period = 'full'
        self.timeframes = ["1min", "5min", "30min", "1hour", "1day"]
        self.adjustments = ['contin_adj ', 'contin_UNadj']
        self.metafile_timeframes = ['1min', '1day']

    def hist_urls(self, uid):
        result = []
        for timeframe in reversed(self.timeframes):
            for adj in self.adjustments:
                msg = (
                    "https://firstratedata.com/api/data_file?"
                    f"type={self.api}"
                    f"&period={self.period}"
                    f"&timeframe={timeframe}"
                    f"&adjustment={adj}"
                    f"&userid={uid}"
                )
                result.append(msg)
        return result

    def metafiles(self, uid):
        result = []
        for meta_timeframe in self.metafile_timeframes:
            msg = (
                f'https://firstratedata.com/api/futures_contract?'
                f'contract_files=archive'
                f'&timeframe={meta_timeframe}'
                f'&userid={uid}'
            )
            result.append(msg)
        return result

    def tickers(self):
        return 'https://firstratedata.com/api_ticker_files/futures_ticker_dates_listing.txt'

    def readme(self):
        return 'https://firstratedata.com/_readme/futures.txt'


class Crypto:
    """Class containing parameters for available crypto market data."""
    def __init__(self):
        self.api = "crypto"
        self.period = 'full'
        self.timeframes = ["1min", "5min", "30min", "1hour", "1day"]

    def hist_urls(self, uid):
        result = []
        for timeframe in reversed(self.timeframes):
            msg = (
                "https://firstratedata.com/api/data_file?"
                f"type={self.api}"
                f"&period={self.period}"
                f"&timeframe={timeframe}"
                f"&userid={uid}"
            )
            result.append(msg)
        return result

    def tickers(self):
        return 'https://firstratedata.com/api_ticker_files/crypto_ticker_dates_listing.txt'

    def readme(self):
        return 'https://firstratedata.com/_readme/crypto.txt'


def download_zip(url, trg_subdir, chunk_size=1024):
    """Downloads zip files from specified url."""
    try:
        r = requests.get(url, stream=True)
        if r.text == 'no active subscription':
            raise ConnectionRefusedError(
                "Server responded with message 'no active subscription'; "
                "please verify that UserID belongs to an active subscription."
            )
        trg_fn = trg_subdir + r.url.split('/')[-1]
        assert trg_fn[-4:] == '.zip', f"Expected .zip file format; downloaded file format is {trg_fn[-4:]}"
        with open(trg_fn, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    except Exception as e:
        print(f"Error downloading {url}: {type(e).__name__} -- {str(e)}")


def download_txt(url, trg_subdir):
    """Downloads txt files from specified url."""
    assert url[-4:] == '.txt', f"Expected .txt file format; downloaded file format is {url[-4:]}"
    try:
        r = requests.get(url)
        if r.text == 'no active subscription':
            raise ConnectionRefusedError(
                "Server responded with message 'no active subscription'; "
                "please verify that UserID belongs to an active subscription."
            )
        trg_fn = trg_subdir + r.url.split('/')[-1]
        assert trg_fn[-4:] == '.txt'
        with open(trg_fn, "w") as f:
            lines = r.text.split("\n")
            f.writelines(lines)
    except Exception as e:
        print(f"Error downloading {url}: {type(e).__name__} -- {str(e)}")


def download_firstratedata(trg_dir):
    try:
        from firstratedata.credentials import UID
    except ImportError as e:
        print(e)
        UID = input("Please enter FirstRateData API UserID:")

    apis = [Index(), ETF(), Forex(), Stock(), Futures(), Crypto()]

    for api in apis:
        trg_subdir = trg_dir + f"/{api.api}/"
        if not os.path.exists(trg_subdir):
            os.makedirs(trg_subdir)

        ticker = api.tickers()
        print(f"Downloading tickers: {ticker}...")
        download_txt(ticker, trg_subdir)

        readme = api.readme()
        print(f"Downloading readme: {readme}...")
        download_txt(readme, trg_subdir)

        # Get historical data files.
        file_count = 0
        urls = api.hist_urls(UID)
        num_urls = len(urls)
        for url in urls:
            file_count += 1
            print(f"Downloading file {api.api}#{file_count:0>3} / {num_urls}: {url}...")
            download_zip(url, trg_subdir)

        # Get metadata files.
        if hasattr(api, 'metafiles'):
            metafiles = api.metafiles(UID)
            file_count = 0
            num_metafiles = len(metafiles)
            for meta in metafiles:
                file_count += 1
                print(f"Downloading file metafile#{file_count:0>3} / {num_metafiles}: {meta}...")
                if meta[-4:] == '.zip':
                    download_zip(meta, trg_subdir)
                elif meta[-4:] == '.txt':
                    download_txt(meta, trg_subdir)


if __name__ == "__main__":
    trg_dir = str(Path("./").expanduser())
    download_firstratedata(trg_dir=trg_dir)
