import pgzrun
from random import randint
TITLE = "flappy Ball"
WIDTH = 800
HEIGHT = 800
R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
COLOR = R,G,B
game_over = False
Gravity = 2000.0

class Ball:
    def __init__(self,initial_x,initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40
    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,COLOR)
ball = [Ball(50,100), Ball(200,150), Ball(350,200)]
def update(dt):
    uy = ball.vy
    ball.vy = Gravity * dt
    ball.y = (ball.y + ball.vy) * 0.5 * dt
    if ball.y > HEIGHT - ball.radius:
        ball.y = HEIGHT - ball.radius
        ball.vy = ball.vy * 0.9
pgzrun.go()