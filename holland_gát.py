def holland_gát(hullámok_magassága, gát_magasság):
    átcsapók = [x for x in hullámok_magassága if x > gát_magasság]
    return int(sum(átcsapók)/len(átcsapók))

holland_gát([8,9,10,11,12,14],10)