def solution(ineq, eq, n, m):
    equation = ineq + eq
    
    if equation == ">=":
        return 1 if n >= m else 0
    elif equation == "<=":
        return 1 if n <= m else 0
    elif equation == ">!":
        return 1 if n > m else 0
    elif equation == "<!":
        return 1 if n < m else 0