import pygame
import random
import os
import sys
import webbrowser


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


icon_win = resource_path('Resources/ru.bmp')
pygame.display.set_icon(pygame.image.load(icon_win))
white = (255, 255, 255)
black = (0, 0, 0)
gray = (120, 120, 120)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pygame.init()
pygame.font.init()
shrift = resource_path('Resources/comicsansms3.ttf')
my_font = pygame.font.Font(shrift, 30)
FPS = 60
clock = pygame.time.Clock()
win = pygame.display.set_mode((450, 720))  # Размер окна
pygame.display.set_caption("Голосуем за")  # Название окна
text_1 = 'Голосуем за'
text_2 = 'отключение интернета?'
click = False


def draw_button(name, color, x, y, height, length):
    global my_font
    pygame.draw.rect(win, color, (x, y, height, length))
    text_no = my_font.render('Нет', False, (0, 0, 0))
    win.blit(text_no, (x + 50, y + 5))


pygame.font.init()
tf2build_font1 = resource_path('Resources/tf2build.ttf')
tf2secondary_font1 = resource_path('Resources/tf2secondary.ttf')
smallfon = pygame.font.Font(tf2build_font1, 18)
myfont = pygame.font.Font(tf2build_font1, 16)
font = pygame.font.Font(tf2build_font1, 30)
font2 = pygame.font.Font(tf2build_font1, 50)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def play():
    global text_1
    global text_2
    button_1 = pygame.Rect(50, 200, 150, 50)
    button_2 = pygame.Rect(250, 200, 150, 50)

    movie = {1: [250, 300], 2: [250, 400], 3: [250, 500], 4: [250, 600], 5: [50, 300],
             6: [50, 400], 7: [50, 500], 8: [50, 600], 9: [250, 200], 0: [250, 200]}
    X = 250
    Y = 200
    run = True
    while run:
        # mouse
        mx, my = pygame.mouse.get_pos()
        # keys
        keys = pygame.key.get_pressed()
        keys_pres = pygame.key.get_pressed()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if keys_pres[pygame.K_ESCAPE]:
                run = False
            if even.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(even.pos):
                    print('ok')
                    run = False
                    main_menu()
        if button_2.collidepoint((mx, my)):
            random_value = movie.get(random.randint(0, 9))
            X, Y = random_value[0], random_value[1]
            button_2 = pygame.Rect(X, Y, 150, 50)

        # draw
        win.fill(gray)  # Background

        pygame.draw.rect(win, blue, button_1)
        text_yes = my_font.render('Да', False, (0, 0, 0))
        win.blit(text_yes, (100, 205))
        text_vote_1 = my_font.render(text_1, False, (0, 0, 0))
        win.blit(text_vote_1, (40, 55))
        text_vote_2 = my_font.render(text_2, False, (0, 0, 0))
        win.blit(text_vote_2, (40, 95))

        draw_button('No', red, X, Y, 150, 50)

        pygame.display.update()
        clock.tick(FPS)


def text1():
    global text_1
    global text_2
    running = True
    font = pygame.font.Font(tf2build_font1, 30)
    font_2 = pygame.font.Font(tf2build_font1, 20)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(40, 100, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    while running:

        keys_pres = pygame.key.get_pressed()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys_pres[pygame.K_ESCAPE]:
                main_menu()

            if even.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(even.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if even.type == pygame.KEYDOWN:
                if active:

                    if even.key == pygame.K_RETURN:
                        print(text)
                        text_1 = text
                        main_menu()
                    elif even.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += even.unicode

        win.fill(gray)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(win, color, input_box, 2)
        draw_text(' Введите текст:', font, (0, 0, 0), win, 30, 50)
        draw_text('И нажмите Enter!', font_2, (0, 0, 0), win, 50, 150)
        draw_text('Esc - назад', font_2, (0, 20, 50), win, 50, 220)
        draw_text('', font_2, (0, 20, 50), win, 30, 250)
        pygame.display.update()
        clock.tick(FPS)


def text2():
    global text_1
    global text_2
    running = True
    font = pygame.font.Font(tf2build_font1, 30)
    font_2 = pygame.font.Font(tf2build_font1, 20)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(40, 100, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    while running:

        keys_pres = pygame.key.get_pressed()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys_pres[pygame.K_ESCAPE]:
                main_menu()

            if even.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(even.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if even.type == pygame.KEYDOWN:
                if active:

                    if even.key == pygame.K_RETURN:
                        print(text)
                        text_2 = text
                        main_menu()
                    elif even.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += even.unicode

        win.fill(gray)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(win, color, input_box, 2)
        draw_text(' Введите текст:', font, (0, 0, 0), win, 30, 50)
        draw_text('И нажмите Enter!', font_2, (0, 0, 0), win, 50, 150)
        draw_text('Esc - назад', font_2, (0, 20, 50), win, 50, 220)
        draw_text('', font_2, (0, 20, 50), win, 30, 250)
        pygame.display.update()
        clock.tick(FPS)


def main_menu():
    click = False
    my_font_2 = pygame.font.Font(shrift, 15)
    while True:

        win.fill(gray)
        draw_text('Программа бесплатная.', my_font_2, (0, 0, 255), win, 50, 630)
        draw_text('Вы сами отвечаете за свои действия.', my_font_2, (0, 0, 255), win, 50, 650)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 220, 50)
        button_2 = pygame.Rect(50, 200, 250, 50)
        button_3 = pygame.Rect(50, 300, 300, 50)
        button_4 = pygame.Rect(50, 500, 350, 50)
        button_5 = pygame.Rect(50, 560, 180, 30)
        if button_1.collidepoint((mx, my)):
            if click:
                print('Голос')
        if button_2.collidepoint((mx, my)):
            if click:
                print('Текст 1')
        if button_3.collidepoint((mx, my)):
            if click:
                print('Текст 2')
        if button_4.collidepoint((mx, my)):
            if click:
                print('Donation')
                webbrowser.open('https://www.donationalerts.com/r/vdk45')
        if button_5.collidepoint((mx, my)):
            if click:
                print('download')
                webbrowser.open('https://cloud.mail.ru/public/BHJJ/6djS1G3qZ')
        pygame.draw.rect(win, blue, button_1)
        pygame.draw.rect(win, (20, 120, 120), button_2)
        pygame.draw.rect(win, (20, 120, 120), button_3)
        pygame.draw.rect(win, (255, 120, 0), button_4)
        pygame.draw.rect(win, blue, button_5)
        click = False
        keys_pres = pygame.key.get_pressed()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys_pres[pygame.K_ESCAPE]:
                play()
            if even.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(even.pos):
                    print('ok')
                    if even.button == 1:
                        click = True
                        play()
                if button_2.collidepoint(even.pos):
                    print('ok')
                    if even.button == 1:
                        click = True
                        text1()
                if button_3.collidepoint(even.pos):
                    print('ok')
                    if even.button == 1:
                        click = True
                        text2()
                if button_4.collidepoint(even.pos):
                    print('ok')
                    if even.button == 1:
                        click = True
                if button_5.collidepoint(even.pos):
                    print('ok')
                    if even.button == 1:
                        click = True

        draw_text('Начать', font, (255, 255, 255), win, 80, 115)
        draw_text('Текст 1', font, (255, 255, 255), win, 80, 215)
        draw_text('Текст 2', font, (255, 255, 255), win, 80, 315)
        draw_text('Подержать меня', font, (255, 255, 255), win, 80, 515)
        draw_text('скачать приложение', my_font_2, (255, 255, 255), win, 70, 565)
        pygame.display.update()
        clock.tick(FPS)


main_menu()

pygame.quit()
