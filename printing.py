import typing

# translate the card number to printable format
def get_name(num: int) -> str:
    if num == 11:
        return "J"
    if num == 12:
        return "Q"
    if num == 13:
        return "K"
    if num == 1:
        return "A"
    else:
        return str(num)


if __name__ == "__main__":
    print(get_name(1))
