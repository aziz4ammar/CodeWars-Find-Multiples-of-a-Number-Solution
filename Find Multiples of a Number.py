def find_multiples(integer, limit):
    multiples = []
    for i in range(1, limit + 1):
        if i * integer <= limit:
            multiples.append(i * integer)
    return multiples