from pygame import *
from random import randint

lose1 = False
lose2 = False

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, pos_x, pos_y, speed,size_x,size_y):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(p_image), (self.size_x,self.size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_ws(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 410:
            self.rect.y += self.speed
    def update_arrows(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 410:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self,p_image, pos_x, pos_y, speed,size_x,size_y):
        super().__init__(p_image, pos_x, pos_y, speed,size_x,size_y)
        self.speed_x = speed
        self.speed_y = speed
    def update(self):
        if self.rect.y < 5 or self.rect.y > 478:
            self.speed_y *= -1
        if self.rect.x < -17:
            global lose1
            lose1 = True
        if self.rect.x > 700:
            global lose2
            lose2 = True
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if sprite.collide_rect(player1, ball):
            self.speed_x *= -1
        if sprite.collide_rect(player2, ball):
            self.speed_x *= -1


window = display.set_mode((700, 500))
display.set_caption('Ping-pong')
background = transform.scale(image.load('C:\\Users\\Инесса\\Desktop\\пингпонг\\fon.jpg'),(700,500))

game = True
final = False
clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont('Arial',35)
font2 = font.SysFont('Arial',20)
t_lose1 = font1.render('Первый игрок проиграл!',True, (180,0,0))
t_lose2 = font1.render('Второй игрок проиграл!',True, (180,0,0))

player1 = Player('C:\\Users\\Инесса\\Desktop\\пингпонг\\raketka.jpg', 5,10, 6, 10, 80)
player2 = Player('C:\\Users\\Инесса\\Desktop\\пингпонг\\raketka.jpg', 680,10, 6, 10, 80)
ball = Ball('C:\\Users\\Инесса\\Desktop\\пингпонг\\ball.jpg',randint(30,200),randint(0,450),6,17,17)

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
                           
    if final != True:
        window.blit(background,(0, 0))
        player1.update_ws()
        player1.reset()
        player2.update_arrows()
        player2.reset()
        ball.update()
        ball.reset()

        if lose1 == True:
            final = True
            window.blit(t_lose1,(200, 200))
        if lose2 == True:
            final = True
            window.blit(t_lose2,(200, 200))
    display.update()
    clock.tick(FPS)

