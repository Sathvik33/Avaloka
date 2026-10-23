import heapq


def can_attend_all(events):
    sorted_events = sorted(events)

    for i in range(1, len(sorted_events)):
        previous_end = sorted_events[i - 1][1]
        current_start = sorted_events[i][0]

        if current_start < previous_end:
            return False

    return True


def min_rooms_required(events):
    if not events:
        return 0

    sorted_events = sorted(events)
    end_times = []

    for start, end in sorted_events:
        # Reuse a room if its meeting has ended.
        if end_times and end_times[0] <= start:
            heapq.heappop(end_times)

        # This event now occupies a room until its end time.
        heapq.heappush(end_times, end)

    return len(end_times)


def main():
    # Example 1: Adjacent events do not overlap.
    events1 = [(9, 10), (10, 11), (11, 12)]
    print("Events:", events1)
    print("Can attend all:", can_attend_all(events1))  # Expected: True
    print("Rooms required:", min_rooms_required(events1))  # Expected: 1

    print()

    # Example 2: Some meetings overlap.
    events2 = [(9, 11), (10, 12), (11, 13)]
    print("Events:", events2)
    print("Can attend all:", can_attend_all(events2))  # Expected: False
    print("Rooms required:", min_rooms_required(events2))  # Expected: 2

    print()

    # Example 3: Empty input.
    events3 = []
    print("Events:", events3)
    print("Can attend all:", can_attend_all(events3))  # Expected: True
    print("Rooms required:", min_rooms_required(events3))  # Expected: 0


if __name__ == "__main__":
    main()
