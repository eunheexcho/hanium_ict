import cv2
import imagezmq
import time

image_hub = imagezmq.ImageHub()

while True:
    rpi_name, image = image_hub.recv_image()

    cv2.imshow("Strip", image)
    if cv2.waitKey(1) == ord('q'):
        break

    image_hub.send_reply(b'OK')
    cv2.imwrite('test.jpg', image)