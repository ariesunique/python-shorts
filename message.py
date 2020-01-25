# -------------------------
# Algorithms challenge - Solution for MessMessage problem
# https://www.interviewcake.com/question/python3/mesh-message
#
# The code and the test cases are my own. Only the example used
# was borrowed.
#
# Solution: Use a breadth-first seach to visit each node until we
# find the one we're looking for.
# -------------------------

import pytest

from collections import OrderedDict, deque

class Network():
    
    def __init__(self, network={}):
        self.network = network
    
    def __repr__(self):
        pass
    
    def shortest_path(self, sender, recipient):
        network = self.network
        if sender == recipient:
            return [sender]
        
        if not sender in network:
            return []
        
        # keep track visited nodes; use a dict for easy lookups to get the parent
        visited = {}
        # ordered dict maintains insertion order, thus we can use a dict as a queue
        queued = OrderedDict()
        found = False
        
        # queue the current person and their parent
        queued[sender] = None
        
        while queued and not found:
            current, parent = queued.popitem(last=False)
            visited[current] = parent
            neighbors = network.get(current, [])
            if recipient in neighbors:
                visited[recipient] = current
                found = True
            else:                
                for neighbor in neighbors:
                    if neighbor not in visited and neighbor not in queued:
                        queued[neighbor] = current
        
        if not found:
            return []
        else:
            # iterate over visited nodes to build route
            route = deque()
            route.appendleft(recipient)
            parent = visited[recipient]
            while parent:
                route.appendleft(parent)
                parent = visited[parent]
            return list(route)
    
    
def setup():
    network = {
        "Min": ["William", "Jayden", "Omar"],
        "William": ["Min", "Noam"],
        "Jayden": ["Min", "Amelia", "Ren", "Noam"],
        "Ren": ["Jayden", "Omar"],
        "Amelia": ["Jayden", "Adam", "Miguel"],
        "Adam": ["Amelia", "Miguel", "Sofia", "Lucas"],
        "Miguel": ["Amelia", "Adam", "Liam", "Nathan"],
        "Noam": ["Nathan", "Jayden", "William"],
        "Omar": ["Ren", "Min", "Scott"]        
    }
    return network


def test_same_sender_recipient():
    network = Network(setup())
    path = network.shortest_path("Jayden", "Jayden")
    assert path == ["Jayden"]

    
def test_empty_network():
    network = Network()
    path = network.shortest_path("John", "Jack")
    assert path == []


def test_direct_neighbor():
    network = Network(setup())
    path = network.shortest_path("Jayden", "Amelia")
    assert path == ["Jayden", "Amelia"]

    
def test_neighbor_once_removed():
    network = Network(setup())
    path = network.shortest_path("Ren", "Scott")
    assert path == ["Ren", "Omar", "Scott"]


def test_neighbors_nlevels():
    network = Network(setup())
    path = network.shortest_path("Jayden", "Lucas")
    assert path == ["Jayden", "Amelia", "Adam", "Lucas"]

    
def test_no_path():
    network = Network({
        "John": ["Tracy"],
        "Jenny": ["Bob"]
    })
    path = network.shortest_path("John", "Bob")
    assert path == []


def test_standard():
    network = Network(setup())
    path = network.shortest_path("Jayden", "Adam")
    assert path == ["Jayden", "Amelia", "Adam"]
    

    
if __name__ == "__main__":
    test_works()