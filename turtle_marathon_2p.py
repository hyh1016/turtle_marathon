import turtle as t
import pygame as pg
import time

thema = './thema.wav' # 테스트용 테마 송
pg.mixer.init()
pg.mixer.music.load(thema)

player = t.Turtle()
enemy = t.Turtle()
judgment = t.Turtle()
goal_x = 295
is_play = False

# 플레이어
player.shape('turtle')
player.color('blue')
player.speed(5)
player.up()

# 적 거북이
enemy.shape('turtle')
enemy.color('red')
enemy.up()
enemy.speed(5)

# 심판 거북이
judgment.shape('turtle')
judgment.color('black')
judgment.pensize(10)
judgment.speed(5)

# t(Default): for print message
t.speed(0)
t.up()
t.hideturtle()

def init():
    player.goto(-300, 200)

    enemy.goto(-300, -200)

    judgment.up()
    judgment.goto(300, -300)
    judgment.down()
    judgment.seth(90)
    judgment.forward(600)

    pg.mixer.music.play()
    message("TURTLE MARATHON", "Press [Enter] to start!")

# 이동 함수 - space bar key event와 연결
def go_1p():
    global is_play
    if is_play:
        player.forward(10)

def go_2p():
    global is_play
    if is_play:
        enemy.forward(10)

def goal_in():
    if player.position()[0] >= goal_x:
        return 1
    elif enemy.position()[0] >= goal_x:
        return 2
    else: return False

def start():
    t.clear()
    pg.mixer.music.stop()

    global is_play
    is_play = True

    while is_play:
        t.forward(1) # 이게 없으면 오류가 난다.
        is_goal = goal_in()
        if is_goal:
            who_is_winner(str(is_goal))
            is_play = False
            init()

# 심판 거북이가 누가 이겼는지 직접 말해주는 함수
def who_is_winner(winner):
    judgment_position = judgment.position()
    t.goto(judgment_position[0] - 50, judgment_position[1])
    if winner == '1':
        t.write("1P win!", False, "center", ("", 12))
    elif winner == '2':
        t.write("2P win!", False, "center", ("", 12))
    time.sleep(2)
    t.clear()

def message(m1, m2):
    t.color('blue')
    t.goto(0, 100)
    t.write(m1, False, "center",("",24, "bold"))
    t.goto(0,-100)
    t.write(m2, False, "center",("",15, "bold"))

init()
t.onkey(go_1p, 'Right')
t.onkey(go_2p, 'a')
t.onkey(start, '\n')
t.listen()
t.mainloop()