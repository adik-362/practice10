import pygame

pygame.init()

# Размер окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen.fill(WHITE)

# Настройки
drawing = False
tool = "brush"   # brush / rect / circle / eraser
color = BLACK
start_pos = None
radius = 5

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Нажатие кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Отпуск кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            # Рисуем фигуры
            if tool == "rect":
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, color, rect, 2)

            elif tool == "circle":
                center = start_pos
                r = int(((end_pos[0]-center[0])**2 + (end_pos[1]-center[1])**2) ** 0.5)
                pygame.draw.circle(screen, color, center, r, 2)

        # Движение мыши
        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "brush":
                pygame.draw.circle(screen, color, event.pos, radius)

            elif tool == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, radius)

        # Кнопки клавиатуры
        if event.type == pygame.KEYDOWN:

            # Выбор инструментов
            if event.key == pygame.K_b:
                tool = "brush"

            elif event.key == pygame.K_r:
                tool = "rect"

            elif event.key == pygame.K_c:
                tool = "circle"

            elif event.key == pygame.K_e:
                tool = "eraser"

            # Выбор цвета
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE

    pygame.display.flip()

pygame.quit()