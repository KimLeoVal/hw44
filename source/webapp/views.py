from urllib.parse import parse_qs

from django.shortcuts import render

from webapp import checker

n = 4
secret_nums = checker.Check()
secret_nums = secret_nums.generate_numbers(n)
num_list = []
step_list = []
step = {'step': 0}


def index_view(request):
    if request.method == 'GET':
        context = {'sec_num': secret_nums}
        return render(request, 'index.html', context)

    if request.method == 'POST':
        int_num = []

        try:
            num = request.POST.get('user_num')
            num = num.split(" ")
            num = list(num)
            num_list.append(num)
            step['step'] += 1
            step_list.append(step['step'])
            try:
                for i in num:
                    i = int(i)
                    int_num.append(i)
            except ValueError:
                context = {'error': "Enter 4 different numbers from 1 to 9",
                           }
                return render(request, 'index.html', context)
            try:
                check_num = checker.Check()
                if check_num.checker_list(int_num):
                    game = checker.Check()
                    res = game.checker_game(int_num, secret_nums)
                    context = {'res': res,

                               }
            except ValueError:
                context = {'error': "Enter 4 different numbers from 1 to 9",
                           }
                return render(request, 'index.html', context)
        except ValueError:
            context = {'error': "You didn't enter anything",
                       }
            return render(request, 'index.html', context)
        return render(request, 'index.html', context)


def history_view(request):
    context = {'step': step_list,
               'num_list': num_list
               }
    return render(request, 'history.html', context)
