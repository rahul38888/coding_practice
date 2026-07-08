def robot_in_circle(m):
    # 0:straight, 1:left, 2:back, 3:right
    facing = 1
    y_steps = 0
    x_steps = 0
    for move in m:
        if move is 'L':
            facing = (facing + 1) % 4
        elif move is 'R':
            facing = (facing - 1) % 4
        else:
            if facing is 0:
                y_steps += 1
            elif facing is 1:
                x_steps -= 1
            elif facing is 2:
                y_steps -= 1
            else:
                x_steps += 1

    if y_steps is 0 and x_steps is 0:
        return 'Circular'
    else:
        return 'Not Circular'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        m = input()
        print(robot_in_circle(m))
