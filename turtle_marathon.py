import turtle as t
player = t
goal_x = 295
enemy = t.Turtle()
judgment = t.Turtle()

def init():
    # 플레이어
    player.shape('turtle')
    player.color('BLUE')
    player.up()
    player.goto(-300, 200)

    # 적 거북이
    enemy.shape('turtle')
    enemy.color('RED')
    enemy.up()
    enemy.goto(-300, -200)

    # 심판 거북이
    judgment.shape('turtle')
    judgment.color('BLACK')
    judgment.pensize(10)
    judgment.up()
    judgment.goto(300, -300)
    judgment.down()
    judgment.left(90)
    judgment.forward(600)
    judgment.left(90)

# 이동 함수 - space bar key event와 연결
def go():
    player.forward(30) # 플레이어의 이동 속도

def goal_in():
    if player.position()[0] >= goal_x:
        print('You Win!')
    elif enemy.position()[0] >= goal_x:
        print('You Lose!')
    else: return False
    return True

# 심판 거북이가 누가 이겼는지 직접 말해주는 함수
def message():
    pass

init()
t.onkey(go, 'space')
t.listen()

while True:
    enemy.forward(1)
    if goal_in():
        break

t.exitonclick()