from game import Game, Color

game = Game(100, 100)
game.cellsize = 10


game.state.interval = 100

game.add_cell('live', color=Color.GREEN)


def start(state):
    for i in range(state.width*state.height//2):
        state.field[state.randomcell()] = state.cell['live']

    return state

def keydown(state, key):
    if key == 'pagedown':
        state.interval *= 2
    elif key == 'pageup':
        state.interval //= 2
        if state.interval == 0:
            state.interval = 1
    return state


def turn(state):
    field = state.field.copy()
    for index in state.range:
        i,j = index

        lt = (i - 1) % state.width
        rt = (i + 1) % state.width
        up = (j - 1) % state.height
        dn = (j + 1) % state.height

        s = sum([
            field[lt,up],
            field[lt, j],
            field[lt,dn],
            field[i, up],
            field[i, dn],
            field[rt,up],
            field[rt, j],
            field[rt,dn],
        ])

        if s == 3 and field[index] == 0:
            state.field[index] = 1
        elif s != 2 and field[index] == 1:
            state.field[index] = 0

    return state

def click(state, pos):
    state.field[pos] = (state.field[pos] + 1) % 2
    return state


game.start = start
game.turn = turn
game.keydown = keydown
game.click = click

if __name__ == '__main__':
    game.play()
