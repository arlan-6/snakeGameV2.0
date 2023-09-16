from colorPick import ColorPicker
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 480))
pg.display.set_caption("Color Picker")

picker = ColorPicker(screen)
picker.run()
pg.quit()
sys.exit()