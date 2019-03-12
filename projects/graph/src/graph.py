"""
Simple graph implementation
"""
# *************************BFT**************************

class Queue():
    def __inti__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return(len(self.queue))



# *************************DFT**************************
class Stack():
    def __inti__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return(len(self.stack))

# Part 1

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
            
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

# Part 2

    def bft(self, starting_vertex_id):
        # create and empty queue
        q = Queue()
        # create an empty list (set) of visited vertices
        visited = set()
        # Put the starting vertex in the queue
        q.enqueue(starting_vertex_id)
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first node from the queue
            v = q.dequeue()
            # If that node has not been visited...
            if v not in visited:
            # Mark it as visited
                print(v)
                visited.add(v)
            # Then put all of its children into the queue
                for neighbor in self.vertices(v):
                    q.enqueue(neighbor)

# Part 3

    def dft(self, starting_vertex_id):
        # create and empty stack
        s = Stack()
        # create an empty list (set) of visited vertices
        visited = set()
        # Put the starting vertex in the stack
        s.push(starting_vertex_id)
        # While the stack is not empty
        while s.size() > 0:
            # pop the first node from the stack
            v = q.pop()
            # If that node has not been visited...
            if v not in visited:
            # Mark it as visited
                print(v)
                visited.add(v)
            # Then put all of its children into the stack
                for neighbor in self.vertices(v):
                    s.push(neighbor)
        
# Part 3.5

    def dtf_r(self, starting_vertex_id, visited=None):
        if visited is None:
            visited = set()
        # mark the starting node as visited
        visited.add(starting_vertex_id)
        # then call recursevly on each unvisited neighbor
        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:
                self.dtf_r(neighbor, visited)


# Part 4

    def bfs(self, starting_vertex_id, target_id):
        # create an empty queue
        q = Queue
        # create an empty set of visited vertices
        visited = set()
        # setup path to the starting vertex
        q.enqueue([starting_vertex_id])
        # While queue is not empty...
        while q.size > 0:
            # dequeue the first path from queue
            path = q.dequeue()
            # get current vertex from last element in path
            print(path)
            v = path[-1]
            # if vertex has not been visited...
            if v not in visited:
                # Mark as visited
                return path
            for neighbor in self.vertices[v]:
                # copy path into new instance
                new_path = list(path)
                # append the neighbor to the end of path
                new_path.append(neighbor)
                # enqueue
                q.enqueue(new_path)


# Part 5

    def dfs(self, start, end):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(start)
        # While the value passed as "end" is not in the visit array....
        while end not in visited:
            # Pop the top node from the stack
            v = s.pop()
            # If that node has not been visted...
            if v not in visited:
                    # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the stack
                if v is not None:
                    for neighbor in self.vertices[v]:
                        s.push(neighbor)
                else:
                    return print("they don't connect")



