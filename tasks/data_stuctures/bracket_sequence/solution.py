def solution(s: str) -> bool:
    map_of_pairs = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    list_of_brackets = []

    for char in s:
        if char in map_of_pairs.values():
            list_of_brackets.append(char)
        elif char in map_of_pairs.keys():
            if not list_of_brackets:
                return False
            last_open = list_of_brackets.pop()
            if last_open != map_of_pairs[char]:
                return False

    return not list_of_brackets

