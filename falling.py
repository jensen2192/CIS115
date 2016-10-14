def main():
    for time in range (1,11):
        distance = falling_distance(time)
        print(time, "seconds: ", format(distance, ',.1f'))

def falling_distance(time):
    distance = 0.5 * 9.8 * time * time
    return distance

main()