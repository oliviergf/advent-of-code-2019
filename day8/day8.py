inputs = open("day8/input.txt", "r")
pixels = list(inputs.readline())

layers = []
row_size = 25
col_size = 6


def part2(layers, row_size, col_size):
    message = []
    for i in range(col_size):
        row = []
        for j in range(row_size):
            pixel = "z"
            for l in reversed(range(len(layers))):
                if layers[l][i][j] == "1":
                    pixel = "x"
                if layers[l][i][j] == "0":
                    pixel = "."
            row.append(pixel)
        message.append(row)

    for i in range(col_size):
        for j in range(row_size):
            print(message[i][j], end=" ")
        print()


def part1(pixels, layers, row_size, col_size):
    size_image = row_size * col_size
    layers_zeros = []
    pixel_count = 0
    while pixel_count != len(pixels) - 1:
        image = []
        zeroes = 0
        for j in range(col_size):
            row = []
            for i in range(row_size):
                row.append(pixels[pixel_count])
                if pixels[pixel_count] == "0":
                    zeroes += 1
                pixel_count += 1
            image.append(row)
        layers.append(image)
        layers_zeros.append(zeroes)

    max_zeroes = row_size * col_size + 1
    fewest_layer = -1
    for i in range(len(layers)):
        if layers_zeros[i] < max_zeroes:
            max_zeroes = layers_zeros[i]
            fewest_layer = i

    ones = 0
    twos = 0
    for i in range(col_size):
        for j in range(row_size):
            if layers[fewest_layer][i][j] == "1":
                ones += 1
            if layers[fewest_layer][i][j] == "2":
                twos += 1
    print(str(ones * twos))


part1(pixels, layers, row_size, col_size)
part2(layers, row_size, col_size)
