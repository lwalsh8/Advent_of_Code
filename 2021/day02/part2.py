
def calculate_position(input_file):
    pos = [0, 0, 0]  # Depth, distance, aim
    with open(input_file, "r") as f:
        for line in f:
            direction, magnitude = line.split()
            if direction == 'forward':
                pos[1] += int(magnitude)
                pos[0] += int(pos[2]) * int(magnitude)
            elif direction == 'down':
                pos[2] += int(magnitude)
            elif direction == 'up':
                pos[2] -= int(magnitude)
    return pos


def main():
    pos = calculate_position('input.txt')
    print(f'Final position is {pos}')
    print(f'Product of final position coordinates: {int(pos[0]) * int(pos[1])}')


if __name__ == "__main__":
    main()