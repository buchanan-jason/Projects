#!/usr/bin/env python3

"""
Python script to gather ip address and hostname.

inputs: none
outputs: prints text to terminal
"""

import socket


def get_hostname():
    hostname = socket.getfqdn()
    return hostname


def get_ip_address(hostname):
    ip = socket.gethostbyname(hostname)
    return ip


def main():
    machine_hostname = get_hostname()
    print(machine_hostname)
    machine_ip = get_ip_address(machine_hostname)
    print(machine_ip)


if __name__ == '__main__':
    main()