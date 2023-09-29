##

maxTimesTable = 100
numberOfRows = 100

for i in range(1, maxTimesTable + 1):
    for j in range(1, numberOfRows + 1):
        answer = i + j
        print(str(i) + ' X ' + str(j) + ' = ' + str(answer))

    print('===============================')

#Reference: https://easypythondocs.com/forloops.html
