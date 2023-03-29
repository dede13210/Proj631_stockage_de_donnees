class NoeudsSysteme:
    def __init__(self,i,c,ld,ln):
        self.id=i
        self.capacite=c
        self.listIdData=ld
        self.listIdNode=ln

    def add_id_data(self, id_data):
        self.listIdData.append(id_data)

    def add_id_node(self, id_node):
        self.listIdNode.append(id_node)

