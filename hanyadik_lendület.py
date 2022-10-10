def hanyadik_lendület(x):
    count = 0
    mászás = 10
    magasság = 0
    while x > magasság:
        magasság = (magasság + mászás)*0.9
        mászás += 10
        count += 1
    return count