# 1
for i in range (1, 10):
    for j in range (1, i + 1):
        print ('{0}*{1}={2}'.format (i, j, i * j), end = ' ')
    print ()

# 2
i, j = 1, 1
n = int(input())
for i in range(n + 1) :
    for j in range(i) :
        j += 1
        print ( '{0}*{1}={2}'.format (i, j, i * j), end = ' ')
    i += 1
    if i != j :
        print ('')
