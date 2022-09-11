def pluralize_bottles(count: int) -> str:
    """Returns proper plurization of the word 'bottle'.

    Args:
        count: number of bottles
    """
    return "" if count == 1 else "s"


def verse(count: int) -> str:
    """Assembles a verse from song '99 Bottles of Beer'.

    Args:
        count: number of bottles

    Returns:
        str: song verse for bottle count

    Raises:
        AssertionError: count exceeds 99 or falls below 1
    """
    assert count < 100 and count > 0
    pluralization = "" if count == 1 else "s"
    if count == 1:
        remaining = f"Take one down and pass it around, no more bottles of beer on the wall."
    else:
        remaining = (f"Take one down and pass it around, {count - 1} "
                     f"bottle{pluralize_bottles(count -1)} of beer on the wall.")
    return (f"{count} bottle{pluralize_bottles(count)} of beer on the wall, "
            f"{count} bottle{pluralize_bottles(count)} of beer.\n"
            f"{remaining}\n\n")


def main():
    for count in range(99, 0, -1):
        print(verse(count))
    print("No more bottles of beer on the wall, no more bottles of beer.\n"
          "Go to the store and buy some more. 99 bottles of beer on the wall.")


if __name__ == '__main__':
    main()
