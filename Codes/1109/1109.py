def corpFlightBookings_TLE(bookings, n):
    answer = [0] * n

    for start, end, n_seats in bookings:
        for i in range(start-1, end):
            answer[i] += n_seats

    return answer

def corpFlightBookings(bookings, n):

    diff = [0] * (n + 1)
    for start, end, n_seats in bookings:
        diff[start - 1] += n_seats
        diff[end] -= n_seats

    answer = [0] * (n + 1)
    for i in range(1, n + 1):
        answer[i] = answer[i - 1] + diff[i - 1]

    return answer[1: ]


print(corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))