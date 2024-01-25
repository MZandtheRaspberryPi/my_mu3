import time

import cv2

from my_mu3.mu3_image_grabber import Mu3ImageGrabber

IP_ADDRESS = "192.168.1.183"

def main():

    my_mu3 = Mu3ImageGrabber(ip_address=IP_ADDRESS)

    exit_flag = False
    my_mu3.start()

    while not exit_flag:

        image = my_mu3.get_image()
        if image is not None:
            cv2.imshow('mu3 camera', image)

        if cv2.waitKey(1) == ord("q"):
            exit_flag = True
        time.sleep(0.01)

    my_mu3.stop()

if __name__ == "__main__":
    main()