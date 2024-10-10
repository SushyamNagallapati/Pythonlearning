def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    
    while wall_on_right():
           turn_right()
            
    turn_right()
    move()
    turn_right()
    while front_is_clear():
           move()
    turn_left()

while not at_goal():
    if wall_on_right() and wall_in_front():
        turn_left()
    elif right_is_clear():
        turn_right()
