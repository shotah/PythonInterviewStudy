class RecentCounter:
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        return len(self.queue)


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case 1 (Example 1 from problem description)
    recent_counter1 = RecentCounter()
    expected_output1 = [
        1,
        2,
        3,
        3,
    ]  # First element is None because __init__ doesn't return anything
    actual_output1 = []  # Initialize with None for RecentCounter() call
    actual_output1.append(recent_counter1.ping(1))
    actual_output1.append(recent_counter1.ping(100))
    actual_output1.append(recent_counter1.ping(3001))
    actual_output1.append(recent_counter1.ping(3002))

    assert (
        actual_output1 == expected_output1
    ), f"Test Case 1 Failed: Expected: {expected_output1}, Actual: {actual_output1}"
    print("Test Case 1 Passed!")

    # Test Case 2 (Extended test case from previous response)
    recent_counter2 = RecentCounter()
    expected_output2 = [
        1,
        2,
        3,
        3,
        1,
    ]  # First element is None because __init__ doesn't return anything
    actual_output2 = []  # Initialize with None for RecentCounter() call
    actual_output2.append(recent_counter2.ping(1))
    actual_output2.append(recent_counter2.ping(100))
    actual_output2.append(recent_counter2.ping(3001))
    actual_output2.append(recent_counter2.ping(3002))
    actual_output2.append(recent_counter2.ping(7000))

    assert (
        actual_output2 == expected_output2
    ), f"Test Case 2 Failed: Expected: {expected_output2}, Actual: {actual_output2}"
    print("Test Case 2 Passed!")

    print("All inline tests passed!")
