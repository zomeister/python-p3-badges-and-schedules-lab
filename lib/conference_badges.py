def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    return [f"Hello, {names[num]}! You'll be assigned to room {num+1}!" for num in range(len(names))]
    # i = 0
    # room_strings = []
    
    # while i < len(names):
    #     room_strings.append(f"Hello, {names[i]}! You'll be assigned to room {i+1}!")
    #     i += 1
    # return room_strings

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for assignment in assign_rooms(names):
        print(assignment)
    # return None
