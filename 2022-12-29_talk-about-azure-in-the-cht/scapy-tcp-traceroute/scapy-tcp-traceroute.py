#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import csv
import logging
import ipaddress
from scapy.layers.inet import traceroute

OKCYAN = "\033[96m"
WARNING = "\033[93m"
FAIL = "\033[91m"
ENDC = "\033[0m"

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def log_ok(msg):
    print(OKCYAN + msg + ENDC)


def log_warning(msg):
    print(WARNING + msg + ENDC)


def log_error(msg):
    print(FAIL + msg + ENDC)


def is_application_rule(dport: int) -> bool:
    return dport == 80 or dport == 443


def tcp_traceroute(dst, dport=443):
    max_ttl=30
    got_sa = False
    try:
        res, unans = traceroute(dst, dport=dport, maxttl=max_ttl, verbose=False)
    except Exception as e:
        log_error("{} with {}:{}".format(e, dst, dport))
        return
    last_packet = res.res[-1]
    last_packet_query = last_packet.query
    last_packet_answer = last_packet.answer
    last_packet_answer_payload = last_packet_answer.payload
    if last_packet_answer_payload.name == "TCP":
        tcp_flags = last_packet_answer_payload.flags
        if tcp_flags == "SA":
            got_sa = True

    query_dst = last_packet_query.dst
    answer_src = last_packet_answer.src
    if got_sa:
        if query_dst != answer_src:
            log_warning("[-] Invalid TCP connection with {}, Query {} -> Answer {}".format(dst, query_dst, answer_src))
        else:
            if len(res.res) <= 5 and is_application_rule(dport):
                penultimate_package = res.res[-2]
                penultimate_package_answer_src = penultimate_package.answer.src
                if ipaddress.ip_interface(penultimate_package_answer_src).is_private:
                    log_warning(
                        "[-] Possible problem with TCP connection to {}:{}, "
                        "the penultimate package answer src: {}".format(dst, dport, penultimate_package_answer_src))
                    return
            if len(res.res) == max_ttl:
                for idx in range(1, max_ttl):
                    previous_package = res.res[idx -1]
                    current_package = res.res[idx]
                    if previous_package.answer.src == current_package.answer.src:
                        real_penultimate_package = res.res[idx - 2]
                        penultimate_package_answer_src = real_penultimate_package.answer.src
                        if ipaddress.ip_interface(penultimate_package_answer_src).is_private:
                            log_warning(
                                "[-] Possible problem with TCP connection to {}:{}, "
                                "the penultimate package answer src: {}".format(dst, dport, penultimate_package_answer_src))
                            return

            display_dst = "{}:{}".format(dst, dport)
            if dst != query_dst:
                display_dst += " ({})".format(query_dst)
            log_ok("[+] TCP connection established with {}, total hops: {}".format(display_dst, len(res.res)))
    else:
        log_error("[-] TCP connection failed with {}:{}, the last packet answer src: {}".format(dst, dport, answer_src))


def main(csv_file):
    with open(csv_file, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            tcp_traceroute(row["host"], int(row["port"]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP traceroute")
    parser.add_argument("-f", "--file", help="Destination CSV file with host and port", required=True)
    args = parser.parse_args()
    if args.file:
        main(args.file)
