def add_time(start: str, duration: str, day: str = None):
    # Split start time and duration
    start_hour, start_minute_with_abb = start.split(':')
    start_minute, abb = start_minute_with_abb.split(' ')

    # Duration time split
    dur_hour, dur_minute = duration.split(':')

    # Convert times to minutes
    start_total_minutes = int(start_hour) * 60 + int(start_minute)
    if abb == "PM":
        start_total_minutes += 12 * 60
    dur_total_minutes = int(dur_hour) * 60 + int(dur_minute)

    # Total new minutes
    total_minutes = start_total_minutes + dur_total_minutes

    # Calculate new hour, minute, and period
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    new_abb = "AM" if new_hour < 12 else "PM"
    new_hour = new_hour if new_hour <= 12 else new_hour - 12
    new_hour = 12 if new_hour == 0 else new_hour

    # Format new minute
    new_minute = f'0{new_minute}' if new_minute < 10 else str(new_minute)

    # Calculate days passed
    days_passed = total_minutes // (24 * 60)
    days_later = ""
    if days_passed == 1:
        days_later = " (next day)"
    elif days_passed > 1:
        days_later = f" ({days_passed} days later)"

    # Calculate the new day of the week
    if day:
        day = day.capitalize()
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = (days_of_week.index(day) + days_passed) % 7
        new_day = days_of_week[day_index]
        ultimate_answer = f'{new_hour}:{new_minute} {new_abb}, {new_day}{days_later}'
    else:
        ultimate_answer = f'{new_hour}:{new_minute} {new_abb}{days_later}'

    return ultimate_answer
