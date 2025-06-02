user_input = input('Enter text to write to the file: ')

try:
    with open('output.txt', 'r+') as file:
        file.write(user_input)
        print('Data successfully written to output.txt')
        user2_input = input('Enter additional text to append: ')
        file.write('\n' + user2_input)
        print('Data successfully appended')

    with open('output.txt', 'r') as file:
        file1_content = file.readline()
        file2_content = file.readline()
        print('Final content of output.txt:')
        print(file1_content)
        print(file2_content)
        file.close()

except FileNotFoundError:
    print('Error: The file "output.txt" was not found.')
