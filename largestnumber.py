def largest_number(A):
    A.sort(key=lambda x: str(x), reverse=True)
    largest_num = ''.join(str(num) for num in A)
    return largest_num
A = list(map(int,input().split()))
print(largest_number(A))
