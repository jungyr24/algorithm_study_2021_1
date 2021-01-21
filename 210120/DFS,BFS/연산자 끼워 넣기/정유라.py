n = int(input())
numbers = list(map(int, input().split()))

# + - * /
op = list(map(int, input().split()))
MAX = -1e9
MIN = 1e9

def dfs(numbers, index, op, result):
    global n, MIN, MAX

    # 모든 연산을 마쳤을 때 최대값, 최소값 비교 후 종료
    if index >= n:
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return
    
    for i in range(4):
        # 연산자 없으면 패스
        if op[i] == 0:
            continue

        if i == 0: # 덧셈
            op[i] -= 1
            dfs(numbers, index+1, op, result + numbers[index])
            op[i] += 1
        elif i == 1: # 뺄셈
            op[i] -= 1
            dfs(numbers, index+1, op, result - numbers[index])
            op[i] += 1
        elif i == 2: # 곱셉
            op[i] -= 1
            dfs(numbers, index+1, op, result * numbers[index])
            op[i] += 1
        elif i == 3: # 나눗셈
            if result < 0:
                result = -result
            op[i] -= 1
            dfs(numbers, index+1, op, int(result // numbers[index])) 
            op[i] += 1

dfs(numbers, 1, op, numbers[0])
print(MAX, MIN)