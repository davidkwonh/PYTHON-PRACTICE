class TreesNode:
    def __inite(self,data):
        self.data = data
        self.children = []
        self.Parent = None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

# Tree Practice

# def build_product_tree():
#     root = TreesNode("electronics")
#     laptop = TreesNode('Laptop')
#     laptop.add_child("MAC")
#     root.add_child(laptop)
#     return root

# BFS implementation
def bfs(V, adj)
    bfs_traverse = []
    vix = [False]*V
    for i in range(V):
        # check if visited
        if (vix[i] == False):
            q=[]
            vix[i] = True
            q.append(i)
            # BFS starting from the ith node
            while (len(q)>0):
                g_node = q.pop(0)

                bfs_traverse.append(g_node)
                for it in adj[g_node]:
                    if(vix[it]==False):
                        vix[it] = True
                        q.append(it)
    return bfs_traverse

def adjmat()



    if __name__ == '__main__':
        root = build_product_tree()
        pass