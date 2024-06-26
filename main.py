import binascii
import nfc
import time
from playsound import playsound


def on_connected(user_id: str):
    print(user_id)
    # 音を鳴らす
    playsound('purchase.mp3')


def on_connect_nfc(tag):
    # タグのIDなどを出力する
    # print tag
    # 学生証のサービスコード
    service_code = 0x300B
    if isinstance(tag, nfc.tag.tt3.Type3Tag):
        try:
            sc = nfc.tag.tt3.ServiceCode(service_code >> 6, service_code & 0x3f)
            bc = nfc.tag.tt3.BlockCode(0, service=0)
            data = tag.read_without_encryption([sc], [bc])
            user_id = data[4:11].decode('utf-8')
            on_connected(user_id)

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
