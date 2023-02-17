# В матрице найти сумму элементов второй половины матрицы.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
count = sum(matrix[i][j] for i in range(len(matrix)//2, len(matrix)) for j in range(len(matrix[0])))
print(count)
# Чтобы найти количество элементов второй половины матрицы,
# нужно разделить матрицу на две части и сложить элементы второй части