signal = input()

start = 0
end = 4
while end <= len(signal):
    marker = signal[start:end]

    if len(set(marker)) == 4:
        print(marker, end)
        break

    start += 1
    end += 1
