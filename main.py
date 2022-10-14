def computation(n):
    # Any num of input by loops
    # variable initialization
    num = 0.0
    squared_num = 0.0

    #    selecting
    if n < 2:
        print('Seems like you enter a invalid integer :( Please try again')
        print('( Noticification: the number should be above 1 )')

    # 2. do loops
    else:
        for i in range(n):
            print('Please enter the ' + str(i + 1) + ' value:')
            a = float(input())
            num = num + a
            squared_num = squared_num + a ** 2

        # 3. Computing
        mean = num / n
        variance = squared_num / n - mean ** 2

        # 4.Representation
        print('The mean is', mean)
        print('The variance is', variance)
        print('Thanks for use :)')

    # 1. enter the num of computing


print('Welcome! This is a computor for mean and variance.')
print('Please enter the number of variables:')
print('Happy')
n = int(input('How many variables do you want to compute:'))
computation(n)
