def slice_me(family: list, start: int, end: int) -> list:
    """slice func take specific lists index to slice it as the input want
        and printing the old shape with the new shape after the slice"""
    if not isinstance(family, list) or not all(
        isinstance(row, list) for row in family
    ):
        raise ValueError("Input must be a list of lists")

    if len(set(len(row) for row in family)) != 1:
        raise ValueError("All sublists must have the same length.")

    rows, cols = len(family), len(family[0])
    print(f"My shape is : ({rows}, {cols})")

    truncated = family[start:end]

    new_rows = len(truncated)
    print(f"My new shape is : ({new_rows}, {cols})")

    return truncated
