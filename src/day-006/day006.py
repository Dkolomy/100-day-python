# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump_barier():
#    move()
#    turn_left()
#    move()
#    turn_right()
#    move()
#    turn_right()
#    move()
#    turn_left() 

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# for i in range(6):
#     jump_barier()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# go_home = True
# while go_home:
#     jump_barier()
#     go_home = not at_goal()

# while not at_goal():
#     jump_barier()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# def jump_barier1():
#    turn_left()
#    move()
#    turn_right()
#    move()
#    turn_right()
#    move()
#    turn_left()     

# while not at_goal():
#     if front_is_clear():
#         move()
#     if wall_in_front():
#         jump_barier1()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# def jump():
#     move()
#     if not wall_on_right():
#         turn_right()
#         move()
#         turn_right()
#         move()

# while not at_goal():
#     if wall_in_front():
#         turn_left()
#     else:
#         jump()

# def jump():
#   turn_left()
#   while wall_on_right():
#     move()

#   turn_right()
#   move()
#   turn_right()

#   while front_is_clear():
#     move()
#   turn_left()

# while not at_goal():
#   if wall_in_front():
#     jump()
#   else:
#     turn_left()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json        
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while front_is_clear():
#     move()
# turn_left()
   
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

