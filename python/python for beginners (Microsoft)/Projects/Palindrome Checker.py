import string

def is_palindrome(s):
    # Remove punctuation and spaces, convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned = s.translate(translator).replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Ask user for input
text = input("Enter a word, phrase, or number: ")

if is_palindrome(text):
    print(f"🎉 '{text}' is a palindrome!")
else:
    print(f"❌ '{text}' is not a palindrome.")