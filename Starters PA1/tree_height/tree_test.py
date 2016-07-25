# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
# threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def tree_struct(self, root, nodes):
        tree_dic = {'root':root, 'children': []}
        children = [ind for ind, node in enumerate(nodes) if node == root]
        for child in children:
            tree_dic['children'].append(self.tree_struct(child, nodes))
        return tree_dic

    def compute_height(self, tree_structure):
        if tree_structure['children'] == []:
            return 0
        else:
            return 1 + max(self.compute_height(i) for i in tree_structure['children'])

def main():
    tree = TreeHeight()
    tree.read()
    tree_total = tree.tree_struct(-1, tree.parent)
    # print(tree_total)
    print(tree.compute_height(tree_total))

# threading.Thread(target=main).start()
if __name__ == "__main__":
    main()