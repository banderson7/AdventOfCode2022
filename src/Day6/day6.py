if __name__ == '__main__':
    file_input = open('signal.txt')
    signal = file_input.read()
    index = 0
    for i in range(len(signal)):
        if i < 4:
            continue
        potential_start = list(signal[i-4:i])
        potential_start_set = set(potential_start)
        if len(potential_start) == len(potential_start_set):
            index = i
            break
    print(index)
