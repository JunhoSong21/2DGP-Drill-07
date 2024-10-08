from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    
    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5


    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class BigBall:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(50, 750), 599
        self.speed = random.randint(1, 7)

    def update(self):
        if(self.y > 60):
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

class SmallBall:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(50, 750), 599
        self.speed = random.randint(1, 7)

    def update(self):
        if(self.y > 60):
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global boy
    global small
    global big
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    bigballcount = random.randint(1, 19)

    big = [BigBall() for i in range(bigballcount + 1)]
    world += big

    small = [BigBall() for i in range(21 - bigballcount)]
    world += small

running = True

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    # game logic
    handle_events()
    update_world() # 상호작용을 시뮬레이션
    render_world() # 결과 출력
    delay(0.05)

# finalization code
close_canvas()