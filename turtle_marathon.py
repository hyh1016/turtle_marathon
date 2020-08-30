import turtle as t
player = t
goal_x = 295
enemy = t.Turtle()
judgment = t.Turtle()

def init():
    player.shape('turtle')
    player.color('BLUE')
    player.up()
    player.goto(-300, 200)

    enemy.shape('turtle')
    enemy.color('RED')
    enemy.up()
    enemy.goto(-300, -200)

    judgment.shape('turtle')
    judgment.color('BLACK')
    judgment.pensize(10)
    judgment.up()
    judgment.goto(300, -300)
    judgment.down()
    judgment.left(90)
    judgment.forward(600)

def go():
    player.forward(30)

def touch():
    if player.position()[0] >= goal_x:
        print('You Win!')
    elif enemy.position()[0] >= goal_x:
        print('You Lose!')
    else: return False
    return True

init()
t.onkey(go, 'space')
t.listen()

while True:
    enemy.forward(1)
    if touch():
        break

t.exitonclick()