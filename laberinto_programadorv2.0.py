import pygame
import sys
import random
import time

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Definir tamaño de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laberinto del Programador")

# Tamaño de celda del laberinto
CELL_SIZE = 40

# Clase Laberinto
class Laberinto:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.generar_laberinto()

    def generar_laberinto(self):
        stack = [(0, 0)]
        visited = set()
        while stack:
            current = stack[-1]
            visited.add(current)
            neighbors = [(current[0] + 2, current[1]), (current[0] - 2, current[1]),
                         (current[0], current[1] + 2), (current[0], current[1] - 2)]
            unvisited_neighbors = [neighbor for neighbor in neighbors if neighbor not in visited and
                                   0 <= neighbor[0] < self.rows and 0 <= neighbor[1] < self.cols]
            if unvisited_neighbors:
                chosen_neighbor = random.choice(unvisited_neighbors)
                wall = ((current[0] + chosen_neighbor[0]) // 2, (current[1] + chosen_neighbor[1]) // 2)
                self.grid[wall[0]][wall[1]] = 1
                self.grid[chosen_neighbor[0]][chosen_neighbor[1]] = 0  # Crear un espacio para garantizar un camino
                stack.append(chosen_neighbor)
            else:
                stack.pop()

        # Establecer la salida en la esquina opuesta del laberinto
        self.grid[self.rows - 1][self.cols - 1] = 0

    def renderizar(self):
        for row in range(self.rows):
            for col in range(self.cols):
                color = WHITE if self.grid[row][col] else BLACK
                pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                if row == self.rows - 1 and col == self.cols - 1:
                    pygame.draw.rect(screen, GREEN, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def es_salida(self, x, y):
        return x >= (self.cols - 1) * CELL_SIZE and y >= (self.rows - 1) * CELL_SIZE

    def colision_con_pared(self, x, y):
        row = y // CELL_SIZE
        col = x // CELL_SIZE
        return self.grid[row][col] == 1

# Clase Programador
class Programador:
    def __init__(self, laberinto):
        self.x = 0
        self.y = 0
        self.laberinto = laberinto
        self.tiempo_inicio = None
        self.tiempo_final = None

    def mover(self):
        possible_moves = [(0, -CELL_SIZE), (0, CELL_SIZE), (-CELL_SIZE, 0), (CELL_SIZE, 0)]
        random.shuffle(possible_moves)

        for dx, dy in possible_moves:
            new_x = max(0, min(self.x + dx, WIDTH - CELL_SIZE))
            new_y = max(0, min(self.y + dy, HEIGHT - CELL_SIZE))

            # Verificar colisiones con las paredes
            if not self.laberinto.colision_con_pared(new_x, new_y):
                self.x = new_x
                self.y = new_y
                break

    def renderizar(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), 10)

# Instanciar objetos
laberinto = Laberinto(HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE)
programador = Programador(laberinto)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar pantalla
    screen.fill(BLACK)

    # Renderizar laberinto y programador
    laberinto.renderizar()
    programador.renderizar()

    # Iniciar el temporizador cuando el jugador comienza a moverse
    if programador.tiempo_inicio is None and (programador.x != 0 or programador.y != 0):
        programador.tiempo_inicio = time.time()

    # Mover al programador
    programador.mover()

    # Verificar si el jugador alcanzó la salida
    if laberinto.es_salida(programador.x, programador.y):
        programador.tiempo_final = time.time()
        tiempo_total = programador.tiempo_final - programador.tiempo_inicio
        print(f"¡Has escapado del laberinto en {tiempo_total:.2f} segundos!")
        laberinto.generar_laberinto()  # Generar nuevo laberinto
        programador.x = 0  # Reiniciar posición del programador
        programador.y = 0
        programador.tiempo_inicio = None
        programador.tiempo_final = None

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(60)
