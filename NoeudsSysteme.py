class NoeudsSysteme:
    def __init__(self, i: object, c: object, ld: object, ln: object) -> object:
        self.id = i
        self.capacite = c
        self.listIdData = ld
        self.listIdNode = ln

    def add_id_data(self, id_data):
        self.listIdData.append(id_data)

    def add_id_node(self, id_node):
        self.listIdNode.append(id_node)

    def display(self):
        print("id = ", self.id, "capacité = ", self.capacite)
