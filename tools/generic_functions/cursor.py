def clear_up(times: int = 1, lines: int = 0):
    space = " " * lines
    cursor_up = f"\033[F {space}"
    print(cursor_up * times + "\033[F")
