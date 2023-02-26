### Exercise - 22 -  Series

def slices(series, length):
    if series == '' or length <= 0 or length > len(series):
        raise ValueError("Invalid Input")
    else:
        size = length
        start = 0
        end = start + size
        sub_str = []
        while end != len(series) + 1:
            sub_str.append(series[start:end])
            start += 1
            end += 1
        return sub_str