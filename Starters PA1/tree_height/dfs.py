# python3

import sys
import threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
    
    def make_adj(self):
        # make adjacency list representation
        adj = []
        for i in range(self.n):
            adj_i = [k for k, item in enumerate(self.parent) if item == i]
            adj.append(adj_i)
        # print('adj looks like', adj)
        return adj

    def dfs_iterative(self, adjLists, s):
        stack = []
        stack.append(s)
        n1 = len(adjLists)
        visited = []
        for i in range(0,n1):
            visited.append(False)
        dep = [0] * n1
        dep[s] = 1

        max_height = -1
        while(len(stack)>0):
            v = stack.pop()
            if(not visited[v]):                
                visited[v] = True
                # print(v, " ", end='')
                stack_aux = []
                for w in adjLists[v]:
                    if(not visited[w]):
                        dep[w] = dep[v] + 1
                        max_height = max(dep[w], max_height) 
                        stack_aux.append(w)
                while(len(stack_aux)>0):
                    stack.append(stack_aux.pop())
        # print(dep)
        return max_height

def main():
    tree = TreeHeight()
    tree.read()
    adjlists = tree.make_adj()

    print(tree.dfs_iterative(adjlists, tree.parent.index(-1)))

threading.Thread(target=main).start()
# if __name__ == "__main__":
    # main()