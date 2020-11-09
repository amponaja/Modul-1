
def timeconverter(sec):
    if sec > 359999:
        print("invalid input")
    else:
        hours = sec // 3600
        minutes = (sec % 3600) // 60
        seconds = sec % 60
        str = f'{(hours)}:{(minutes)}:{(seconds)}'
        print(str)

timeconverter(359999)

# import datetime
# def timeconverter(sec):
#     if sec > 359999:
#         print("invalid input")
#     else:
#         second = datetime.timedelta(seconds =sec)
#         print(second)

# timeconverter(86400)