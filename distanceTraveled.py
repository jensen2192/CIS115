speed = int(input('What is the speed of the vehicle in mph?:'))
time = int(input('How many hours has it traveled?:'))

print('Hour\tDistance Traveled')
print('-------------------------')

for time in range(time + 1):
    distance = speed * time
    print(time, '\t', distance)
