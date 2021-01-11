# Find the maximum number of non overlaping activities (return those activities)


def activity_selection(start_finish_time):
    start_finish_time.sort(key=lambda x: x[1])

    activities = []
    count = 1
    i = 0
    j = 1
    activities.append(start_finish_time[i])

    while j < len(start_finish_time):
        if start_finish_time[j][0] >= start_finish_time[i][1]:
            i = j
            activities.append(start_finish_time[j])
        j += 1

    return activities


if __name__ == '__main__':
    start_finish_time = [
        (12, 14), (3, 5), (1, 3), (5, 7), (0, 6), (3, 8), (5, 9),
        (8, 11), (6, 10), (2, 13), (8, 12)
    ]

    print(activity_selection(start_finish_time))

# Time: O(N log N)
# Space: O(N)
