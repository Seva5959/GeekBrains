def likes(names):
    """
    
    Возвращает строку с информацией о том, кто лайкнул пост.

    >>> likes([])
    'no one likes this'
    >>> likes(['Alice'])
    'Alice likes this'
    >>> likes(['Alice', 'Bob'])
    'Alice and Bob like this'
    >>> likes(['Alice', 'Bob', 'Charlie'])
    'Alice, Bob and Charlie like this'
    >>> likes(['Alice', 'Bob', 'Charlie', 'Dave'])
    'Alice, Bob and 2 others like this' """

    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


print(likes([]))
