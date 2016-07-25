# python3

import sys
import threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
    
    def compute_height(self):
        num = self.n
        num_list = self.parent
        if len(num_list) == 0:
            return 0
        if len(num_list) == 1:
            return 1
        height = 0
        root = num_list.index(-1)
        # print("root is " + str(root))
        for i in range(num):
            # print("checking i = "+str(i))
            if i not in num_list and root != i:
                depth = 0
                check = i
                while check != root:
                    check = num_list[check]
                    depth += 1
                depth += 1
                if depth > height:
                    height = depth
        return height
 

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

task = threading.Thread(target=main)
task.start()
# if __name__ == "__main__":
#     main()