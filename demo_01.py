import pygame
from pygame.locals import Rect

pygame.init()

clock = pygame.time.Clock()
# ウィンドウサイズ
screen = pygame.display.set_mode([640, 480])
# ウィンドウの名前
pygame.display.set_caption("pygame demo - window title here")

running = True
x1, y1 = 0, 2

# infinite loop top ----
while running:
    # press ctrl-c to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #　ウィンドウの背景の色
    screen.fill((0, 0, 255))  # back ground color

    pygame.draw.circle(screen, (176, 176, 222), (320, 240), 120)
    pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
    pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
    pygame.draw.rect(screen, (120, 120, 120), Rect(120, 120, 200, 120))

    #動く点のon,offそれぞれの色
    color_on = (240, 120, 120)
    color_off = (120, 120, 120)
    # 動く点の四角の横の数
    for x0 in range(5):
        #　動く点の四角の縦の数
        for y0 in range(7):
            # pygame.draw.circle(screen, color_off, (24 + x0 * 16, 24 + y0 * 16), 8)
            pygame.draw.rect(screen, color_off, Rect(24 + x0 * 16, 24 + y0 * 16, 12, 12))

    # pygame.draw.circle(screen, color_on, (24 + x1 * 16, 24 + y1 * 16), 8)
    pygame.draw.rect(screen, color_on, Rect(24 + x1 * 16, 24 + y1 * 16, 12, 12))
    # ステップ3
    x1 += 1
    if x1 > 4:
        x1 = 0
        y1 += 1
        if y1 > 6:
            y1 = 0

    pygame.display.flip()  # update
    clock.tick(5)  # FPS, Frame Per Second
# infinite loop bottom ----

pygame.quit()
