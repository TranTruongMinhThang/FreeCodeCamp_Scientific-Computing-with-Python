def add_time(start, duration, day=None):
    startTimeList = start.split()

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

    returnPrint = ''

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

    # print(returnPrint)

    dayOfWeekPrint = ', '

    dayOfWeek = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}
    dayOfWeekReverse = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day is None:
        dayOfWeekPrint = ''
    else:
        if resultHourRaw // 24 == 0:
            dayOfWeekPrint += dayOfWeekReverse[dayOfWeek[day.lower()]]
        else:
            # dùng được cho ngày thứ 7 nhưng chủ nhật thì không đc
            if (dayOfWeek[day.lower()] + resultHourRaw // 24) / 7 <= 1:
                dayOfWeekPrint += dayOfWeekReverse[(dayOfWeek[day.lower()] + resultHourRaw // 24)]
            elif (dayOfWeek[day.lower()] + resultHourRaw // 24) / 7 > 1:
                dayOfWeekPrint += dayOfWeekReverse[(dayOfWeek[day.lower()] + resultHourRaw // 24) % 7]
            else:
                dayOfWeekPrint += dayOfWeekReverse[(dayOfWeek[day.lower()] + resultHourRaw // 24) % 7]

    dayLaterPrint = ''
    if resultHourRaw // 24 == 0:
        dayLaterPrint += ''
    elif resultHourRaw // 24 == 1:
        dayLaterPrint += ' (next day)'
    else:
        dayLaterPrint += ' (' + str(resultHourRaw // 24) + ' days later)'

    if day is None:
        returnPrint += dayLaterPrint
    else:
        returnPrint += dayOfWeekPrint + dayLaterPrint
    print(returnPrint)
    return returnPrint

startTime = "11:59 PM"
duration = "24:05"
day = 'Wednesday'
startTimeList = startTime.split()
# print(startTimeList[0].split(':'))

add_time(startTime, duration, day)