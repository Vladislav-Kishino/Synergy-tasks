# 🌲 🌊 🚁 🟩 🔥 🏥 💛 💧 🏪 ☁️ ⚡ 🏆 ⬛

from map import Map
import time
import os

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.generate_forest(1, 10)
field.generate_river(15)
field.generate_river(10)
field.print_map()

tick = 1

while True:
   os.system("cls") # "clear" for unix
   print("TICK", tick)
   field.print_map()
   tick += 1
   time.sleep(TICK_SLEEP)
   if (tick % TREE_UPDATE == 0):
      field.generate_tree()
   if (tick % FIRE_UPDATE == 0):
      field.update_fires()