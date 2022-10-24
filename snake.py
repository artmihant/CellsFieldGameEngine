from game import Game, Color

game = Game(15, 15)
game.cellsize = 50

game.state.interval = 100

game.add_cell('head', color=Color.GREEN)
game.add_cell('apple', color=Color.RED)
game.add_cell('tail', color=Color.GRASS)


def drowfield(state):

    state.field[...] = state.cell['empty']
    state.field[state.apple] = state.cell['apple']
    state.field[state.head] = state.cell['head']
    for segment in state.tail:
        state.field[segment] = state.cell['tail']
    return state


def getapple(state):
    besides = [state.head, *state.tail]
    while True:
        apple_coord = state.randomcell()
        if apple_coord not in besides:
            break
    return apple_coord


def start(state):
    state.head = state.width // 2, state.height // 2
    state.tail = []
    state.apple = getapple(state)
    state.course = 'up'
    state.gameover = False
    return drowfield(state)


def keydown(state, key):
    if key in ('up', 'down') and state.course in ('left', 'right') or \
            key in ('left', 'right') and state.course in ('up', 'down'):
        state.course = key
    elif key == 'pagedown':
        state.interval *= 2
    elif key == 'pageup':
        state.interval //= 2
    return state

def turn(state):
    if state.gameover:
        return state

    h = state.head
    if state.course == 'up':
        h = h[0], h[1] - 1
    elif state.course == 'down':
        h = h[0], h[1] + 1
    elif state.course == 'left':
        h = h[0] - 1, h[1]
    elif state.course == 'right':
        h = h[0] + 1, h[1]

    h = h[0] % state.width, h[1] % state.height

    state.tail.append(state.head)

    if h == state.apple:
        state.apple = getapple(state)
    else:
        state.tail = state.tail[1:]

    if h in state.tail:
        state.gameover = True

    state.head = h

    return drowfield(state)



game.start = start
game.turn = turn
game.keydown = keydown

if __name__ == '__main__':
    game.play()
