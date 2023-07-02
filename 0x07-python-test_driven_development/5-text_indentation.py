#!/usr/bin/python3
"""
5-text_indentaion

Print two new lines after each of specifc symbols
"""


def text_indentation(text):
    """
    Print 2 new line after ?, ., : chars

    Args:
        text: (str) string to manipulate
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    lst = []
    tmp_idx = 0
    for i in range(len(text)):
        if text[i] in "?.:":
            print(text[tmp_idx:i + 1].strip())
            print()
            tmp_idx = i + 1
    print(text[tmp_idx:].strip(), end="")
