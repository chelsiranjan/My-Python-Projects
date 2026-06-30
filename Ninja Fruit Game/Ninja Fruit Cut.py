import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruit Ninja')

clock = pygame.time.Clock()

gravity = 0.2
fruits = []
bombs =[]

fruit_spawn_timer = 0
fruit_spawn_delay = random.randint(20, 50)

bomb_spawn_timer = 0
bomb_spawn_delay = random.randint(120,300)


def create_fruit():
    radius = random.randint(30, 45)

    return {
        'x': random.randint(100, 700),
        'y': HEIGHT + radius,
        'radius': radius,
        'color': (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)),
        'vx': random.uniform(-2, 2),
        'vy': random.uniform(-12, -9)}

def create_bomb():
    radius = 35

    return {
        'x': random.randint(100, 700),
        'y': HEIGHT + radius,
        'radius': radius,
        'color': (40, 40, 40),
        'color_outline': (255,0,0),
        'vx': random.uniform(-2, 2),
        'vy': random.uniform(-12, -9)}


running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fruit_spawn_timer += 1
    bomb_spawn_timer += 1

    if fruit_spawn_timer >= fruit_spawn_delay:
        fruits.append(create_fruit())
        fruit_spawn_timer = 0
        fruit_spawn_delay = random.randint(20, 50)

    if bomb_spawn_timer >= bomb_spawn_delay:
        bombs.append(create_bomb())
        bomb_spawn_timer = 0
        bomb_spawn_delay = random.randint(120, 300)


    screen.fill((30, 30, 30))


    for fruit in fruits[:]:  
        fruit['x'] += fruit['vx']
        fruit['y'] += fruit['vy']

        fruit['vy'] += gravity

        pygame.draw.circle(screen,fruit['color'],(int(fruit['x']), int(fruit['y'])),fruit['radius'])

        if fruit['y'] - fruit['radius'] > HEIGHT:
            fruits.remove(fruit)

    for bomb in bombs[:]:
        bomb['x'] += bomb['vx']
        bomb['y'] += bomb['vy']

        bomb['vy'] += gravity

        pygame.draw.circle(screen,bomb['color'],(int(bomb['x']), int(bomb['y'])),bomb['radius'])
        pygame.draw.circle(screen,bomb['color_outline'],(int(bomb['x']), int(bomb['y'])),bomb['radius'], 3)
        
        if bomb['y'] - bomb['radius'] > HEIGHT:
            bombs.remove(bomb)

    pygame.display.flip()

pygame.quit()