import ast

def load_tests(filename):
    tests = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            expected_str, triangle_str = line.split(';', 1)
            expected = int(expected_str)
            triangle = ast.literal_eval(triangle_str)
            tests.append((expected, triangle))
    return tests

def minimum_total(triangle: list[list[int]])->int: 
    if not triangle:
        return None 
    rowsCount = len(triangle)
    # идём снизу вверх по строкам
    for i in range(rowsCount - 2, -1, -1): 
        for j in range(len(triangle[i])): 
            # вычисляем значение функции Беллмана S(i,j)
            triangle[i][j] += min(triangle[i+1][j], 
                                  triangle[i+1][j+1])
    return triangle[0][0]

if __name__ == "__main__":
    tests = load_tests('triangle_tests.txt')
    for i, (expected, tri) in enumerate(tests):
        result = minimum_total(tri)
        if result == expected:
            status = "OK" 
        else:
            status = "FAIL"
        print(f"Тест {i+1}: {status} | ожидалось {expected}, получено {result}")