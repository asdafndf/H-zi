# %%
def sorozat(a,b,c):
    list_ = [x for x in range(a,b+1,c)]
    string_list = [str(x) for x in list_]
    result = " ".join(string_list) + " "
    return result

sorozat(10,20,3)


