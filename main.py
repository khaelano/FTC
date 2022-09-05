import pygame as pg
import sys

def main():
    WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 800

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (200, 200, 200)
    GREEN = (200,255,200)
    RED = (255, 150, 150)
    BLUE = (200, 200, 255)

    window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption('Fucking Terraria Clone')
    clock = pg.time.Clock()

    run = True
    while run:
        clock.tick(60)
        window.fill(BLUE)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
if __name__ == '__main__':
    main()