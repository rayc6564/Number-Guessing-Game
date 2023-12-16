import pygame 
import os
import random

pygame.init()

WIDTH, HEIGHT = 800,565

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Test")

GHOST_IMG = pygame.image.load(os.path.join('pictures', 'ghost.png'))
GHOST = pygame.transform.scale(GHOST_IMG, (100,100))

MESSAGE_IMG = pygame.image.load(os.path.join('pictures', 'message.png'))
MESSAGE = pygame.transform.scale(MESSAGE_IMG, (150, 150))

X_IMAGE = pygame.image.load(os.path.join('pictures', 'x.png'))


NUM1 = pygame.image.load(os.path.join('pictures', 'num1.png'))

NUM2 = pygame.image.load(os.path.join('pictures', 'num2.png'))

NUM3 = pygame.image.load(os.path.join('pictures', 'num3.png'))

NUM4 = pygame.image.load(os.path.join('pictures', 'num4.png'))

NUM5 = pygame.image.load(os.path.join('pictures', 'num5.png'))

NUM6 = pygame.image.load(os.path.join('pictures', 'num6.png'))

NUM7 = pygame.image.load(os.path.join('pictures',  'num7.png'))

NUM8 = pygame.image.load(os.path.join('pictures', 'num8.png'))

NUM9 = pygame.image.load(os.path.join('pictures', 'num9.png'))

NUM10 = pygame.image.load(os.path.join('pictures', 'num10.png'))

NUM11 = pygame.image.load(os.path.join('pictures', 'num11.png'))

NUM12 = pygame.image.load(os.path.join('pictures', 'num12.png'))

NUM13 = pygame.image.load(os.path.join('pictures', 'num13.png'))

NUM14 = pygame.image.load(os.path.join('pictures', 'num14.png'))

NUM15 = pygame.image.load(os.path.join('pictures', 'num15.png'))

NUM16 = pygame.image.load(os.path.join('pictures', 'num16.png'))

NUM17 = pygame.image.load(os.path.join('pictures', 'num17.png'))

NUM18 = pygame.image.load(os.path.join('pictures', 'num18.png'))

NUM19 = pygame.image.load(os.path.join('pictures', 'num19.png'))

NUM20 = pygame.image.load(os.path.join('pictures', 'num20.png'))


BLACK = (0,0,0)

WHITE = (255,255,255)

RED = (255,0,0)

CYAN = (0,100,100)

font = pygame.font.SysFont(None, 23)

con_font = pygame.font.SysFont(None, 50, italic = True)


#draw text function
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    width = img.get_width()
    SCREEN.blit(img, (x - (width / 2), y))

def window_draw(tries):

    tries_text = font.render("Tries: " + str(tries), 1, BLACK)    
    SCREEN.blit(tries_text, (10,10))

    SCREEN.blit(GHOST, (100,450))

    SCREEN.blit(MESSAGE, (170, 300))

    SCREEN.blit(NUM1, (20, 100))
    SCREEN.blit(NUM2, (100, 100))
    SCREEN.blit(NUM3, (180, 100))
    SCREEN.blit(NUM4, (260, 100))
    SCREEN.blit(NUM5, (340, 100))
    SCREEN.blit(NUM6, (420, 100))
    SCREEN.blit(NUM7, (500, 100))
    SCREEN.blit(NUM8, (580, 100))
    SCREEN.blit(NUM9, (660, 100))
    SCREEN.blit(NUM10, (740, 100))
    SCREEN.blit(NUM11, (20, 200))
    SCREEN.blit(NUM12, (100, 200))
    SCREEN.blit(NUM13, (180, 200))
    SCREEN.blit(NUM14, (260, 200))
    SCREEN.blit(NUM15, (340, 200))
    SCREEN.blit(NUM16, (420, 200))
    SCREEN.blit(NUM17, (500, 200))
    SCREEN.blit(NUM18, (580, 200))
    SCREEN.blit(NUM19, (660, 200))
    SCREEN.blit(NUM20, (740, 200))

    

num_choice = {
    1: NUM1.get_rect(topleft = (20,100)),
    2: NUM2.get_rect(topleft = (100,100)),
    3: NUM3.get_rect(topleft = (180,100)),
    4: NUM4.get_rect(topleft = (260,100)),
    5: NUM5.get_rect(topleft = (340,100)),
    6: NUM6.get_rect(topleft = (420,100)),
    7: NUM7.get_rect(topleft = (500,100)),
    8: NUM8.get_rect(topleft = (580,100)),
    9: NUM9.get_rect(topleft = (660,100)),
    10: NUM10.get_rect(topleft = (740,100)),
    11: NUM11.get_rect(topleft = (20,200)),
    12: NUM12.get_rect(topleft = (100,200)),
    13: NUM13.get_rect(topleft = (180,200)),
    14: NUM14.get_rect(topleft = (260,200)),
    15: NUM15.get_rect(topleft = (340,200)),
    16: NUM16.get_rect(topleft = (420,200)),
    17: NUM17.get_rect(topleft = (500,200)),
    18: NUM18.get_rect(topleft = (580,200)),
    19: NUM19.get_rect(topleft = (660,200)),
    20: NUM20.get_rect(topleft = (740,200))
}


CHOOSE_NUM = random.randint(1, 20)

def main():

    WIN = False

    FPS = 60
    clock = pygame.time.Clock()

    tries = 5

    run = True

    DURATION = 2

    while run:
        clock.tick(FPS)

        SCREEN.fill((202, 246, 196))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if num_choice[CHOOSE_NUM].collidepoint(pos):
                    WIN = True
                else:
                    tries -= 1
                    COUNT = 0
                    while COUNT < DURATION:
                        SCREEN.blit(X_IMAGE, (WIDTH / 2 - 210, HEIGHT / 2 - 279))
                        pygame.display.flip()
                        pygame.time.delay(500 // DURATION)
                        COUNT += 1

                    

            if event.type == pygame.QUIT:
                run = False

        draw_text("Guess A Number", font, BLACK, 245, 320)
        draw_text("Between", font, BLACK, 245, 350)
        draw_text("(1 - 20)", font, BLACK, 245, 380)

        window_draw(tries)

        if tries == 0:
            SCREEN.fill(RED)
            TRY_COUNT = 0
            while TRY_COUNT < DURATION:
                draw_text("Out of Tries", con_font, BLACK, WIDTH / 2, HEIGHT / 2 - 50)
                draw_text(f"The Number was {CHOOSE_NUM}", con_font, WHITE, WIDTH / 2, HEIGHT / 2 + 50)
                pygame.display.flip()
                pygame.time.delay(1000 // DURATION)
                TRY_COUNT += 1
                run = False
                            

        if WIN:
            SCREEN.fill(WHITE)
            WIN_COUNT = 0
            while WIN_COUNT < DURATION:
                draw_text(f"Correct! The Number Was {CHOOSE_NUM}", con_font, BLACK, WIDTH / 2, HEIGHT / 2)
                pygame.display.flip()
                pygame.time.delay(1000 // DURATION)
                WIN_COUNT += 1
                run = False
            

        pygame.display.flip()

        pygame.display.update()
        

    pygame.quit()


if __name__ == "__main__":
    main()
