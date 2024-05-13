from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 490:
            self.rect.y += self.speed            
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 490:
            self.rect.y += self.speed   



back = (20,10,30)
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60

game = True
finish = False

font.init()
font = font.SysFont('Arial', 40)
lose1 = font.render('Player 1 lose!', True, (255, 255, 255))
lose2 = font.render('Player 2 lose!', True, (255, 255, 255))

raket1 = Player('pngtree-modren-ball-icon-vector-png-image_5048397.jpg', 10,10,10,30,60)
raket2 = Player('pngtree-modren-ball-icon-vector-png-image_5048397.jpg', 450,10,10,30,60)
ball = GameSprite('png-transparent-blue-and-gray-tennis-racket-illustration-racket-squash-tennis-head-squash-tennis-tennis-racket-blue-happy-birthday-vector-images-sports-equipment.png', 200,200,10,30,30)

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball) :
        speed_x = speed_x * -1

    raket1.update_l()
    raket2.update_r()
    raket1.reset()
    raket2.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)

