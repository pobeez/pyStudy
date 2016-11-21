def reverse(text):
    # palindrome
    pa_text = text[::-1]
    print("Reverse: ", pa_text)
    return pa_text


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter Text:")

if is_palindrome(something):
    print("Yes, it is palindrome")
else:
    print("No, it is not palindrome")