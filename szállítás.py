# %%
def szállítás(input):
    list_ = input.split(" ")
    number_list = [int(x) for x in list_]
    return sum(number_list[1:])

szállítás("5 3 6 3 2 1")



