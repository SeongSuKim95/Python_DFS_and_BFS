def recursive_function(i):

    if i == 100:

        return

    print( i,'번째 재귀함수에서 ', i+1, '번째 재귀함수 호출')
    recursive_function(i+1)

    print( i,'번째 재귀함수 종료')
recursive_function(1)

#재귀함수의 수행은 stack 구조를 이용한다. 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문.

def factorial_iterative(n):
    result = 1
    # 1부터 n까지 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):

    if n <= 1:
        return 1
    return n*factorial_recursive(n-1)

print('iterative:', factorial_iterative(5))
print('recursive:', factorial_recursive(5))

#반복과 재귀 함수의 차이 : code를 recursive하게 짤 때 code가 더 간단해진다. 점화식을 그대로 code로 구현하기 때문

