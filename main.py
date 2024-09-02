maze = [
    ["🐭", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
    ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
    ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
    ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
    ["⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬛️"],
    ["⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "🚪"]
]

mickey = [0, 0]

while True: 
    
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
            print("Direccion no valida.")