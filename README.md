Escape the Coder - Pygame Maze Game
This is a simple game implemented in Pygame called "Escape the Coder." The player, represented by a white circle, must navigate through a randomly generated maze to reach the exit. The maze is created using a maze generation algorithm.

Code Description
The code uses Pygame for creating the graphical interface and handling events. Here's a summary of key classes and components:

Maze Class
Random Generation: Uses the maze generation algorithm based on the "backtracking" approach to create a random maze.
Rendering: Draws maze cells on the screen, using colors to represent walls (black), free spaces (white), and the exit (green).
Collisions: Checks if a specific position in the maze corresponds to a wall.
Coder Class
Random Movement: The coder moves randomly in any allowed direction, avoiding collisions with maze walls.
Rendering: Draws the coder as a white circle on the screen.
Main Game Loop
Event Handling: Manages game events, such as exiting the game.
Timer: Records the total time it takes for the player to escape the maze.
Continuous Rendering: Updates the screen and shows changes in each iteration of the main loop.
Game Instructions
The game starts with the coder in the top-left corner of the maze.
The player must navigate through the maze, avoiding walls.
The goal is to reach the exit in the bottom-right corner of the maze.
The total time the player takes to escape the maze is recorded.
Enjoy escaping the coder's maze!

Note: This game could benefit from improved gameplay and graphics. If you have suggestions or want to make enhancements, feel free to do so. Enjoy the code!

MIT License

Copyright (c) [Año] [Nombre del titular del copyright]

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y archivos de documentación asociados (el "Software"), para tratar
el Software sin restricción, incluidos, entre otros, los derechos de uso, copia, modificación,
fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software y permitir
a las personas a las que se les proporcione el Software hacer lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permisos se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA,
INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN PROPÓSITO PARTICULAR
Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES
DE NINGÚN RECLAMO, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO,
DE LOS O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE.
