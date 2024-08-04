def main():
    while True:
        text = input('Please enter the text to check for a palindrome (or type "exit" to quit): ').strip().lower()

        if text == 'exit':
        	break

        if text == text[::-1]:
            print('The text is a palindrome.')
        else:
            print('The text is not a palindrome.')


if __name__ == '__main__':
    main()