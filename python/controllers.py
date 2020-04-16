from inputs import devices, WIN
import json
import time
import turtle
from dataclasses import dataclass
from threading import Timer

def event_to_json(event):
    event_dict = {
        "device": str(event.device),
        "code": event.code,
        "type": event.ev_type,
        "state": event.state,
        "timestamp": time.asctime((time.localtime(event.timestamp)))
    }
    return json.dumps(event_dict)

def event_to_basicjson(event):
    event_dict = {
        "code": event.code,
    }
    return json.dumps(event_dict)

def convert_event(event):
    if event.ev_type == "Key":
        if event.code == "BTN_SOUTH":
            event.code = "A"
        if event.code == "BTN_EAST":
            event.code = "B"
        if event.code == "BTN_NORTH":
            event.code = "Y"
        if event.code == "BTN_WEST":
            event.code = "X"
        if event.code == "BTN_TL":
            event.code = "LB"
        if event.code == "BTN_TR":
            event.code = "RB"
        if event.code == "BTN_SELECT":
            event.code = "START"
        if event.code == "BTN_START":
            event.code = "BACK"
        return event
    if event.ev_type == "Absolute":
        if event.code == "ABS_HAT0Y":
            if event.state == -1:
                event.code = "UP"
            if event.state == 1:
                event.code = "DOWN"
            if event.state == 0:
                event.code = "YMIDDLE"
            return event
        if event.code == "ABS_HAT0X":
            if event.state == -1:
                event.code = "LEFT"
            if event.state == 1:
                event.code = "RIGHT"
            if event.state == 0:
                event.code = "XMIDDLE"
            return event
    return None

@dataclass
class GameState:
    speed: int = 10
    angle: int = 30
    forwardPressed: bool = False
    rightPressed: bool = False
    leftPressed: bool = False
    t = None
    xbox_controller = None

def update_turtle(state, event):
    print("update_turtle with " + str(event))
    if event.code == "UP":
        state.forwardPressed = True
    if event.code == "YMIDDLE":
        state.forwardPressed = False
    elif event.code == "LEFT":
        state.leftPressed = True
    elif event.code == "RIGHT":
        state.rightPressed = True
    if event.code == "XMIDDLE":
        state.rightPressed = False
        state.leftPressed = False
    elif event.code == "RB":
        state.speed = state.speed + 10
    elif event.code == "LB":
        state.speed = state.speed - 10
    elif event.code == "B":    
        state.t.penup()
    elif event.code == "A":
        state.t.pendown()
    print (state)

def draw_turtle(state):
    print("draw_turtle")
    if state.rightPressed == True:
        state.t.rt(state.angle)
    if state.leftPressed == True:
        state.t.lt(state.angle)
    if state.forwardPressed == True:
        state.t.forward(state.speed)

xbox_controller = None

# Find the xbox controller
for device in devices:
    if device.name == "Microsoft X-Box 360 pad":
        print("We found an X-Box controller. Using this!")
        xbox_controller = device
    else:
        print("Found " + device.name + ". Skipping!")    

if xbox_controller == None:
    exit("You need to plug in an Xbox 360 controller. Exiting")
else:
    print ("Found an xbox controller. Continuing on.")

state = GameState()
state.t = turtle.Pen()
state.t.speed = 0
state.xbox_controller = xbox_controller
print(dir(xbox_controller))

def process_game_loop(state):
    print("processing game loop")
    if WIN:
        state.xbox_controller._GamePad__check_state()
    events = state.xbox_controller._do_iter()
    if events is not None:
        for event in events:
            event = convert_event(event)
            if event is not None:
                update_turtle(state, event)
    draw_turtle(state)
    print("scheduling loop")
    t = Timer(0.1, process_game_loop, [state])
    t.setDaemon(True)
    t.start()

t = Timer(0.1, process_game_loop, [state])
t.setDaemon(True)
t.start()

turtle.mainloop()