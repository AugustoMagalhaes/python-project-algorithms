def validate_nums(nums):
    if not nums or type(nums) not in [list, tuple, set]:
        return False

    if len(nums) == len(set(nums)) or len(nums) == 0:
        return False

    return True


def find_duplicate(nums):
    if not validate_nums(nums):
        return False

    sorted_nums = sorted(nums)

    if sorted_nums[0] < 0:
        return False

    for index, num in enumerate(sorted_nums):
        next_index = index + 1 if index != len(sorted_nums) - 1 else index
        if num == sorted_nums[next_index]:
            return num

    return False
