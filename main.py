import sys

import pygame

pygame.init()
clock = pygame.time.Clock()
display_width = 1820
display_height = 980
display = pygame.display.set_mode((1820, 980))
main_font = pygame.font.SysFont("cambria", 50)


def print_text(text, x, y, font_type='Font.ttf', font_col=(0, 0, 0), font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(text, True, font_col)
    display.blit(text, (x, y))


def pause():
    paused = True
    main_menue(start_butt_text='test1.png')
    while paused:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused = False
            start_game()


def start_game():
    bckimg = pygame.image.load(r'C:\Users\Лев\PycharmProjects\gameme\testimageforgame2.jpg')
    display.blit(bckimg, (0, 0))
    pygame.display.update()
    menue_butt = Button(50, 50, 1700, 50, "mbutt.png")
    pygame.display.update()
    game = True
    while game:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                game = False
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                menue_butt.checkForInput(pygame.mouse.get_pos(), pause)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause()
        menue_butt.changeimg(pygame.mouse.get_pos())
        pygame.display.update()


def closer():
    pygame.quit()
    sys.exit()


class Button:
    def __init__(self, weight, height, x_pos, y_pos, active):
        self.weight = weight
        self.height = height
        self.active = pygame.transform.scale(pygame.image.load(active), (weight, height))
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.active.get_rect(topleft=(self.x_pos, self.y_pos))

    def checkForInput(self, position, action=None):
        if self.x_pos < position[0] < self.x_pos + self.x_pos and self.y_pos < position[1] < self.y_pos + self.y_pos:
            action()

    def changeimg(self, position, in_active=None):
        if in_active == None:
            display.blit(self.active, (self.x_pos, self.y_pos))
        else:
            button = [self.active,
                      pygame.transform.scale(pygame.image.load(in_active), (self.weight, self.height))]
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                            self.rect.bottom):
                display.blit(button[0], (self.x_pos, self.y_pos))
            elif in_active != None:
                display.blit(button[1], (self.x_pos, self.y_pos))


def main_menue(start_butt_text='test1.png'):
    bckimg_M = pygame.image.load(r'C:\Users\Лев\PycharmProjects\gameme\testimageforgame1.jpg')
    display.blit(bckimg_M, (0, 0))
    start_butt = Button(400, 150, 760, 250, start_butt_text)
    quit_butt = Button(400, 150, 760, 450, 'test2.png')
    pygame.display.update()
    show = True
    while show:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                start_butt.checkForInput(pygame.mouse.get_pos(), start_game)
                quit_butt.checkForInput(pygame.mouse.get_pos(), closer)
                pygame.display.update()
        start_butt.changeimg(pygame.mouse.get_pos(), 'test2.png')
        quit_butt.changeimg(pygame.mouse.get_pos(), 'test1.png')
        pygame.display.update()


def reader():
    with open('novel.txt', 'r', encoding='utf-8') as file:
        a = len(file.readlines())
        file.seek(0)

        for i in range(a):
            text_on_screen = file.readline()


main_menue()
