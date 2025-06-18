# Example file showing a basic pygame "game loop"
import pygame
from mesh import Mesh
from triangle import Triangle
from vector import Vec3d
from constants import *

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    mesh = Mesh()
    # note that +z is into screen, +x is right, +y is up
    mesh.tris = [[Vec3d(0,0,0), Vec3d(0,1,0), Vec3d(1,1,0)], # SOUTH
                 [Vec3d(0,0,0), Vec3d(1,1,0), Vec3d(1,0,0)],
                 
                 [Vec3d(1,0,0), Vec3d(1,1,0), Vec3d(1,1,1)], # EAST
                 [Vec3d(1,0,0), Vec3d(1,1,1), Vec3d(1,0,1)],
                 
                 [Vec3d(1,0,1), Vec3d(1,1,1), Vec3d(0,1,1)], # NORTH
                 [Vec3d(1,0,1), Vec3d(0,1,1), Vec3d(0,0,1)],

                 [Vec3d(0,1,0), Vec3d(0,1,1), Vec3d(1,1,1)], # TOP
                 [Vec3d(0,1,0), Vec3d(1,1,1), Vec3d(1,1,0)],
                 
                 [Vec3d(0,0,1), Vec3d(0,0,0), Vec3d(1,0,0)], # BOTTOM
                 [Vec3d(0,0,1), Vec3d(1,0,0), Vec3d(1,0,1)],]

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        pygame.draw.circle(screen, "red", player_pos, 40)
        pygame.draw
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        for tri in mesh.tris:
            list_points = []
            for vec in tri:
                list_points.append(vec.get_py_point())
            list_points = [(100*x, 100*y) for (x,y) in list_points]
            pygame.draw.lines(screen, "white", True, list_points)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()



if __name__ == "__main__":
    main()