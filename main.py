from pygame import *
back = (100,20,190)
win_height = 500
win_width = 600
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    

    display.update()
    clock.tick(FPS)