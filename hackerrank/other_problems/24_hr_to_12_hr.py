# function for converting to 24 hour time from 12 hour time

def time_conversion(s: str) -> str:
    # Write your code here
    new_date = []
    time_dict = {f"{i:02}": i + 12 for i in range(13)}
    date_split = s.split(":")
    date_split.append(date_split[-1][:2])
    date_split.append(date_split[-2][2:])
    date_split.pop(2)
    if date_split[-1] == "AM" and date_split[0] != "12":
        new_date.append(f"{date_split[-4]}:{date_split[-3]}:{date_split[-2]}")
    elif date_split[-1] == "AM" and date_split[0] == "12":
        new_date.append(f"00:{date_split[-3]}:{date_split[-2]}")
    elif date_split[-1] == "PM" and date_split[0] != "12":
        new_date.append(f"{time_dict[date_split[-4]]}:{date_split[-3]}:{date_split[-2]}")
    elif date_split[-1] == "PM" and date_split[0] == "12":
        new_date.append(f"12:{date_split[-3]}:{date_split[-2]}")
    return ''.join(new_date)
# print(timeConversion("12:45:54PM"))
