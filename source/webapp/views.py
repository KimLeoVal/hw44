from urllib.parse import parse_qs

from django.shortcuts import render

from webapp import checker

n = 4
secret_nums = checker.Check()
secret_nums = secret_nums.generate_numbers(n)


def index_view(request):
    if request.method == 'GET':
        context = {'sec_num': secret_nums}
        return render(request, 'index.html', context)

    if request.method == 'POST':
        int_num = []
        num_list = []
        step = 0
        try:
            num = request.POST.get('user_num')
            num = num.split(" ")
            num = list(num)
            num_list.append(num)
            step += 1
            try:
                for i in num:
                    i = int(i)
                    int_num.append(i)
            except ValueError:
                context = {'error': "Enter 4 different numbers from 1 to 9",
                           'num_list': num_list,
                           'step': step}
                return render(request, 'index.html', context)
            try:
                check_num = checker.Check()
                if check_num.checker_list(int_num):
                    game = checker.Check()
                    res = game.checker_game(int_num, secret_nums)
                    context = {'res': res,
                               'num_list': num_list,
                               'step': step

                       }
            except ValueError:
                context = {'error': "Enter 4 different numbers from 1 to 9",
                           'num_list': num_list,
                           'step': step}
                return render(request, 'index.html', context)
        except ValueError:
            context = {'error': "You didn't enter anything",
                       'num_list': num_list,
                       'step': step}
            return render(request, 'index.html', context)
        return render(request, 'index.html', context)



def history_view(request):
    step = 0
    while True:
        a = index_view(request)
        step += 1
        print(a)

        break
        num = a
    context = {'user_num': num}
    return render(request, 'history.html', context)
