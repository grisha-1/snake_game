# -*- coding: utf-8 -*-
import pygame
from random import randrange

pygame.init()  # Инициализация модуля pygame


# Создаём главный класс приложения
class game:
    x = 1
    scoring_ = 1
    code_ = 0
    RES = 700
    SIZE = 20
    sc = pygame.display.set_mode([RES, RES])
    pygame.display.set_caption('The SNAKE._.')
    time = 0
    sound_ = 0.4
    codddde = 0

    def game_sound(self):
        wav_file = 'snake_sound.wav'
        freq = 44100
        bitsize = -16
        channels = 2
        buffer = 1024
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(self.sound_)
        pygame.mixer.music.load(wav_file)
        pygame.mixer.music.play()

    @staticmethod
    def eat_sound():
        wav_file1 = 'eat_sound.wav'
        freq1 = 44100
        bitsize1 = -16
        channels1 = 2
        buffer1 = 1024
        pygame.mixer.init(freq1, bitsize1, channels1, buffer1)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.load(wav_file1)
        pygame.mixer.music.play()

    def start(self):
        scoring = 1
        coding = 0
        time_ = 1
        megaapple = 800, 800
        x, y = randrange(0, self.RES, self.SIZE), randrange(0, self.RES, self.SIZE)
        apple = randrange(0, self.RES, self.SIZE), randrange(0, self.RES, self.SIZE)
        dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
        dirs_ = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
        fps = 10
        score = 0
        length = 1
        snake = [(x, y)]
        dx, dy = 0, 0
        clock = pygame.time.Clock()
        font_score = pygame.font.SysFont('Times new Roman', 26, bold=True)
        font_end = pygame.font.SysFont('Arial', 66, bold=True)
        img = pygame.image.load('grass.png').convert()

        while True:
            if coding == 1:
                scoring += 1
                if scoring % fps == 1:
                    time_ += 1

            self.scoring_ += 1
            if self.scoring_ % fps == 0:
                self.time += 1
                if self.time % 44 == 1:
                    self.game_sound()

            if time_ % 30 == 0:
                megaapple = randrange(0, self.RES, self.SIZE), randrange(0, self.RES, self.SIZE)
            self.sc.blit(img, (0, 0))
            [(pygame.draw.rect(self.sc, pygame.Color('green'), (i, j, self.SIZE - 1, self.SIZE - 1))) for i, j in snake]
            pygame.draw.rect(self.sc, pygame.Color('red'), (*apple, self.SIZE, self.SIZE))
            pygame.draw.rect(self.sc, pygame.Color('orange'), (*megaapple, self.SIZE, self.SIZE))
            render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('blue'))
            position = font_score.render(f'x: {x} y: {y}', True, pygame.Color('blue'))
            time = font_score.render(f'TIME: {time_}', True, pygame.Color('black'))
            help_ = font_score.render('w: вверх       '
                                      'a: влево       '
                                      's: вниз       '
                                      'd: вправо       '
                                      'r: заново       ', True, pygame.Color('white'))
            self.sc.blit(time, (300, 5))
            self.sc.blit(position, (555, 5))
            self.sc.blit(render_score, (5, 5))
            if self.x == 0:
                pass
            else:
                self.sc.blit(help_, (5, 25))
            pygame.display.flip()
            x += dx * self.SIZE
            y += dy * self.SIZE
            snake.append((x, y))
            snake = snake[-length:]

            # eating apple
            key = pygame.key.get_pressed()
            pygame.display.flip()
            if snake[-1] == apple:
                apple = randrange(0, self.RES, self.SIZE), randrange(0, self.RES, self.SIZE)
                length += 1
                fps += 1
                score += 1
            if snake[-1] == megaapple:
                megaapple = 10000, 10000
                length += 5
                self.code_ = 0
                fps += 3
                score += 5
                pygame.display.flip()
            # проигрыш

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            if key[pygame.K_w] and dirs['W'] or key[pygame.K_UP] and dirs_['UP']:
                dx, dy = 0, -1
                dirs = {'W': True, 'S': False, 'A': True, 'D': True}
                dirs_ = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}
                coding = 1
                pygame.display.flip()
            elif key[pygame.K_s] and dirs['S'] or key[pygame.K_DOWN] and dirs_['DOWN']:
                dx, dy = 0, 1
                dirs = {'W': False, 'S': True, 'A': True, 'D': True}
                dirs_ = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
                coding = 1
                pygame.display.flip()
            elif key[pygame.K_a] and dirs['A'] or key[pygame.K_LEFT] and dirs_['LEFT']:
                dx, dy = -1, 0
                dirs = {'W': True, 'S': True, 'A': True, 'D': False}
                dirs_ = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}
                coding = 1
                pygame.display.flip()
            elif key[pygame.K_d] and dirs['D'] or key[pygame.K_RIGHT] and dirs_['RIGHT']:
                dx, dy = 1, 0
                dirs = {'W': True, 'S': True, 'A': False, 'D': True}
                dirs_ = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}
                coding = 1
                pygame.display.flip()
            if key[pygame.K_ESCAPE]:
                exit()
            if key[pygame.K_h]:
                if self.x == 0:
                    self.x = 1
                else:
                    self.x = 0

            if x < 0 or x > self.RES - self.SIZE or y < 0 or y > self.RES - self.SIZE or len(snake) != len(set(snake)):
                render_end = font_end.render('GAME OVER ! ', True, pygame.Color('cyan'))
                self.sc.blit(render_end, (130, 350))
                while True:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_r]:
                        break
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                    pygame.display.flip()
                    clock.tick(fps)
                break
            pygame.display.flip()
            clock.tick(fps)


if __name__ == "__main__":
    while True:
        a = game()
        a.start()
else:
    print("Это не библиотека!")
