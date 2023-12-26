import cv2
import numpy as np

demo = cv2.imread("C:/Users/User/Downloads/download.jpg", 0)
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)
cv2.imwrite("C:/Users/User/Downloads/KEY-download.jpg", key)

cv2.imshow("demo", demo)
cv2.imshow("key", key)

encryption = cv2.bitwise_xor(demo, key)
cv2.imwrite("C:/Users/User/Downloads/ENC-download.jpg", encryption)
decryption = cv2.bitwise_xor(encryption, key)
cv2.imwrite("C:/Users/User/Downloads/DES-download.jpg", decryption)

cv2.imshow("encryption", encryption)
cv2.imshow("decryption", decryption)

cv2.waitKey(-1)
cv2.destroyAllWindows()