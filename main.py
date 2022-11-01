def text(text):
    try:
        res = text.count(".") + text.count("!") + text.count("?")
        print(res)
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        text(input("Text -->"))
    except Exception as e:
        print(f"Error {e}")
main()

