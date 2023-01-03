def handle_merge_sort(letters, letters_range, left, right):
    left_index, right_index = 0, 0

    for general_index in letters_range:

        if left_index >= len(left):
            letters[general_index] = right[right_index]
            right_index = right_index + 1

        elif right_index >= len(right):
            letters[general_index] = left[left_index]
            left_index = left_index + 1

        elif left[left_index] < right[right_index]:
            letters[general_index] = left[left_index]
            left_index = left_index + 1

        else:
            letters[general_index] = right[right_index]
            right_index = right_index + 1


def merge(letters, start, mid, end):

    left = letters[start:mid]
    right = letters[mid:end]
    letters_range = range(start, end)

    handle_merge_sort(letters, letters_range, left, right)


def merge_sort_palavra(letters, start=0, end=None):

    if end is None:
        end = len(letters)

    if (end - start) > 1:

        mid = (start + end) // 2

        merge_sort_palavra(letters, start, mid)
        merge_sort_palavra(letters, mid, end)
        merge(letters, start, mid, end)


def is_anagram(first_string, second_string):
    first_string_letters = list(first_string.lower())
    second_string_letters = list(second_string.lower())

    merge_sort_palavra(first_string_letters)
    merge_sort_palavra(second_string_letters)

    ordered_first_string = "".join(first_string_letters)
    ordered_second_string = "".join(second_string_letters)

    comparison = ordered_first_string == ordered_second_string

    if len(first_string) == 0 or len(second_string) == 0:
        comparison = False

    return (ordered_first_string, ordered_second_string, comparison)
