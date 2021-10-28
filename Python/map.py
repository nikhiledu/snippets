def array_left_rotation(a, n, k):
  print(a)
  print(n)
  print(k)
  return 0

n, k = list(map(int, input().strip().split(' ')))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(' '.join(map(str,answer)))

