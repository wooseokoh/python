import pygame
import random
import sys

monitor = None
r,g,b = [0] * 3
count = 0

def playGame():
    global monitor, count, ship

    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)

    shipX = swidth/2 # 우주선 처음 위치 가로
    shipY = sheight * 0.8 # 우주선 처음 위치 세로
    dx, dy = 0, 0 #

    while True:
        pygame.time.Clock().tick(100) # 게임 진행을 늦쳐줌
        monitor.fill((r, g, b)) # 배경화면 칠하기
        # 키보드나 마우스 이벤트가 들어오는 것을 체크
        for e in pygame.event.get():
            if e.type in [pygame.QUIT]: # <X> 누르면 종료
                pygame.quit()
                sys.exit()
            # 화살표 키보드 이벤트 처리
            if e.type in [pygame.KEYDOWN]:
                if e.type == pygame.K_LEFT: dx = -5
                if e.type == pygame.K_RIGHT: dx = +5
                if e.type == pygame.K_UP: dy = -5
                if e.type == pygame.K_DOWN: dy = +5
            if e.type in [pygame.KEYUP]:
                if e.type == pygame.K_LEFT or \
                   e.type == pygame.K_RIGHT or \
                   e.type == pygame.K_UP or \
                   e.type == pygame.K_DOWN:
                    dx, dy = 0, 0
            if(0< shipX + dx and shipX + dx <= swidth - shipSize[0] \
                    and (sheight /2 < shipY + dy and shipY + dy <= sheight - shipSize[1])):
                shipX += dx
                shipY += dy
            paintEntity(ship, shipX, shipY)
        pygame.display.update() # 화면 업데이트하기
        print("업데이트횟수: ", count) # 게임진행 확인
        count = count + 1
        # print('~', end='')

### 전역변수 선언 ###
swidth, sheight = 500, 700
monitor = None
ship = None
shipSize = 0


def paintEntity(entity, x, y):
    monitor.blit(entity, (x,y)) # 모니터에 위치시켜주는 함수.

monitor = pygame.init()
pygame.display.set_caption('우주괴물 무찌르기')
monitor =  pygame.display.set_mode((swidth, sheight))

ship = pygame.image.load('ship02.png')
shipSize = ship.get_rect().size
playGame()