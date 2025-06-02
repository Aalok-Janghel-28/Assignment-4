# Assignment-4

<h1>Task1</h1>

1. Open File: Attempts to open a file named sample.txt in read mode ('r').

2. Read Lines: Reads the first two lines from the file using readline() function.

3. Print Output: Displays the content of the first and second lines on the screen.

4. Error Handling: If the file sample.txt is not found, it prints an error message:
"Error: The file 'sample.txt' was not found."

5. File Closing: Though the with statement handles file closing automatically, there's an explicit file.


<h1>Task2</h1> : 
1. Takes user input using the input() function.

2. Opens the file output.txt in read and write mode (r+).

3. Writes the user input to the file.

4. Prompts the user again for additional text to append.

5. Appends the new input to the file by writing it on a new line.

6. Closes the file after writing and appending.

7. Reopens the same file in read mode (r).

8. Reads and prints the first two lines of the file to show the final content.

9. Handles file not found errors with a try-except block.