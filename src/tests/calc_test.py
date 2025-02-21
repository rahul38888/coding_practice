

def do_sum(a, b):

    if a == None:
        return b
    elif b == None:
        return a
    else:
        return a + b

def do_sum_new(a, b):
    if a == None:
        a = 0
    if b == None:
        b = 0

    return a + b


test_data = {
    (1, 2, 0): 3,
    (None, 2, 1): 2,
    (1, None, 2): 1,
    (0, 2, 3): 2,
    (1, 0, 4): 1,
    (-1, 1, 5): 0,
    (-1, -1, 6): -2
}

# [(1, 2), 3]
for k in test_data.items():
    a, b, u = k[0][0], k[0][1], k[0][2]
    v = k[1]

    print(a, b, v)
    if u == 0:
         assert do_sum(a, b) == v
