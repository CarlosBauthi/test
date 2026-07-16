from pygame import *
from time import *


back = (200, 255, 255) # fondo de juego
img_1 = "Paleta.jpeg"  # personaje
img_enemy = "Pelota.jpeg"  # enemigo



win_width = 700
win_height = 500
display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True

ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

finish = False
run = True  
while run:
    # el evento de pulsación del botón Cerrar
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        # actualizar fondo
        window.blit(background, (0, 0))

        # escribiendo texto en la pantalla
        text = font2.render("Puntaje: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        # produciendo los movimientos del objeto
        ship.update()
        monsters.update()

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            # Este ciclo se repetirá tantas veces como los monstruos sean asesinados
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        # posible derrota: hubo muchos fallos o el personaje chocó con el enemigo
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True  # derrota, se establece el fondo y ya no hay más control de objetos.
            window.blit(lose, (200, 200))

        # comprobación de victoria: ¿cuántos puntos se anotaron?
        if score >= 10:
            finish = True
            window.blit(win, (200, 200))

        display.update()
        clock.tick(FPS)