from Donnees import Donnees



class System:
    def __init__(self):
        self.listNodes = []

    def add_node(self, node):
        self.listNodes.append(node)

    def find_node(self, id_node):
        for node in self.listNodes:
            if node.id == id_node:
                return node

    def placer_donnee_node(self, donnee, node):
        if donnee.taille <= node.capacite:
            node.listIdData.append(donnee.id)
            return True
        return False

    def place_donnees(self, donnee, user):
        node = self.find_node(user.idNode)
        list_node = []
        list_node.extend(self.listNodes)
        list_node.remove(node)
        if self.placer_donnee_node(donnee, node):
            print("la donnee", donnee.id, "est placer dans le noeud", node.id)
        else:
            for neighborId in node.listIdNode:
                if self.placer_donnee_node(donnee, self.find_node(neighborId)):
                    break
