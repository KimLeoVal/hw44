import random


class Check:
    def generate_numbers(self, n):
        nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        secret_nums = random.sample(nums2, n)
        return secret_nums

    def checker_list(self, get_nums):
        if len(get_nums) == 4:
            if len(get_nums) == len(set(get_nums)):
                for i in get_nums:
                    if 0 < i < 10:
                        return get_nums
                    else:
                        raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError

    def checker_game(self, int_num, secret_nums):

        while True:
            bulls = 0
            cows = 0
            for i in int_num:
                for j in secret_nums:
                    if i == j and int_num.index(i) == secret_nums.index(j):
                        bulls += 1
                        if bulls == 4:
                            return f'Congratulations, you won!'
                    elif i == j and int_num.index(i) != secret_nums.index(j):
                        cows += 1
            return f'You have got {bulls} bulls and {cows} cows.'
