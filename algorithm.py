def houses_disp(d, places2):
    places = {}
    k = 0
    for i in range(places2[3]):
        places[i] = 3
        k = i
    for j in range(k, places2[4]):
        places[j] = 4
    first = []
    second = []
    third = []
    fourth = []
    x = 1
    for i in range(len(d["name"])):
        if d["gender"][i] == "Ж" or d["gender"][i] == "ж":
            fourth.append(d["name"][i])
        elif d["age"][i] >= 16:
            first.append(d["name"][i])
        elif d["age"][i] >= 14:
            second.append(d["name"][i])
        else:
            third.append(d["name"][i])
    h = {}
    if len(fourth) > 0:
        for i in range(len(fourth)):
            if x not in h.keys():
                h[x] = fourth[i] + " "
            else:
                h[x] += fourth[i] + " "
            places[x] -= 1
            if places[x] == 0:
                x += 1
                while x not in places.keys():
                    x += 1
        x += 1
        while x not in places.keys():
            x += 1
    for i in range(len(third)):
        if x not in h.keys():
            h[x] = third[i] + " "
        else:
            h[x] += third[i] + " "
        places[x] -= 1
        if places[x] == 0:
            x += 1
            while x not in places.keys():
                x += 1
    for i in range(len(second)):
        if x not in h.keys():
            h[x] = second[i] + " "
        else:
            h[x] += second[i] + " "
            places[x] -= 1
        if places[x] == 0:
            x += 1
            while x not in places.keys():
                x += 1
    for i in range(len(first)):
        if x not in h.keys():
            h[x] = first[i] + " "
        else:
            h[x] += first[i] + " "
            places[x] -= 1
        if places[x] == 0:
            x += 1
            while x not in places.keys():
                x += 1
    return output(h)


def output(d):
    x = 1
    string = ""
    tmp = ""
    for i in d.keys():
        tmp += "Дом " + str(x) + ':'
        string += tmp + "\n" + d[i] + "\n"
        x += 1
        tmp = ""
    return string


def output1(d):
    x = 1
    string = ""
    for i in range(len(d)):
        tmp = "Команда " + str(x) + ':'
        string += tmp + "\n"
        for j in range(len(d[i])):
            string += str(d[i][j]) + "\n"
        x += 1
    return string


def activity(d, n):
    end = []
    one = []
    two = []
    three = []
    x = 0
    for i in range(len(d["name"])):
        if d["age"][i] >= 16:
            one.append(d["name"][i])
        elif d["age"][i] >= 14:
            two.append(d["name"][i])
        else:
            three.append(d["name"][i])
    for i in range(n):
        end.append([])
    while 1:
        try:
            minimum = 0
            for i in range(n):
                if len(end[i]) < len(end[minimum]):
                    minimum = i
            end[minimum].append(one[x])
            x += 1
        except IndexError:
            break
    x = 0
    while 1:
        try:
            minimum = 0
            for i in range(n):
                if len(end[i]) < len(end[minimum]):
                    minimum = i
            end[minimum].append(two[x])
            x += 1
        except IndexError:
            break
    x = 0
    while 1:
        try:
            minimum = 0
            for i in range(n):
                if len(end[i]) < len(end[minimum]):
                    minimum = i
            end[minimum].append(three[x])
            x += 1
        except IndexError:
            break

    return output1(end)
