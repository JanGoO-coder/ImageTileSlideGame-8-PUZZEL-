from crop import crop_picture
from puzzle import Puzzle
import pygame
pygame.init()

W = 700
H = 700
C = (W//3 - 20, H//3 - 20)

window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Puzzle")

crop_picture()

puzzle = Puzzle()

def loop():

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    puzzle.__init__()
                if event.button == 3:
                    puzzle.auto_solve()
                
            if event.type == pygame.KEYDOWN and not puzzle.is_correct():
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT:
                    puzzle.move_right()
                if event.key == pygame.K_RIGHT:
                    puzzle.move_left()
                if event.key == pygame.K_UP:
                    puzzle.move_down()
                if event.key == pygame.K_DOWN:
                    puzzle.move_up()
        
        window.fill((100, 100, 200))
        # window.fill((0, 0, 0))
        puzzle.draw(window, W, H, C)
        # pygame.draw.rect(window, (200, 200, 240), (30, 30, W - 60, H - 60), 10)
        pygame.display.update()

def main():
    loop()
    pygame.quit()

if __name__ == "__main__":
    main()