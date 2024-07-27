vowels = ['a', 'e', 'i', 'o', 'u']

def main():
    twitter = str(input("Input: ")).strip()
    print('Output:', shorten(twitter))

def shorten(word):
    for c in word:
        if c.lower() in vowels:
            word = word.replace(c, '')
    return word

if __name__ == "__main__":
    main()
