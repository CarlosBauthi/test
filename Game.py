import pygame
pygame.init()

back = (200, 255, 255) # fondo de juego
img_1 = "Paleta.jpeg"  # personaje
img_enemy = "Pelota.jpeg"  # enemigo

# clase padre para otros objetos
class GameSprite(pygame.sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        pygame.sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # método para controlar el objeto con las flechas del teclado
    def update1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed


win_width = 600
win_height = 500
pygame.display.set_caption("Ping Pong")
window =pygame.display.set_mode((win_width, win_height))
window.fill(back)

clock = pygame.time.Clock()
FPS = 60
game = True

raque1 = Player(img_1, 30, win_height - 100, 50, 150, 4)
raque2 = Player(img_1, 520, win_height - 100, 50, 150, 4)
bola = GameSprite(img_enemy, 200, 200, 50, 50, 4)

finish = False
game = True
x = 3
y = 3

pygame.font.init()
font1 = pygame.font.Font(None, 35)
lose1 = font1.render(
    'PLAYER 1 PIERDE!', True, ( 180, 0, 0)    
)
lose2 = font1.render(
    'PLAYER 2 PIERDE!', True, ( 180, 0, 0)    
)

while game:
    # el evento de pulsación del botón Cerrar
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if finish != True:
        bola.rect.x += x
        bola.rect.y += y

        window.fill(back)
        raque1.update1()
        raque2.update2()

        if bola.rect.y > win_height-50 or bola.rect.y < 0:
            y *= -1

        if pygame.sprite.collide_rect(raque1, bola) or pygame.sprite.collide_rect(raque2, bola):
            x *= -1
            
        if bola.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = False
        
        if bola.rect.x > 550:
            finish = True
            window.blit(lose2, (200, 200))
            game = False

        raque1.reset()
        raque2.reset()
        bola.reset()
    pygame.display.update()
    clock.tick(FPS)
