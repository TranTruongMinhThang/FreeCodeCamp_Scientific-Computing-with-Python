def time_calculator(startTime, duration, day=None):
    startTimeList = startTime.split()

    if startTimeList[1] == 'PM':
        hour1 = int(startTimeList[0].split(':')[0]) + 12
    else:
        hour1 = int(startTimeList[0].split(':')[0])

    minute1 = int(startTimeList[0].split(':')[1])

    durationHour = int(duration.split(':')[0])
    durationMinute = int(duration.split(':')[1])

    # print(hour1,':',minute1)

    resultMinuteRaw = (minute1 + durationMinute) % 60
    resultHourRaw = hour1 + durationHour + (minute1 + durationMinute)//60

    returnPrint = 'Returns: '

    if resultHourRaw // 24 == 0:
        if resultHourRaw // 12 == 1:
            returnPrint += str(resultHourRaw % 12) + ':' + str(resultMinuteRaw) + ' PM'
        else:
            returnPrint += str(resultHourRaw) + ':' + str(resultMinuteRaw) + ' AM'
    else:
        if resultHourRaw % 24 // 12 > 0:
            returnPrint += str(resultHourRaw % 24 % 12) + ':' + str(resultMinuteRaw) + ' PM'
        else:
            returnPrint += str(resultHourRaw % 24) + ':' + str(resultMinuteRaw) + ' AM'

    print(returnPrint)


startTime = "3:59 PM"
duration = "8:59"
startTimeList = startTime.split()
# print(startTimeList[0].split(':'))

time_calculator(startTime, duration)

