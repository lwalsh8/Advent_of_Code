
def read_input(input_file):
    pos = [0,0]
    with open(input_file, "r") as f:
        for line in f:
            dir, mag = line.split()
            if dir == 'forward':
                pos[1] += int(mag)
            elif dir == 'down':
                pos[0] += int(mag)
            elif dir == 'up':
                pos[0] -= int(mag)
            print(dir, mag, pos)

    return pos


def main():
    pos = read_input('input.txt')
    print(f'Final position is {pos}')

    print(f'Product of final position coordinates: {int(pos[0]) * int(pos[1])}')


if __name__ == "__main__":
    main()