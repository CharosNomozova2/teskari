def spiral_matrix(n):
    # Bo'sh n x n matritsa yaratamiz
    matrix = [[0] * n for _ in range(n)]

    # Boshlang'ich qiymatlar
    num = 1  # Raqamlarni boshlash
    top, bottom, left, right = 0, n - 1, 0, n - 1  # Chegaralar

    while top <= bottom and left <= right:
        # Yuqoridan o'ngga
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # O'ngdan pastga
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Pastdan chapga
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Chapdan yuqoriga
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix


# Matritsani chop etish funksiyasi
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# Matritsa o'lchamini kiritamiz
n = int(input("Matritsa o'lchamini kiriting (n): "))
result = spiral_matrix(n)
print("Soat strelkasi bo'yicha raqamlash natijasi:")
print_matrix(result)
