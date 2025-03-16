def count_in_list(my_lst, item_to_find):
    """Returns the number of times an item appears in a list."""
    count = 0
    for item in my_lst:
        if item == item_to_find:
            count += 1
    return count
