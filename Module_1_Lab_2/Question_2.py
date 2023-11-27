class CustomQueue:
    """
    A class to implement a queue using two stacks.

    Attributes:
    - stack_enqueue (list): Stack for enqueue operation.
    - stack_dequeue (list): Stack for dequeue operation.
    """

    def __init__(self):
        """
        Initializes the CustomQueue class with two empty stacks.
        """
        self.stack_enqueue = []  # Stack for enqueue operation
        self.stack_dequeue = []  # Stack for dequeue operation

    def enqueue(self, x):
        """
        Adds an element to the end of the queue.

        Args:
        - x (int): The element to be enqueued.
        """
        # Push all elements from dequeue stack to enqueue stack
        while self.stack_dequeue:
            self.stack_enqueue.append(self.stack_dequeue.pop())

        # Push the new element to enqueue stack
        self.stack_enqueue.append(x)

    def dequeue(self):
        """
        Removes the element at the front of the queue.
        """
        # Push all elements from enqueue stack to dequeue stack
        while self.stack_enqueue:
            self.stack_dequeue.append(self.stack_enqueue.pop())

        # Pop from dequeue stack (front of the queue)
        if self.stack_dequeue:
            return self.stack_dequeue.pop()
        else:
            return None

    def print_front(self):
        """
        Retrieves the element at the front of the queue without removing it.

        Returns:
        - int or None: The element at the front of the queue or None if the queue is empty.
        """
        # Push all elements from enqueue stack to dequeue stack
        while self.stack_enqueue:
            self.stack_dequeue.append(self.stack_enqueue.pop())

        # Get the element at the front of the queue (top of dequeue stack)
        if self.stack_dequeue:
            return self.stack_dequeue[-1]
        else:
            return None


def process_queries(queries):
    """
    Processes a sequence of queries for the CustomQueue and returns elements to print at the front.

    Args:
    - queries (list): A list of queries in the specified format.

    """
    queue = CustomQueue()
    results = []
    for query in queries:
        query_type, *args = query.split()
        if query_type == '1':  # Enqueue
            elements = [int(x) for x in args[0].split(',')]
            for element in elements:
                queue.enqueue(element)
        elif query_type == '2':  # Dequeue
            queue.dequeue()
        elif query_type == '3':  # Print front
            front_element = queue.print_front()
            if front_element:
                results.append(front_element)

    return results


# Taking input
user_input = input().strip().split(',')

# Processing queries
output = process_queries(user_input)

# Displaying output
print(*output, sep='\n')