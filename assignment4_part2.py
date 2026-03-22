class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __repr__(self):
        return f"Task(name='{self.name}', priority={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)].priority < self.heap[i].priority:
            parent_index = self.parent(i)
            self.heap[i], self.heap[parent_index] = self.heap[parent_index], self.heap[i]
            i = parent_index

    def _heapify_down(self, i):
        size = len(self.heap)
        largest = i

        left = self.left_child(i)
        right = self.right_child(i)

        if left < size and self.heap[left].priority > self.heap[largest].priority:
            largest = left

        if right < size and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def display(self):
        if self.is_empty():
            print("Priority Queue is empty.")
        else:
            print("Current Priority Queue:")
            for task in self.heap:
                print(f"Task: {task.name}, Priority: {task.priority}")


# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()

    pq.insert(Task("Finish assignment", 5))
    pq.insert(Task("Reply to emails", 2))
    pq.insert(Task("Prepare presentation", 4))
    pq.insert(Task("Attend meeting", 3))
    pq.insert(Task("Emergency bug fix", 10))

    pq.display()

    print("\nHighest priority task:", pq.peek())

    print("\nProcessing tasks by priority:")
    while not pq.is_empty():
        print(pq.extract_max())