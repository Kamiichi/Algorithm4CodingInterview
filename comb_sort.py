from typing import List

def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True
    CONSTANT_NUM = 1.3

    while gap != 1 or swapped:
        gap = int(gap / CONSTANT_NUM)
        if gap < 1:
            gap = 1

        swapped = False
        
        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                swapped = True
    
    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(nums)
    print(comb_sort(nums))