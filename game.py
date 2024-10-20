import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Bird:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.velocidade = 0
        self.gravidade = 0.5

    def update(self):
        self.velocidade += self.gravidade
        self.y += self.velocidade

    def flap(self):
        self.velocidade = -10

class Cano:
    def __init__(self):
        self.x = WIDTH
        self.y = HEIGHT / 2
        self.velocidade = -5
        self.largura = 50
        self.altura = 200

    def update(self):
        self.x += self.velocidade

class Jogo:
    def __init__(self):
        self.bird = Bird()
        self.cano = Cano()
        self.pontos = 0
        self.start = False
        self.game_over = False

    def update(self):
        if self.start:
            self.bird.update()
            self.cano.update()

            if self.bird.y > HEIGHT - 20:
                self.game_over = True

            if self.cano.x < self.bird.x < self.cano.x + self.cano.largura and self.bird.y < self.cano.altura:
                self.game_over = True

            if self.cano.x < -self.cano.largura:
                self.cano.x = WIDTH
                self.pontos += 1

    def draw(self):
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(BLACK)

        if not self.start:
            font = pygame.font.Font(None, 36)
            text = font.render("Pressione o botão para iniciar", True, WHITE)
            screen.blit(text, (WIDTH / 2 - 100, HEIGHT / 2 - 18))

            pygame.draw.rect(screen, WHITE, (WIDTH / 2 - 50, HEIGHT / 2 + 20, 100, 50))
            font = pygame.font.Font(None, 24)
            text = font.render("Iniciar", True, BLACK)
            screen.blit(text, (WIDTH / 2 - 40, HEIGHT / 2 + 30))

        elif not self.game_over:
            pygame.draw.rect(screen, WHITE, (self.bird.x, self.bird.y, 20, 20))
            pygame.draw.rect(screen, WHITE, (self.cano.x, self.cano.y, self.cano.largura, self.cano.altura))

            font = pygame.font.Font(None, 36)
            text = font.render(str(self.pontos), True, WHITE)
            screen.blit(text, (WIDTH / 2, 20))

        else:
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over!", True, WHITE)
            screen.blit(text, (WIDTH / 2 - 50, HEIGHT / 2 - 18))

            font = pygame.font.Font(None, 24)
            text = font.render("Pontuação: " + str(self.pontos), True, WHITE)
            screen.blit(text, (WIDTH / 2 - 50, HEIGHT / 2 + 20))

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.start:
                    if WIDTH / 2 - 50 < event.pos[0] < WIDTH / 2 + 50 and HEIGHT / 2 + 20 < event.pos[1] < HEIGHT / 2 + 70:
                        self.start = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()

jogo = Jogo()
clock = pygame.time.Clock()

while True:
    jogo.handle_events
