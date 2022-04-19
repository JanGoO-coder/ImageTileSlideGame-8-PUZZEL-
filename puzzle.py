import pygame, random

class Puzzle:
    def __init__(self):
        self.correct_sequence = [[{} for i in range(3)] for j in range(3)]
        self.current_sequence = [[{} for i in range(3)] for j in range(3)]

        self.generate_correct_sequence()
        self.generate_current_sequence()

        x, y = self.get_empty_position()
        self.current_sequence[x][y]["image"].set_alpha(0)

    def auto_solve(self):
        for i in range(3):
            for j in range(3):
                self.current_sequence[i][j] = self.correct_sequence[i][j]

    def generate_correct_sequence(self):
        for i in range(3):
            for j in range(3):
                image = pygame.image.load("./images/output/output_" + str(i) + str(j) + ".jpg")
                self.correct_sequence[i][j] = {
                    "image": image,
                    "index": i*3 + j,
                }

    def generate_current_sequence(self):
        for i in range(3):
            for j in range(3):
                self.current_sequence[i][j] = self.correct_sequence[i][j]
        
        # shuffle the sequence
        for i in range(3):
            for j in range(3):
                index = random.randint(0, 2)
                self.current_sequence[i][j], self.current_sequence[i][index] = self.current_sequence[i][index], self.current_sequence[i][j]
                index = random.randint(0, 2)
                self.current_sequence[j][i], self.current_sequence[index][i] = self.current_sequence[index][i], self.current_sequence[j][i]

    def get_empty_position(self):
        for i in range(3):
            for j in range(3):
                if self.current_sequence[i][j]["index"] == 8:
                    return (i, j)
        return None

    def swap_with_empty(self, position):
        i, j = position
        x, y = self.get_empty_position()
        self.current_sequence[i][j], self.current_sequence[x][y] = self.current_sequence[x][y], self.current_sequence[i][j]

    def is_correct(self):
        for i in range(3):
            for j in range(3):
                if self.current_sequence[i][j]["index"] != self.correct_sequence[i][j]["index"]:
                    return False
        return True

    def move_up(self):
        x, y = self.get_empty_position()
        if y > 0:
            self.swap_with_empty((x, y - 1))

    def move_down(self):
        x, y = self.get_empty_position()
        if y < 2:
            self.swap_with_empty((x, y + 1))

    def move_left(self):
        x, y = self.get_empty_position()
        if x > 0:
            self.swap_with_empty((x - 1, y))

    def move_right(self):
        x, y = self.get_empty_position()
        if x < 2:
            self.swap_with_empty((x + 1, y))

    def draw(self, window, W, H, C):
        for i in range(3):
            for j in range(3):
                if not self.is_correct():
                    window.blit(self.current_sequence[i][j]["image"], (C[0]*i + 30, C[1]*j + 30))
                    pygame.draw.rect(window, (100, 100, 200), (C[0]*i + 30, C[1]*j + 30, C[0], C[1]), 5)
                    # pygame.draw.rect(window, (200, 200, 240), (C[0]*i + 30, C[1]*j + 30, C[0], C[1]), 5)
                else:
                    self.current_sequence[i][j]["image"].set_alpha(255)
                    window.blit(self.correct_sequence[i][j]["image"], (C[0]*i + 30, C[1]*j + 30))