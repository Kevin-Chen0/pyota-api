# coding=utf-8

from iota import TryteString, ProposedTransaction, Tag


def tx_to_tangle(api, address_in, data_in, tag_in='', value_in=0):
    result = api.send_transfer(transfers=[
        ProposedTransaction(
            address=address_in,
            message=TryteString.from_unicode(data_in),
            tag=Tag(tag_in.encode()),
            value=value_in
        )
    ])
    return result


def bundle_to_tangle(api, address_in, dframe_in, tag_in=''):
    transfer_txs = []
    for index, row in dframe_in.iterrows():
        transfer_txs.append(
            ProposedTransaction(
                address=address_in,
                message=TryteString.from_unicode(row.to_json()),
                tag=Tag(tag_in.encode()),
                value=0
            )
        )
    result = api.send_transfer(transfers=transfer_txs)
    return result
