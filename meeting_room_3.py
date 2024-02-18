import heapq
from typing import List


# Meeting Rooms III - PROGRAMMING CHALLENGE
# You are given an integer n. There are n rooms numbered from 0 to n - 1.

# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting
# will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

# Meetings are allocated to rooms in the following manner:
# 1. Each meeting will take place in the unused room with the lowest number.
# 2. If there are no available rooms, the meeting will be delayed until a room becomes free.
#    The delayed meeting should have the same duration as the original meeting.
# 3. When a room becomes unused, meetings that have an earlier original start time should be given the room.

# Return the number of the room that held the most meetings. If there are multiple rooms,
# return the room with the lowest number.

# A half-closed interval [a, b) is the interval between a and b including a and not including b.

def mostBooked(n: int, meetings: List[List[int]]) -> int:
    meetings.sort()

    available = [i for i in range(n)]
    used = []  # (end_time, room_number)
    count = [0] * n  # count[n] = meetings schedule
    for start, end in meetings:
        # finish meetings
        while used and start >= used[0][0]:
            _, room = heapq.heappop(used)
            heapq.heappush(available, room)
        # no room is available
        if not available:
            end_time, room = heapq.heappop(used)
            end = end_time + (end - start)
            heapq.heappush(available, room)

        room = heapq.heappop(available)
        heapq.heappush(used, (end, room))
        count[room] += 1

    return count.index(max(count))


n = 2
meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]

n1 = 3
meetings1 = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]

print(mostBooked(n, meetings))  # 0
print(mostBooked(n1, meetings1))  # 1
