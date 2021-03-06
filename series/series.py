from typing import List


def slices(digits: str, n: int) -> List[List[int]]:
    if not (0 < n <= len(digits)):
        raise ValueError("Slice length invalid.")
    substrings = zip(*(
        (d for d in digits[i:])
        for i in range(n)
    ))
    return [
        [int(d) for d in substring]
        for substring in substrings
    ]
