import sys

num_steps = int(sys.argv[1])

probel = ' '
stupen = '#'

for i in range(num_steps):
    print(probel * (num_steps-i-1)+stupen*(i+1))