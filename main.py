import argparse
import schedule
import time

from dns_updater.dns_update import update

SCRIPT = 0
SERVICE = 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", type=int, default=SERVICE)

    args = parser.parse_args()
    mode = args.mode

    if mode == SCRIPT:
        print("running dns update...")
        update()
    elif mode == SERVICE:
        print("starting dns updater service...")
        schedule.every().hour.at(":00").do(update)

        while True:
            schedule.run_pending()
            time.sleep(60)

