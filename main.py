#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii
import nfc
import time

# 学生証のサービスコード
service_code = 0x300B


def on_connect_nfc(tag):
    # タグのIDなどを出力する
    # print tag

    if isinstance(tag, nfc.tag.tt3.Type3Tag):
        try:
            sc = nfc.tag.tt3.ServiceCode(service_code >> 6, service_code & 0x3f)
            bc = nfc.tag.tt3.BlockCode(0, service=0)
            data = tag.read_without_encryption([sc], [bc])
            sid = "s" + str(data[4:11])
            print(sid)
        except Exception as e:
            print(f"error: {e}")
    else:
        print("error: tag isn't Type3Tag")


def main():
    clf = nfc.ContactlessFrontend('usb')
    while True:
        clf.connect(rdwr={'on-connect': on_connect_nfc})
        time.sleep(3)


if __name__ == "__main__":
    main()
