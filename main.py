import numpy as np

# Матрица парных сравнений для критериев
matrix = np.array([
    [1, 3, 1/5],
    [1/3, 1, 1/7],
    [5, 7, 1]
])

# Нормализация матрицы
column_sums = np.sum(matrix, axis=0)
normalized_matrix = matrix / column_sums

# Взвешенные суммы
weighted_sums = np.sum(normalized_matrix, axis=1)

# Вычисление весов
weights = weighted_sums / np.sum(weighted_sums)
print("Веса критериев:", weights)
# Пример матрицы парных сравнений для альтернатив по первому критерию
alternatives_matrix = np.array([
    [1, 3, 1/2],  # A vs B, A vs C
    [1/3, 1, 1/5], # B vs A, B vs C
    [2, 5, 1]      # C vs A, C vs B
])

# Нормализация матрицы
alternatives_column_sums = np.sum(alternatives_matrix, axis=0)
normalized_alternatives_matrix = alternatives_matrix / alternatives_column_sums

# Взвешенные суммы для альтернатив
alternatives_weighted_sums = np.sum(normalized_alternatives_matrix, axis=1)

# Вычисление весов для альтернатив
alternatives_weights = alternatives_weighted_sums / np.sum(alternatives_weighted_sums)
print("Веса альтернатив по критерию 1:", alternatives_weights)

# Предположим, что у нас есть веса критериев
weights_criteria = np.array([0.19318606, 0.08330788, 0.72350606])

# Веса альтернатив по каждому критерию (например, из предыдущего шага)
weights_alternatives_criteria1 = np.array([0.5, 0.3, 0.2])  # по первому критерию
weights_alternatives_criteria2 = np.array([0.4, 0.4, 0.2])  # по второму критерию
weights_alternatives_criteria3 = np.array([0.6, 0.2, 0.2])  # по третьему критерию

# Общий балл для каждой альтернативы
total_scores = (
    weights_criteria[0] * weights_alternatives_criteria1 +
    weights_criteria[1] * weights_alternatives_criteria2 +
    weights_criteria[2] * weights_alternatives_criteria3
)

print("Общий балл для каждой альтернативы:", total_scores)
# Матрицы парных сравнений для альтернатив по каждому критерию

# Для критерия 1 (например, "Актуальность")
matrix_criteria_1 = np.array([
    [1, 1/3, 3],    # Сравнение альтернатив A, B, C
    [3, 1, 5],      # Сравнение альтернатив B и C
    [1/3, 1/5, 1]   # Сравнение альтернатив C и A
])

# Для критерия 2 (например, "Перспективность")
matrix_criteria_2 = np.array([
    [1, 5, 1/7],    # Сравнение альтернатив A, B, C
    [1/5, 1, 1/9],  # Сравнение альтернатив B и C
    [7, 9, 1]       # Сравнение альтернатив C и A
])

# Для критерия 3 (например, "Ресурсы")
matrix_criteria_3 = np.array([
    [1, 1/7, 5],    # Сравнение альтернатив A, B, C
    [7, 1, 9],      # Сравнение альтернатив B и C
    [1/5, 1/9, 1]   # Сравнение альтернатив C и A
])
# Нормализация для критерия 1
column_sums_1 = np.sum(matrix_criteria_1, axis=0)
normalized_matrix_1 = matrix_criteria_1 / column_sums_1
weighted_sums_1 = np.sum(normalized_matrix_1, axis=1)
weights_1 = weighted_sums_1 / np.sum(weighted_sums_1)

# Нормализация для критерия 2
column_sums_2 = np.sum(matrix_criteria_2, axis=0)
normalized_matrix_2 = matrix_criteria_2 / column_sums_2
weighted_sums_2 = np.sum(normalized_matrix_2, axis=1)
weights_2 = weighted_sums_2 / np.sum(weighted_sums_2)

# Нормализация для критерия 3
column_sums_3 = np.sum(matrix_criteria_3, axis=0)
normalized_matrix_3 = matrix_criteria_3 / column_sums_3
weighted_sums_3 = np.sum(normalized_matrix_3, axis=1)
weights_3 = weighted_sums_3 / np.sum(weighted_sums_3)
# Вычисление общего балла
final_scores = (weights[0] * weights_1 + weights[1] * weights_2 + weights[2] * weights_3)
print("Общий балл для каждой альтернативы:", final_scores)
