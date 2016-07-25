# python3

import sys
import threading
sys.setrecursionlimit(10**7) # max depth of recursion
# threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
    
    def compute_height(self):
        maxHeight = 0
        for vertex in range(self.n):
            if vertex not in self.parent: # only look at the leaf nodes
                height = 0
                i = vertex
                while i != -1:
                    height += 1
                    i = self.parent[i]
                    maxHeight = max(maxHeight, height)
        return maxHeight

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

# task = threading.Thread(target=main)
# task.start()
if __name__ == "__main__":
    main()