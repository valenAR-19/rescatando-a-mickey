maze = [
    ["🐭", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
    ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
    ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
    ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
    ["⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬛️"],
    ["⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "🚪"]
]

def print_maze(maze):
    for row in maze:
        print(" ".join(row))
    print()

mickey = [0, 0]

while True: 
    
    print_maze(maze)
    
    print("¿Hacia donde se mueve Mickey?")
    print("[w] arriba")
    print("[s] abajo")
    print("[a] izquierda")
    print("[d] derecha")
    direction = input("Direccion: ")
    
    current_row, current_column = mickey
    new_row, new_column = current_row, current_column
    
    match direction:
        case "w":
            new_row = current_row -1
        case "s":
            new_row = current_row + 1
        case "a":
            new_column = current_column - 1
        case "d":
            new_column = current_column - 1
        case _:
            print("Direccion no valida.\n")
            continue
        
    if new_row < 0 or new_row > 5 or new_column < 0 or new_column > 5:
        print("No puedes desplazarte fuera del laberinto.\n")
        continue
    else:
        if maze[new_row][new_column] == "⬛️":
            print("¡En esa dirección hay un obstáculo!\n")
            continue
        elif maze[new_row][new_column] == "🚪":
            print("¡Has encontrado la salida!")
            maze[current_row][current_column] = "⬜️"
            maze[new_row][new_column] = "🐭"
            print_maze()
            break
        else:
            maze[current_row][current_column] = "⬜️"
            maze[new_row][new_column] = "🐭"
            mickey = [new_row, new_column]
            
            
    