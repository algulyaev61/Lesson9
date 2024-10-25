def print_params(a=1, b='строка', c=True):
    print(a, b, c)

values_list=[4.15, 'one', None]
values_dict ={'a': 'two', 'b': [1, 2, 3], 'c': 7.5}

values_list_2=[54.32, 'Строка']

# print_params()
# print_params(*values_list)
# print_params(**values_dict)
print_params(*values_list_2,42)