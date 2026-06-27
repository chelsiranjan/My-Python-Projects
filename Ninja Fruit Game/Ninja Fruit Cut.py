import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Ninja")
clock = pygame.time.Clock()

gravity = 0.2
fruits = []

spawn_timer = 0
spawn_delay = random.randint(20, 50)


def create_fruit():
    radius = random.randint(20, 50)

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


running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    spawn_timer += 1

    if spawn_timer >= spawn_delay:
        fruits.append(create_fruit())
        spawn_timer = 0
        spawn_delay = random.randint(20, 50)

    screen.fill((30, 30, 30))


    for fruit in fruits[:]:  
        fruit['x'] += fruit['vx']
        fruit['y'] += fruit['vy']

        fruit['vy'] += gravity

        pygame.draw.circle(
            screen,
            fruit["color"],
            (int(fruit["x"]), int(fruit["y"])),
            fruit["radius"])

        if fruit["y"] - fruit["radius"] > HEIGHT:
            fruits.remove(fruit)

    pygame.display.flip()

pygame.quit()