def time_conversion(s):
    time = s.split(":")
    # print(time)
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
    else:
        if time[0] == "AM":
            time[0] == "00"
    ntime = ":".join(time)
    print(str(ntime[:-2]))


s = "07:05:45PM"
time_conversion(s)
# print(s[:-2])
