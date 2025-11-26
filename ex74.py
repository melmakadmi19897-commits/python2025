import pygame
import sys

# Inicialització de Pygame
pygame.init()

# ----------------------
# Constants del joc
# ----------------------
AMPLADA = 800
ALÇADA = 600
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
FPS = 60

# ----------------------
# Creació de la pantalla
# ----------------------
pantalla = pygame.display.set_mode((AMPLADA, ALÇADA))
pygame.display.set_caption("Arkanoid")

# ----------------------
# Carregar imatges
# ----------------------
# Assegura't de tenir les imatges al mateix directori
# Exemple: "barra.png", "pilota.png", "bloc.png"
barra_img = pygame.image.load("barra.png")
pilota_img = pygame.image.load("pilota.png")
bloc_img = pygame.image.load("bloc.png")

# ----------------------
# Classes
# ----------------------
class Barra(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = barra_img
        self.rect = self.image.get_rect(midbottom=(AMPLADA//2, ALÇADA - 30))
        self.velocitat = 7

    def update(self, direccio):
        self.rect.x += direccio * self.velocitat
        # No sortir de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > AMPLADA:
            self.rect.right = AMPLADA

class Pilota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pilota_img
        self.rect = self.image.get_rect(center=(AMPLADA//2, ALÇADA//2))
        self.velocitat = pygame.math.Vector2(5, -5)
        self.moure = False

    def update(self):
        if self.moure:
            self.rect.x += self.velocitat.x
            self.rect.y += self.velocitat.y

            # Rebot amb les parets
            if self.rect.left <= 0 or self.rect.right >= AMPLADA:
                self.velocitat.x *= -1
            if self.rect.top <= 0:
                self.velocitat.y *= -1

class Bloc(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = bloc_img
        self.rect = self.image.get_rect(topleft=pos)

# ----------------------
# Creació de sprites
# ----------------------
barra = Barra()
pilota = Pilota()

grup_barra = pygame.sprite.GroupSingle(barra)
grup_pilota = pygame.sprite.GroupSingle(pilota)
grup_blocs = pygame.sprite.Group()

# Crear blocs en una graella
for fila in range(5):
    for columna in range(10):
        bloc = Bloc((columna * (bloc_img.get_width() + 5) + 35,
                     fila * (bloc_img.get_height() + 5) + 50))
        grup_blocs.add(bloc)

# ----------------------
# Bucle principal
# ----------------------
relogi = pygame.time.Clock()
direccio = 0
jugant = True

while jugant:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugant = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direccio = -1
            elif event.key == pygame.K_RIGHT:
                direccio = 1
            elif event.key == pygame.K_SPACE:
                pilota.moure = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                direccio = 0

    # Actualitzar sprites
    grup_barra.update(direccio)
    grup_pilota.update()

    # Col·lisions pilota-barra
    if pygame.sprite.spritecollide(barra, grup_pilota, False):
        pilota.velocitat.y *= -1
        pilota.rect.bottom = barra.rect.top

    # Col·lisions pilota-blocs
    blocs_col = pygame.sprite.spritecollide(pilota, grup_blocs, True)
    if blocs_col:
        pilota.velocitat.y *= -1

    # Rebot pilota fons (game over)
    if pilota.rect.top > ALÇADA:
        print("Game Over")
        jugant = False

    # Pintar pantalla
    pantalla.fill(NEGRE)
    grup_barra.draw(pantalla)
    grup_pilota.draw(pantalla)
    grup_blocs.draw(pantalla)

    pygame.display.flip()
    relogi.tick(FPS)

pygame.quit()
sys.exit()
