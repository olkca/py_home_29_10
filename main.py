def text(text, word):
    try:
        words = word.split()
        for word in words:
            if text.count(word)>0:
                o = word
                t = word.upper()
                text = text.replace(o,t)
        print(text)
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        text(input("Text -->"), input("Word -->"))
    except Exception as e:
        print(f"Error {e}")
main()