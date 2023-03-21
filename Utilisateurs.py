class Utilisateurs:
    def __init__(self,i,l,n):
        self.id=i
        self.listIdData=l
        self.listIdNode=n

    def add_id(self, id_data):
        self.listIdData.append(id_data)

    def add_node(self, id_node):
        self.listIdNode.append(id_node)



