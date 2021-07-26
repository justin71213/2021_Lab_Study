def firstMissingPositive(nums: list) -> int:

    # step 1
    target_list = [None for x in range(len(nums) + 1)]
    for i in nums:
        if (i < 1) or (i > len(nums)):
            continue
        else:
            target_list[i - 1] = True

    # step 2
    for i in range(len(target_list)):
        if target_list[i] == None:
            return i + 1


def firstMissingPositive(nums: list) -> int:

    # step 1
    target = set(nums)

    # step 2
    for i in range(len(target)):
        if i + 1 not in target:
            return i + 1
    return len(target) + 1


def firstMissingPositive(nums: list) -> int:

    # step 1
    appear = {}
    for i in nums:
        if (i > 0) and (i not in appear):
            appear[i] = True

    # step 2
    for i in range(len(appear)):
        if i + 1 not in appear:
            return i + 1
    return len(appear) + 1


if __name__ == "__main__":
    print("ans:", firstMissingPositive([1, 2, 0]))
