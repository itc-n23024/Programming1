def concat_word(*args, separator="_"):
    return separator.join(args)


print(concat_word("a", "b", "c", "d", separator="_"))
