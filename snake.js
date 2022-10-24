
let game = new Game({
    size: [15,15],
    border: 'torus',
    cells:{
        empty: {color: Color.WHITE}
    },
    figures:{
        head: {color:Color.GREEN},
        apple: {color:Color.RED},
        tail: {color:Color.BLUE}
    }

})

game.field.paint('empty', [0,0], game.size)

function start(state, field){
    state.head = new field.figure('head')
    state.head.move([7,7])
    state.head.rotate('up')

    state.tail = []

    state.apple = new field.figure('apple')
    state.apple.move(
        field.filter(cell => !cell.figure).random().coord
    )
}

function turn(state, field){

    let shift
    switch(state.head.direction){
        case 'up':
            shift = [-1,0]
            break
        case 'down':
            shift = [1,0]
            break
        case 'left':
            shift = [0,-1]
            break
        case 'right':
            shift = [0,1]
            break
    }
    let head_position = state.head.position

    head_position.add(shift)

    if(head_position.eq(state.apple.position) ){

    }else{
        state.tail.forEach(segment => {
            if(segment.position.eq()){

            }
        })
        if head_coord

    }



    сдвигаем голову по курсу
    если голова пересекает яблоко, учелививаем хвост на прежние координаты головы
    иначе меняем хвост на прежние координаты
    если голова пересекает хвост, проиграли

}

export default {


}