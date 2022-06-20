from django.shortcuts import render
import random


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


class Check:
    def generate_numbers(self, N):
        nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        secret_nums = random.sample(nums2, N)
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

    def checker_game(self, get_nums, secret_nums):

        while True:
            bulls = 0
            cows = 0
            for i in get_nums:
                for j in secret_nums:
                    if i == j and get_nums.index(i) == secret_nums.index(j):
                        bulls += 1
                        if bulls == 4:
                            return f'Congratulations, you won!'
                    elif i == j and get_nums.index(i) != secret_nums.index(j):
                        cows += 1
            return f'You have got {bulls} bulls and {cows} cows.'
