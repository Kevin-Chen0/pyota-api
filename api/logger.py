# coding=utf-8

from iota import TryteString
from datetime import datetime


'''
    All timestamps will be in GMT time
'''


def print_tx_result(result, timer):
    for bundle in result.values():
        transaction = bundle.transactions[0]
        print('------------------------------')
        print('Hash: ' + str(transaction.hash))
        print('Address: ' + str(transaction.address))
        print('Value: ' + str(transaction.value))
        print('Message: ' + str(transaction.signature_message_fragment.
                                decode()))
        print('Message size ' + str(len(TryteString.from_unicode(transaction.
                                        signature_message_fragment.decode())))
              + ' trytes  (max 2187 trytes)')
        print('Tag: ' + str(transaction.tag))
        print('Nonce: ' + str(transaction.nonce))
        print('Branch hash: ' + str(transaction.branch_transaction_hash))
        print('Trunk hash: ' + str(transaction.trunk_transaction_hash))
        print('Timestamp: ' + str(datetime.utcfromtimestamp(transaction.
                                  timestamp).strftime('%Y-%m-%d %H:%M:%S')))
        print('Upload time: ' + str(round(timer, 2)) + ' seconds')


def print_bundle_result(result, timer, tx_num=1):
    for bundle in result.values():
        for transaction in bundle.transactions:
            i = transaction.current_index + tx_num
            print('------------------------------')
            print(f'    Tx{i} hash: ' + str(transaction.hash))
            print(f'    Tx{i} address: ' + str(transaction.address))
            print(f'    Tx{i} value: ' + str(transaction.value))
            print(f'    Tx{i} message: ' + str(transaction.
                  signature_message_fragment.decode()))
            print(f'    Tx{i} message size: ' + str(len(TryteString.
                  from_unicode(transaction.signature_message_fragment.decode()
                               ))) + ' trytes  (max 2187 trytes)')
            print(f'    Tx{i} tag: ' + str(transaction.tag))
            print(f'    Tx{i} nonce: ' + str(transaction.nonce))
            print(f'    Tx{i} branch hash: ' + str(transaction.
                                                   branch_transaction_hash))
            print(f'    Tx{i} trunk hash: ' + str(transaction.
                                                  trunk_transaction_hash))
            print(f'    Tx{i} timestamp: ' + str(datetime.utcfromtimestamp(
                  transaction.timestamp).strftime('%Y-%m-%d %H:%M:%S')))
        print('------------------------------')
        print('Bundle hash: ' + str(bundle.hash))
        print('Bundle confirmation: ' + str(bundle.is_confirmed))
        print('Bundle upload time: ' + str(round(timer, 2)) + ' seconds  (' +
              str(round(timer/len(bundle.transactions), 2)) + ' sec/tx)')


def print_bundle_tail_result(result, timer, tx_num=1):
    for bundle in result.values():
        for transaction in bundle.transactions[1:]:
            i = transaction.current_index + tx_num
            print('--------------------')
            print(f'    Tx{i} hash: ' + str(transaction.hash))
            print(f'    Tx{i} address: ' + str(transaction.address))
            print(f'    Tx{i} value: ' + str(transaction.value))
            print(f'    Tx{i} message: ' + str(transaction.
                  signature_message_fragment.decode()))
            print(f'    Tx{i} message size: ' + str(len(TryteString.
                  from_unicode(transaction.signature_message_fragment.decode()
                               ))) + ' trytes  (max 2187 trytes)')
            print(f'    Tx{i} tag: ' + str(transaction.tag))
            print(f'    Tx{i} nonce: ' + str(transaction.nonce))
            print(f'    Tx{i} branch hash: ' + str(transaction.
                                                   branch_transaction_hash))
            print(f'    Tx{i} trunk hash: ' + str(transaction.
                                                  trunk_transaction_hash))
            print(f'    Tx{i} timestamp: ' + str(
                datetime.utcfromtimestamp(transaction.timestamp).
                strftime('%Y-%m-%d %H:%M:%S')))
        print('--------------------')
        print('Tail Tx hash: ' + str(bundle.tail_transaction.hash))
        print('Tail Tx address: ' + str(bundle.tail_transaction.address))
        print('Tail Tx value: ' + str(bundle.tail_transaction.value))
        print('Tail Tx message: ' + str(bundle.tail_transaction.
                                        signature_message_fragment.decode()))
        print('Tail Tx message size: ' + str(len(TryteString.from_unicode(
              bundle.tail_transaction.signature_message_fragment.decode()))) +
              ' trytes  (max 2187 trytes)')
        print('Tail Tx tag: ' + str(bundle.tail_transaction.tag))
        print('Tail Tx nonce: ' + str(bundle.tail_transaction.nonce))
        print('Tail Tx branch hash: ' + str(bundle.tail_transaction.
                                            branch_transaction_hash))
        print('Tail Tx trunk hash: ' + str(bundle.tail_transaction.
                                           runk_transaction_hash))
        print('Tail Tx timestamp: ' + str(datetime.utcfromtimestamp(
             bundle.tail_transaction.timestamp).strftime('%Y-%m-%d %H:%M:%S')))
        print('--------------------')
        print('Bundle hash: ' + str(bundle.hash))
        print('Bundle confirmation: ' + str(bundle.is_confirmed))
        print('Bundle upload time: ' + str(round(timer, 2)) + ' seconds  (' +
              str(round(timer/len(bundle.transactions), 2)) + ' sec/tx)')
