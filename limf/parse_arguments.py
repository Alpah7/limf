#!/bin/env python
import argparse
import random
from .decrypter import decrypt_files
from .encrypter import encrypt_files
from .uploader import upload_files
def parse_arguments(args, clone_list):
    """
    Makes parsing arguments a function.
    """
    host_number = args.host
    if args.decrypt:
        for i in args.files:
            print(decrypt_files(i))
            exit()
    for i in args.files:
        if host_number == None or args.host != host_number:
            host_number = random.randrange(0, len(clone_list))
        while True:
            try:
                if args.encrypt:
                    print(encrypt_files(clone_list[host_number], args.only_link, i))
                else:
                    print(upload_files(open(i, 'rb'), \
                          clone_list[host_number], args.only_link, i))
            except IndexError:
                #print('Selected server (' + clone_list[host_number][0] + ') is offline.')
                #print('Trying other host.')
                host_number = random.randrange(0, len(clone_list))
                continue
            break
