signal = input()

start = 0
end = 14
while end <= len(signal):
    marker = signal[start:end]

    if len(set(marker)) == 14:
        print(marker, end)
        break

    start += 1
    end += 1
