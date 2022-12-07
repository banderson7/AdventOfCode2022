if __name__ == '__main__':
    file_input = open('signal.txt')
    signal = file_input.read()
    marker_length = 14
    index = 0
    for i in range(len(signal)):
        if i < marker_length:
            continue
        potential_start = list(signal[i-marker_length:i])
        potential_start_set = set(potential_start)
        if len(potential_start) == len(potential_start_set):
            index = i
            break
    print(index)
