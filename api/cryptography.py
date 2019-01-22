# coding=utf-8

from iota import TryteString, Address
import sha3


def convert(data, salt):
    OUTPUT_SIZE = 80   # Number of characters to fit IOTA address
    hash_shake = sha3.shake_128()
    if salt is None:
        hash_shake.update(data.encode())
    else:
        hash_shake.update(data.encode() + salt.encode())
    msg_trytes = TryteString.from_unicode(hash_shake.hexdigest(
                     int(OUTPUT_SIZE/4))) + TryteString(b'9')
    return Address(msg_trytes)
