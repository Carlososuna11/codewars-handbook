def rgb(r, g, b):
    return f"{hex(r if r <= 255 else 255)[2:] if r > 15 else f'0{hex(r)[2:] if r >= 0 else 0}'}{hex(g if g <= 255 else 255)[2:] if g > 15 else f'0{hex(g)[2:] if g >= 0 else 0}'}{hex(b if b <= 255 else 255)[2:] if b>15 else f'0{hex(b)[2:] if b >= 0 else 0}'}".upper()
    