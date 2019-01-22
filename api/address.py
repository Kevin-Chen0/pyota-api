# coding=utf-8

from iota.crypto.addresses import AddressGenerator
from random import SystemRandom


def generate_seed():
    alphabet = u'9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    generator = SystemRandom()
    seed = ''.join(generator.choice(alphabet) for _ in range(81))
    return seed


def generate_address(seed=generate_seed(), security=1):
    generator = AddressGenerator(seed, security_level=security)
    address = generator.get_addresses(start=0)[0]
    return address
