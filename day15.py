

def day15p1():
    print("Part 1")
    input = [2, 0, 1, 7, 4, 14, 18]

    turn = len(input)
    number = input[-1]
    storage = {}
    for i, v in enumerate(input):
        storage[v] = i + 1


    while turn < 2020:
        if not storage.get(number, None):
            storage[number] = turn
            number = 0
            turn += 1
        else:
            last_seen = storage[number]
            storage[number] = turn
            number = turn - last_seen
            turn += 1

    print(number)

def day15p2():
    print("Part 2")
    input = [2, 0, 1, 7, 4, 14, 18]

    turn = len(input)
    number = input[-1]
    storage = {}
    for i, v in enumerate(input):
        storage[v] = i + 1


    while turn < 30000000:
        if not storage.get(number, None):
            storage[number] = turn
            number = 0
            turn += 1
        else:
            last_seen = storage[number]
            storage[number] = turn
            number = turn - last_seen
            turn += 1

    print(number)

day15p1()

day15p2()
