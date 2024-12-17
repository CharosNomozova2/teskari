def generate_spiral_matrix(size, direction="clockwise"):
    matrix = [[0] * size for _ in range(size)]  # Boshlang'ich bo'sh matritsa
    num = 1  # To'ldiriladigan son
    top, bottom, left, right = 0, size - 1, 0, size - 1

    if direction == "counterclockwise":
        while num <= size * size:
            # Yuqoridan pastga
            for i in range(top, bottom + 1):
                if num > size * size:
                    break
                matrix[i][left] = num
                num += 1
            left += 1

            # Chapdan o'ngga
            for i in range(left, right + 1):
                if num > size * size:
                    break
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            # Pastdan yuqoriga
            for i in range(bottom, top - 1, -1):
                if num > size * size:
                    break
                matrix[i][right] = num
                num += 1
            right -= 1

            # O'ngdan chapga
            for i in range(right, left - 1, -1):
                if num > size * size:
                    break
                matrix[top][i] = num
                num += 1
            top += 1

    return matrix


# Matritsa o'lchamini aniqlaymiz
size = int(input("Matritsa o'lchamini kiriting: "))
counter_clockwise_matrix = generate_spiral_matrix(size, "counterclockwise")

# Matritsani chiroyli chiqaramiz
print("Soat strelkasiga qarama-qarshi:")
for row in counter_clockwise_matrix:
    print(row)
