try:
    with open('sample.txt', 'r') as file:
        line1 = file.readline()
        line2 = file.readline()
        print('Reading file content:')

        print('line 1: ', line1)
        print('line 2: ', line2)
        file.close()

except FileNotFoundError:
    print('Error: The file "sample.txt" was not found.')