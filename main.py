from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, scale_player_x, scale_player_y):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (scale_player_x, scale_player_y)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[k_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[k_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 
    def update_l(self):
        keys = key.get_pressed()
        if keys[k_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[k_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 

racket1 = Player('racket.png', 30, 200, 4, 50,150)
recket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = Player('ball.png', 200, 300, 4, 50,50)


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
    
    if finish != True:
        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)
