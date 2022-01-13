import argparse

from src.SocketSender import SocketSender
from src.config import *

parser = argparse.ArgumentParser(description='Autonomous Military Vehicle CLI.')
parser.add_argument('--wireless', action="store_true", help="uses wireless connection instead of wired")
group = parser.add_mutually_exclusive_group()
group.add_argument('--live', action="store_true", help='start live command processing')
group.add_argument('--msg', type=str, help='send a message to the tank control board')

args = parser.parse_args()

if __name__ == "__main__":
    socket_sender = SocketSender(WIRELESS_IP, WIRELESS_PORT) if args.wireless else SocketSender(UDP_IP, UDP_PORT)
    if args.live:
        while True:
            command = str(input())
            if command.lower() in ["stop", "q"]:
                print("Process terminated successfully!")
                break
            else:
                socket_sender.send_message(command)
    elif args.msg:
        socket_sender.send_message(args.msg)
    else:
        parser.print_help()

