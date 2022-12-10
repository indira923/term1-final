from sense_hat import SenseHat
from time import sleep
sense = SenseHat()



r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)

snow =  [k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, w, k, k, k, k, k,
         k, w, w, w, k, k, k, k,
         k, k, w, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, w, w, w, k, k, k,
         w, w, w, w, w, w, w, w
]

sense.set_pixels(snow)
# sense.set_pixel(0,4,255,255,255)
# sense.set_pixel(2,4,255,255,255)
# sense.set_pixel(4,4,255,255,255)