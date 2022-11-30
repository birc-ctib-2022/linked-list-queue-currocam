"""Testing queues."""


import random

from queue_impl import Queue


def test_me() -> None:
    """Remember to write tests."""
    queue = Queue()
    assert queue.is_empty()
    x = random.sample(range(10, 300), 50)
    for el in x:
        queue.enqueue(el)
    assert queue.front() == x[0]
    for el in x:
        assert el == queue.dequeue()
