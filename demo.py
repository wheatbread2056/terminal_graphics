from getkey import getkey, keys
import terminal_graphics as tgrap, os

xs, ys, xe, ye = 0, 0, 1, 0
x_size, y_size = 2, 1
width, height = 50, 25

tgrap.gen_screen(width, height)
tgrap.rect(xs, ys, xe, ye, 2)

while True:
  os.system("clear")
  tgrap.gen_screen(50, 25)
  tgrap.rect(xs + x_size, ys + y_size, xe + x_size, ye + y_size, 2)
  tgrap.draw()

  print("Coin Collector - Terminal Game")
  print(f"X: {(xe + x_size) - 1}, Y: {ys + y_size}")

  key_press = getkey()

  if key_press == keys.UP:
    if ys == -1:
      pass
    else:
      ys -= y_size
      ye -= y_size
  elif key_press == keys.DOWN:
    if ye == 23:
      pass
    else:
      ys += y_size
      ye += y_size
  elif key_press == keys.LEFT:
    if xs == -2:
      pass
    else:
      xs -= x_size
      xe -= x_size
  elif key_press == keys.RIGHT:
    if xs == 46:
      pass
    else:
      xs += x_size
      xe += x_size