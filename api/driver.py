# coding=utf-8

from iota import Iota
import pandas as pd
import cryptography as Cryptography
import address as Address
import upload as Upload
import logger as Logger
import conn as Conn
import time


class Session:

    def __init__(self, seed=None, conn=None, bundle_amt=4):
        if seed is None:
            seed = Address.generate_seed()
        if conn is None:
            conn = Conn.get_active_full_nodes(seed)[0]
        self.seed = seed
        self.conn = conn
        self.api = Iota(conn, seed)
        self.bundle_amt = bundle_amt   # max amount of transactions per bundle

    def data_to_tangle(self, data, tag='', address=Address.generate_address()):
        start_time = time.time()
        if isinstance(data, pd.DataFrame):
            step = self.bundle_amt
            begin_row = 0
            end_row = step
            while end_row <= len(data):
                result = Upload.bundle_to_tangle(self.api, address, data.iloc
                                                 [begin_row:end_row], tag)
                end_time = time.time()
                Logger.print_bundle_result(result, end_time-start_time)
                start_time = end_time
                begin_row += step
                end_row += step
        else:
            result = Upload.tx_to_tangle(self.api, address, data, tag)
            end_time = time.time()
            Logger.print_tx_result(result, end_time-start_time)

    def payment_to_tangle(self, value, data='', tag='',
                          address=Address.generate_address()):
        start_time = time.time()
        result = Upload.tx_to_tangle(self.api, address, data, tag, value)
        end_time = time.time()
        Logger.print_tx_result(result, end_time-start_time)

    # transform any data into an IOTA wallet address
    def convert_into_address(self, data, salt=None):
        return Cryptography.convert(data, salt)
