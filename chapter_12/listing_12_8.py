import asyncio
from asyncio import Queue, PriorityQueue
from dataclasses import dataclass, field


@dataclass(order=True)
class WorkItem:
    priority: int
    data: str = field(compare=False)


async def worker(queue: Queue):
    while not queue.empty():
        work_item: WorkItem = await queue.get()
        print(f'Processing work item {work_item}')
        queue.task_done()


async def main():
    priority_queue = PriorityQueue()

    work_items = [WorkItem(3, 'Lowest priority'),
                  WorkItem(3, 'Lowest priority second'),
                  WorkItem(3, 'Lowest priority third'),
                  WorkItem(2, 'Medium priority'),
                  WorkItem(1, 'High priority')]

    worker_task = asyncio.create_task(worker(priority_queue))

    for work in work_items:
        priority_queue.put_nowait(work)

    await asyncio.gather(priority_queue.join(), worker_task)


asyncio.run(main())

# Processing work item WorkItem(priority=1, data='High priority')
# Processing work item WorkItem(priority=2, data='Medium priority')
# Processing work item WorkItem(priority=3, data='Lowest priority third')
# Processing work item WorkItem(priority=3, data='Lowest priority second')
# Processing work item WorkItem(priority=3, data='Lowest priority')

# 对于相当的优先级3，插入顺序和执行顺序不保证相同。

# This is happening because the underlying heapsort algorithm is not a stable
# sort algorithm, as equal items are not guaranteed to be in the same order of insertion