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















#from pygame import *
#from random import randint
#import time as ttime 
#
#lost = 0
#score = 0
#ammo = 0
#global reload_b
#reload_b = False
#
#
#class GameSprite(sprite.Sprite):
#    def __init__(self, p_image, pos_x, pos_y, speed,size_x,size_y):
#        super().__init__()
#        self.size_x = size_x
#        self.size_y = size_y
#        self.image = transform.scale(image.load(p_image), (self.size_x,self.size_y))
#        self.speed = speed
#        self.rect = self.image.get_rect()
#        self.rect.x = pos_x
#        self.rect.y = pos_y
#    def reset(self):
#        window.blit(self.image, (self.rect.x, self.rect.y))
#
#class Player(GameSprite):
#    def update(self):
#        keys_pressed = key.get_pressed()
#        if keys_pressed[K_LEFT] and self.rect.x > 5:
#            self.rect.x -= self.speed
#        if keys_pressed[K_RIGHT] and self.rect.x < 630:
#            self.rect.x += self.speed
#    def fire(self):
#        bullet = Bullet('bullet.png', self.rect.centerx-6, self.rect.top, 15,15,20)
#        bullets.add(bullet)
#
#class Enemy(GameSprite):
#    def update(self):
#        self.rect.y += self.speed
#        global lost
#        if self.rect.y > 500:
#            self.rect.x = randint(30,630)
#            self.rect.y = -60
#            self.speed = randint(1,2)
#            lost += 1
#
#class Asteroid(GameSprite):
#    def update(self):
#        self.rect.y += self.speed
#        if self.rect.y > 500:
#            self.rect.x = randint(30,630)
#            self.rect.y = -60
#            self.speed = randint(1,1)
#
#class Bullet(GameSprite):
#    def update(self):
#        self.rect.y -= self.speed
#        if self.rect.y < 0:
#            self.kill()
#
#window = display.set_mode((700, 500))
#display.set_caption('Шутер')
#background = transform.scale(image.load("galaxy.jpg"),(700,500))
#
#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
#fire = mixer.Sound('fire.ogg')
#
#player = Player('rocket.png', randint(5,630), 420, 6,65,65)
#
#vragi = sprite.Group()
#for i in range (0,5):
#    vrag = Enemy('ufo.png', randint(30, 600),randint(-100,-40), randint(1,3),65,65)
#    vragi.add(vrag)
#    
#asteroids = sprite.Group()
#for i in range (0,3):
#    asteroid = Asteroid('asteroid.png', randint(30, 600),randint(-100,-40), randint(1,3),65,65)
#    asteroids.add(asteroid )
#bullets = sprite.Group()
#
#game = True
#final = False
#clock = time.Clock()
#FPS = 60
#
#font.init()
#font1 = font.SysFont('Arial',70)
#win = font1.render('Выигрыш!',True, (255,215,0))
#lose = font1.render('Проигрыш!',True, (180,0,0))
#font2 = font.SysFont('Arial',20)
#font3 = font.SysFont('Arial',40)
#while game:
#    for i in event.get():
#        if i.type == QUIT:
#            game = False
#        elif i.type == KEYDOWN:
#            if i.key == K_SPACE:
#                
#                if reload_b == False:
#                    player.fire()
#                    fire.play()
#                    ammo += 1
#                
#                
#                    
#    if final != True:
#        window.blit(background,(0, 0))
#
#        time2 = ttime.time()
#        if ammo == 5:
#            reload_b = True
#            time1 = ttime.time()
#            ammo = 0
#        if reload_b == True and time2 - time1 >= 2:
#            reload_b = False
#
#        if reload_b == True:
#            text_reload = font3.render('Перезарядка!',True, (180,0,0))
#            window.blit(text_reload,(230, 450))
#        else:
#            text_reload = font3.render('Перезарядка!',True, (180,0,0))
#            window.blit(text_reload,(700, 450))
#
#
#        if sprite.spritecollide(player, vragi, False):
#            window.blit(lose,(200, 250))
#            final = True
#
#        if sprite.spritecollide(player, asteroids, False):
#            window.blit(lose,(200, 250))
#            final = True
#
#        if sprite.groupcollide(bullets, vragi, True, True):
#            vrag = Enemy('ufo.png', randint(30, 600),randint(-180,-40), randint(1,3),65,65)
#            vragi.add(vrag)
#            score += 1
#            text_s = font2.render('Счёт: '+ str(score), 1, (255,255,255))
#            window.blit(text_s,(10, 10))
#            if score >= 10:
#                final = True
#                window.blit(win,(200, 250))
#
#        if lost >= 3:
#            final = True
#            window.blit(lose,(200, 250))
#
#        text_l = font2.render('Пропущено: '+ str(lost), 1, (255,255,255))
#        window.blit(text_l,(10, 30))
#        text_s = font2.render('Счёт: '+ str(score), 1, (255,255,255))
#        window.blit(text_s,(10, 10))
#
#        player.reset()
#        player.update()
#        vragi.update()
#        vragi.draw(window)
#        asteroids.update()
#        asteroids.draw(window)
#        bullets.update()
#        bullets.draw(window)
#
#
#    display.update()
#    clock.tick(FPS)