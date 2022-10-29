def text(text):
    try:
        a = text[::-1]
        if text == a:
            print("Є паліндромом")
        else:
            print("Не є паліндромом")
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        text(input("Text -->"))
    except Exception as e:
        print(f"Error {e}")
main()