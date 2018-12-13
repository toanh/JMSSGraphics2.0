from JMSSGraphics import *

from random import *
import math
import colorsys

class Entity:
    def __init__(self, filename):
        if isinstance(filename, str):
            self.image = jmss.loadImage(filename)
        else:
            self.image = filename
        self.x = 0
        self.y = 0
        self.xdir = 0
        self.ydir = 0
        self.width = self.image.width
        self.height = self.image.height
        self.opacity = None

    def Draw(self):
        jmss.drawImage(self.image, self.x, self.y, opacity=self.opacity)

    def Update(self):
        self.x += self.xdir
        self.y += self.ydir


class Paddle(Entity):
    def __init__(self, filename, gunfilename, upKey, downKey, fireKey, lives, fireDir):
        super().__init__(filename)
        self.up = upKey
        self.down = downKey
        self.fire = fireKey
        self.lives = lives
        self.fireDir = fireDir
        self.coolDown = 40
        self.timer = 0
        self.gun = jmss.loadImage(gunfilename)

    def Draw(self):
        super().Draw()
        if (self.fireDir > 0):
            jmss.drawImage(self.gun, self.x, self.y + self.image.height / 2 - self.gun.height / 2)
        else:
            jmss.drawImage(self.gun, self.x - self.gun.width / 2, self.y + self.image.height / 2 - self.gun.height / 2)

    def Update(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 0
        self.ydir *= 0.9
        if jmss.isKeyDown(self.up):
            self.ydir += 0.5
            if self.ydir >= 3:
                self.ydir = 3
        if jmss.isKeyDown(self.down):
            self.ydir -= 0.5
            if self.ydir <= -3:
                self.ydir = -3
        if jmss.isKeyDown(self.fire) and self.timer == 0:
            self.timer = self.coolDown
            if (self.fireDir > 0):
                game.SpawnBullet(self.x + self.gun.width / 2, self.y + self.height / 2, self.fireDir * 10, self)
            else:
                game.SpawnBullet(self.x - self.gun.width / 2, self.y + self.height / 2, self.fireDir * 10, self)

        super().Update()


class Ball(Entity):
    def __init__(self, filename, respawnable=True):
        super().__init__(filename)
        self.respawnable = respawnable
        self.opacity = 0.5

    def Update(self):
        self.opacity += 0.01
        if self.opacity >= 1.0:
            self.opacity = 1.0

        if abs(self.xdir) >= 5:
            self.xdir = self.xdir / abs(self.xdir) * 5
        super().Update()


class Bullet(Entity):
    def __init__(self, filename, owner):
        self.owner = owner
        super().__init__(filename)


class Game:
    def SpawnBall(self, x, y, xdir=None, ydir=None, filename="ball.png", respawnable=True):
        ball = Ball(filename, respawnable)
        ball.x = x
        ball.y = y
        if xdir is None:
            ball.xdir = (random() - 0.5) * 2
            if ball.xdir < 0:
                ball.xdir -= 2
            else:
                ball.xdir += 2
        else:
            ball.xdir = xdir
        if ydir is None:
            ball.ydir = (random() - 0.5) * 2
            if ball.ydir < 0:
                ball.ydir -= 2
            else:
                ball.ydir += 2
        else:
            ball.ydir = ydir
        self.balls.append(ball)

        # background 3D animation


    def drawTriangleList(self, triList):
        colour = colorsys.hsv_to_rgb(self.angle/2, 0.6, 0.6)
        # turtle.pencolor(colour)
        for i in range(0, len(triList), 3):
            jmss.drawLine(triList[i][0], triList[i][1], triList[i + 1][0], triList[i + 1][1], r = colour[0], g = colour[1], b = colour[2])
            jmss.drawLine(triList[i + 1][0], triList[i + 1][1], triList[i + 2][0], triList[i + 2][1], r = colour[0], g = colour[1], b = colour[2])
            jmss.drawLine(triList[i + 2][0], triList[i + 2][1], triList[i][0], triList[i][1], r = colour[0], g = colour[1], b = colour[2])

    def rotateTransform(self, triList3D, angle):
        transformedList = []
        for vertex in triList3D:
            x = vertex[0] * math.cos(angle) - vertex[2] * math.sin(angle)
            y = vertex[1]
            z = vertex[0] * math.sin(angle) + vertex[2] * math.cos(angle)

            newTri = (x, y, z)
            transformedList.append(newTri)
        return transformedList

    def translateTransform(self, triList3D, cameraPos):
        transformedList = []
        for i in range(len(triList3D)):
            newTri = (triList3D[i][0] - cameraPos[0], triList3D[i][1] - cameraPos[1], triList3D[i][2] - cameraPos[2])
            transformedList.append(newTri)
        return transformedList

    def perspectiveTransform(self, triList3D):
        triList2D = [];
        for i in range(0, len(triList3D)):
            newTri = (triList3D[i][0] / triList3D[i][2], triList3D[i][1] / triList3D[i][2])
            triList2D.append(newTri)
        return triList2D

    def viewportTransform(self, triList2D, width, height):
        transformedList = []
        for vertex in triList2D:
            x = (vertex[0] + 0.6)* width
            y = (vertex[1] + 0.5)* height
            newTri = (x, y)
            transformedList.append(newTri)
        return transformedList

    def SpawnBullet(self, x, y, xdir, owner):
        if owner == self.p1:
            bullet = Bullet(self.bullet_red_image, owner)
        else:
            bullet = Bullet(self.bullet_blue_image, owner)
        bullet.x = x
        bullet.y = y - bullet.image.height / 2
        bullet.xdir = xdir
        bullet.ydir = 0
        self.bullets.append(bullet)

    def ResetGame(self):
        self.balls = []
        self.bullets = []

        self.p1.xdir = 0
        self.p1.ydir = 0
        self.p1.x = 0
        self.p1.y = 100
        self.p1.lives = 3

        self.p2.xdir = 0
        self.p2.ydir = 0
        self.p2.x = 600 - 24
        self.p2.y = 100
        self.p2.lives = 3

        self.SpawnBall(300, 200, filename = self.ball_green_image)

    def __init__(self):
        self.balls = []
        self.bullets = []

        paddle1 = Paddle("paddle_red.png", "gun_left.png", KEY_W, KEY_S, KEY_D, 3, 1)
        paddle1.xdir = 0
        paddle1.ydir = 0
        paddle1.x = 0
        paddle1.y = 100
        self.p1 = paddle1

        paddle2 = Paddle("paddle_blue.png", "gun_right.png", KEY_UP, KEY_DOWN, KEY_LEFT, 3, -1)
        paddle2.xdir = 0
        paddle2.ydir = 0
        paddle2.x = 600 - 24
        paddle2.y = 100
        self.p2 = paddle2

        self.angle = 0
        self.camera = [0, 1.7, -8]

        self.shape = [
            [0, 1, 0], [-1, -1, -1], [1, -1, -1],
            [0, 1, 0], [1, -1, -1], [1, -1, 1],
            [0, 1, 0], [1, -1, 1], [-1, -1, 1],
            [0, 1, 0], [-1, -1, -1], [-1, -1, 1]]
        self.triList = []

        self.gameState = 0

        self.title_image = jmss.loadImage("title.png")
        self.bg_image = jmss.loadImage("background.png")
        self.bg_x = 0

        # pre-load our sound files
        self.blip_sound = jmss.loadSound("blip.wav", streaming=False)
        self.background_music = jmss.loadSound("piano.wav", streaming=True)

        self.bullet_red_image = jmss.loadImage("bullet_red.png")
        self.bullet_blue_image = jmss.loadImage("bullet_blue.png")
        self.ball_red_image = jmss.loadImage("ball_red.png")
        self.ball_green_image = jmss.loadImage("ball.png")

        self.SpawnBall(300, 200, filename = self.ball_green_image)

        jmss.playSound(self.background_music)

    def Draw(self):
        if self.gameState == 0:
            self.DrawTitle()
        elif self.gameState == 1:
            self.DrawGame()
        elif self.gameState == 2:
            self.DrawWin()

    def Update(self):
        if self.gameState == 0:
            self.UpdateTitle()
        elif self.gameState == 1:
            self.UpdateGame()
        elif self.gameState == 2:
            self.UpdateWin()

    def DrawTitle(self):
        jmss.drawImage(self.title_image, 0, 0)

    def UpdateTitle(self):
        if jmss.isKeyDown(KEY_SPACE):
            self.gameState = 1

    def DrawWin(self):
        jmss.drawImage(self.title_image, 0, 0)
        if self.p1.lives <= 0:
            winner = 2
        else:
            winner = 1
        jmss.drawText("Player " + str(winner) + " wins!!", 170, 200, fontSize = 30)

    def UpdateWin(self):
        if jmss.isKeyDown(KEY_SPACE):
            self.gameState = 1
            self.ResetGame()

    def DrawGame(self):
        jmss.clear()
        self.bg_x -= 1
        if self.bg_x <= -self.bg_image.width/2:
            self.bg_x = 0
        jmss.drawImage(self.bg_image, self.bg_x, 0)
        self.drawTriangleList(self.triList)

        for b in self.bullets:
            b.Draw()
        for b in self.balls:
            b.Draw()

        self.p1.Draw()
        self.p2.Draw()

        jmss.drawText("Lives: " + str(self.p1.lives), 10, 350, fontSize=20)
        jmss.drawText("Lives: " + str(self.p2.lives), 490, 350, fontSize=20)

    def UpdateGame(self):
        if self.p1.lives <= 0 or self.p2.lives <= 0:
            self.gameState = 2
            return

        self.angle = self.angle + 0.05

        self.triList = self.rotateTransform(self.shape, self.angle)
        self.triList = self.translateTransform(self.triList, self.camera)

        self.triList = self.perspectiveTransform(self.triList)
        self.triList = self.viewportTransform(self.triList, 500, 500)

        if randint(0, 600) < 1:
            self.SpawnBall(300, 200, filename = self.ball_red_image, respawnable=False)
        for b in self.bullets:
            if b.x >= 600 or b.x <= -b.width:
                self.bullets.remove(b)

        for ball in self.balls:
            for bullet in self.bullets:
                if self.Intersects(bullet.x, bullet.y, bullet.x + bullet.width, bullet.y + bullet.height, \
                                   ball.x, ball.y, ball.x + ball.width, ball.y + ball.height):
                    if ball.xdir * bullet.xdir < 0:
                        ball.xdir *= -1#+= (bullet.xdir / 2.0)
                        self.bullets.remove(bullet)
                        continue
                    elif ball.xdir * bullet.xdir > 0:
                        ball.xdir += (bullet.xdir / 2.0)
                        self.bullets.remove(bullet)
                        continue

        for b in self.balls:
            if self.Intersects(self.p1.x, self.p1.y, self.p1.x + self.p1.width, self.p1.y + self.p1.height, \
                               b.x, b.y, b.x + b.width, b.y + b.height):
                b.x = self.p1.x + self.p1.width
                b.xdir *= -1.05
                b.ydir *= 1.05
                # b.ydir += (self.p1.ydir / 3)
                jmss.playSound(self.blip_sound)

            if self.Intersects(self.p2.x, self.p2.y, self.p2.x + self.p2.width, self.p2.y + self.p2.height, \
                               b.x, b.y, b.x + b.width, b.y + b.height):
                b.x = self.p2.x - b.width
                b.xdir *= -1.05
                b.ydir *= 1.05
                # b.ydir += (self.p1.ydir / 3)
                jmss.playSound(self.blip_sound)

            if b.y <= 0:
                b.y = 0
                b.ydir *= -1

            if b.y >= 400 - b.height:
                b.y = 400 - b.height
                b.ydir *= -1

        if self.p1.y + self.p1.height > 400:
            self.p1.y = 400 - self.p1.height
            self.p1.ydir *= -1
        if self.p2.y + self.p2.height > 400:
            self.p2.y = 400 - self.p2.height
            self.p2.ydir *= -1
        if self.p1.y < 0:
            self.p1.y = 0
            self.p1.ydir *= -1
        if self.p2.y < 0:
            self.p2.y = 0
            self.p2.ydir *= -1

        for b in self.balls:
            b.Update()

        for b in self.bullets:
            b.Update()
        self.p1.Update()
        self.p2.Update()

        for b in self.balls:
            if b.x >= 600:
                self.p2.lives -= 1
                self.balls.remove(b)
                if b.respawnable:
                    self.SpawnBall(300, 200, filename = self.ball_green_image)
            if b.x <= -b.width:
                self.p1.lives -= 1
                self.balls.remove(b)
                if b.respawnable:
                    self.SpawnBall(300, 200, filename = self.ball_green_image)

    def Intersects(self, x1, y1, x2, y2, x3, y3, x4, y4):
        return not (x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4)


jmss = Graphics(width=600, height=400, title="Super Pong")

game = Game()


@jmss.mainloop
def mainloop():
    game.Update()
    game.Draw()


jmss.run()
