from images import *
import random


def slot_1():
    for nums in range(10):
        pygame.draw.rect(screen, WHITE, (0.05*width, height/2-(width/3-0.1*width)/2+y1-(height/2-(width/3-0.1*width)/2)*nums, width/3-0.1*width, width/3-0.1*width))
        if not speed_stop:
            save_text[0] = random.choice(slot1)
        text = font.render(slot1[nums], True, RED)
        text_render = text.get_rect()
        text_render.center = (0.05*width+width/6-0.05*width, height/2-(width/3-0.1*width)/2+y1-(height/2-(width/3-0.1*width)/2)*nums+width/6-0.05*width)
        screen.blit(text, text_render)
    if speed_stop:
        pygame.draw.rect(screen, BLACK, (0.05*width, 0, width/3-0.1*width, height))
        pygame.draw.rect(screen, WHITE, (0.05*width, height*0.5-width/6+width*0.05, width/3-0.1*width, width/3-0.1*width))
        text = font.render(save_text[0], True, RED)
        text_render = text.get_rect()
        text_render.center = (0.05*width+width/6-0.05*width, height*0.5)
        screen.blit(text, text_render)


def slot_2():
    for nums in range(10):
        pygame.draw.rect(screen, WHITE, (0.05*width+width/3, height/2-(width/3-0.1*width)/2+y2-(height/2-(width/3-0.1*width)/2)*nums, width/3-0.1*width, width/3-0.1*width))
        if not speed_stop:
            save_text[1] = random.choice(slot2)
        text = font.render(slot2[nums], True, RED)
        text_render = text.get_rect()
        text_render.center = (0.05 * width+width/3 + width / 6 - 0.05 * width,
                              height / 2 - (width / 3 - 0.1 * width) / 2 + y2 - (
                                          height / 2 - (width / 3 - 0.1 * width) / 2) * nums + width / 6 - 0.05 * width)
        screen.blit(text, text_render)
        if speed_stop:
            pygame.draw.rect(screen, BLACK, (0.05 * width+width/3, 0, width / 3 - 0.1 * width, height))
            pygame.draw.rect(screen, WHITE, (
            0.05 * width+width/3, height * 0.5 - width / 6 + width * 0.05, width / 3 - 0.1 * width, width / 3 - 0.1 * width))
            text = font.render(save_text[1], True, RED)
            text_render = text.get_rect()
            text_render.center = (0.05 * width+width/3 + width / 6 - 0.05 * width, height * 0.5)
            screen.blit(text, text_render)


def slot_3():
    for nums in range(10):
        pygame.draw.rect(screen, WHITE, (0.05*width+width*2/3, height/2-(width/3-0.1*width)/2+y3-(height/2-(width/3-0.1*width)/2)*nums, width/3-0.1*width, width/3-0.1*width))
        if not speed_stop:
            save_text[2] = random.choice(slot3)
        text = font.render(slot3[nums], True, RED)
        text_render = text.get_rect()
        text_render.center = (0.05 * width+width*2/3 + width / 6 - 0.05 * width,
                              height / 2 - (width / 3 - 0.1 * width) / 2 + y3 - (
                                          height / 2 - (width / 3 - 0.1 * width) / 2) * nums + width / 6 - 0.05 * width)
        screen.blit(text, text_render)
        if speed_stop:
            pygame.draw.rect(screen, BLACK, (0.05 * width+width*2/3, 0, width / 3 - 0.1 * width, height))
            pygame.draw.rect(screen, WHITE, (
            0.05 * width+width*2/3, height * 0.5 - width / 6 + width * 0.05, width / 3 - 0.1 * width, width / 3 - 0.1 * width))
            text = font.render(save_text[2], True, RED)
            text_render = text.get_rect()
            text_render.center = (0.05 * width+width*2/3 + width / 6 - 0.05 * width, height * 0.5)
            screen.blit(text, text_render)


running = True
while running:
    clock.tick(FPS)
    if stop:
        if speed1 >= 2:
            speed1 -= 2
        else:
            speed1 = 0
        if speed2 >= 3:
            speed2 -= 3
        else:
            speed2 = 0
        if speed3 >= 4:
            speed3 -= 4
        else:
            speed3 = 0
        if speed1 == 0 and speed2 == 0 and speed3 == 0:
            speed_stop = True
    else:
        speed1, speed2, speed3, speed_stop = 20, 30, 40, False
    y1 += speed1
    y2 += speed2
    y3 += speed3
    if y1 > (height/2-(width/3-0.1*width)/2)*9:
        y1 = 0
    if y2 > (height/2-(width/3-0.1*width)/2)*9:
        y2 = 0
    if y3 > (height/2-(width/3-0.1*width)/2)*9:
        y3 = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not stop:
                stop = True
            elif event.key == pygame.K_SPACE and stop:
                stop = False
    screen.fill(BLACK)
    slot_1()
    slot_2()
    slot_3()
    pygame.draw.rect(screen, BLACK, (0, 0, width, height/3))
    pygame.draw.rect(screen, BLACK, (0, height*2/3, width, height))
    pygame.display.update()
pygame.quit()
