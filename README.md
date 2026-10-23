# Avaloka Data Structures & Systems Design Assignment

Solutions for the two problems in the Avaloka (Guruvai Sciences) take-home assignment.

## Files

- `problem1_lru_cache.py` — LRU Cache using a dictionary and doubly linked list.
- `problem2_event_scheduler.py` — Event overlap detection and minimum room calculation using sorting and a min-heap.

## Requirements

- Python 3
- No third-party packages are required.

## Run the solutions

```bash
python problem1_lru_cache.py
python problem2_event_scheduler.py
```

## Problem 1: LRU Cache

The cache uses a dictionary to locate nodes by key in O(1) average time and a doubly linked list to maintain usage order. `get()` and `put()` take O(1) average time.

Overall space complexity: O(C), where C is the cache capacity.

## Problem 2: Event Scheduler

`can_attend_all(events)` sorts events by start time and checks whether any event overlaps with the previous event.

`min_rooms_required(events)` sorts events and uses a min-heap of meeting end times to reuse rooms whenever an earlier meeting ends at or before the next meeting starts.

Time complexity for each scheduler function: O(n log n).

Space complexity: O(n).

## Example input

```python
events = [(9, 10), (10, 11), (11, 12)]
```

Expected output:

```text
Can attend all: True
Rooms required: 1
```

Adjacent events are not considered overlapping.
