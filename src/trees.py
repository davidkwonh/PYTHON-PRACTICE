class TreesNode:
    def __inite(self,data):
        self.data = data
        self.children = []
        self.Parent = None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreesNode("electronics")
    laptop = TreesNode('Laptop')
    laptop.add_child("MAC")



    root.add_child(laptop)
    return root


    if __name__ == '__main__':
        root = build_product_tree()
        pass