import argparse
import datetime
import os
import time

import cv2
from dotenv import load_dotenv
import requests


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

def capture():
    vc = cv2.VideoCapture(1)
    # warm up webcam
    time.sleep(5)
    _, frame = vc.read()
    vc.release()
    return frame


def upload2discord(image_path):
    files = {'file': open(image_path, 'rb')}

    r = requests.post(
        url=DISCORD_WEBHOOK_URL,
        files=files,
        headers={'content_type': 'multipart/form-data'}
    )


def parse_args(args=None):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--interval', default=60, help='Capturing interval (min.)')

    if args is None:
        return parser.parse_args()
    else:
        return parser.parse_args(args)


def main(args=None):
    if args is None:
        args = parse_args()
    dir = 'captures'
    os.makedirs(dir, exist_ok=True)

    while True:
        frame = capture()
        now = datetime.datetime.now()
        datestr = now.strftime('%Y%m%d-%H:%M:%S')
        fname = f"{dir}/{datestr}.jpg"
        cv2.imwrite(fname, frame)
        upload2discord(fname)

        time.sleep(args.interval*60)


if __name__ == '__main__':
    main()