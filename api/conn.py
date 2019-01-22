# coding=utf-8

from iota import Iota
import requests
import sys


'''
Please check for updates nodes: https://iota.dance/
Ensure that the nodes beginning in the list are not offline
'''
iota_node_ip_1 = 'https://iotanode.us:443'
iota_node_ip_2 = 'https://turnip.iotasalad.org:14265'
iota_node_ip_3 = 'https://peanut.iotasalad.org:14265'
iota_node_ip_4 = 'https://potato.iotasalad.org:14265'
iota_node_ip_5 = 'https://tuna.iotasalad.org:14265'
iota_node_ip_6 = 'https://durian.iotasalad.org:14265'
iota_node_ip_7 = 'https://pow1.iota.community:443'
iota_node_ip_8 = 'https://pow2.iota.community:443'
iota_node_ip_9 = 'https://pow3.iota.community:443'
iota_node_ip_10 = 'https://pow4.iota.community:443'
iota_node_ip_11 = 'https://pow5.iota.community:443'
iota_node_ip_12 = 'https://pow6.iota.community:443'
iota_node_ip_13 = 'https://nodes.thetangle.org:443'
iota_node_ip_14 = 'https://pool.iota.dance:443'
iota_node_ip_15 = 'https://nodes.iota.cafe:443'
iota_node_ip_16 = 'https://wallet1.iota.town:443'
iota_node_ip_17 = 'https://wallet2.iota.town:443'
iota_node_ip_18 = 'https://pool.trytes.eu'
iota_node_ip_19 = 'https://nutzdoch.einfachiota.de'
iota_node_ip_20 = 'https://trinity.iota-tangle.io:14265'
iota_node_ip_21 = 'https://iota-1.de:14267'
iota_node_ip_22 = 'https://iota-2.de:14267'
iota_node_ip_23 = 'https://iota-3.de:14267'

iota_node_list = [
    iota_node_ip_1,
    iota_node_ip_2,
    iota_node_ip_3,
    iota_node_ip_4,
    iota_node_ip_5,
    iota_node_ip_6,
    iota_node_ip_7,
    iota_node_ip_8,
    iota_node_ip_9,
    iota_node_ip_10,
    iota_node_ip_11,
    iota_node_ip_12,
    iota_node_ip_13,
    iota_node_ip_14,
    iota_node_ip_15,
    iota_node_ip_16,
    iota_node_ip_17,
    iota_node_ip_18,
    iota_node_ip_19,
    iota_node_ip_20,
    iota_node_ip_21,
    iota_node_ip_22,
    iota_node_ip_23
]


def is_connected(api):
    try:
        api.get_node_info()
    except requests.exceptions.ConnectionError:
        print("It appears that the given IOTA full-node is unresponsive."
              "Please change node and try again.")
        sys.exit(1)
    else:
        return True


def get_active_full_nodes(seed, limit=1):
    active_nodes = []
    for ip in iota_node_list:
        if is_connected(Iota(ip, seed)):
            active_nodes.append(ip)
            print("Established connection to following IOTA full-node: "
                  f"'{ip}'")
        if len(active_nodes) == limit:
            break
    return active_nodes
