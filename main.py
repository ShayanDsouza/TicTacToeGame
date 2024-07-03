import pygame

pygame.init()

WINDOW_WIDTH = 720
PIXEL_WIDTH = WINDOW_WIDTH // 3

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsans', 32)
winner_text = font.render('', True, 'green')
textRect = winner_text.get_rect()
textRect.center = (WINDOW_WIDTH // 2 - PIXEL_WIDTH // 2, WINDOW_WIDTH // 2)

running = True

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]


def load_icon(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)


ICON_X = load_icon('x-icon.png', [PIXEL_WIDTH, PIXEL_WIDTH])
ICON_O = load_icon('o-icon.png', [PIXEL_WIDTH, PIXEL_WIDTH])
GRID = load_icon('Tic TAc Toe.jpg', [WINDOW_WIDTH, WINDOW_WIDTH])

PLAYER_1 = 0
PLAYER_2 = 1
player = PLAYER_1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    pygame.display.flip()
    screen.fill("white")
    screen.blit(GRID, (0, 0))
    pygame.event.wait()

pygame.quit()