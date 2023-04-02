from collections import deque

from Donnees import Donnees
from NoeudsSysteme import NoeudsSysteme
from Users import Users


def find_node(id_node, list_node):
    for node in list_node:
        if node.id == id_node:
            return node
    return None


def placer_donnee_node(donnee, node):
    if donnee.taille <= node.capacite:
        node.listIdData.append(donnee.id)
        node.capacite -= donnee.taille
        print("la donnee", donnee.id, "est placer dans le noeud", node.id)
        return True
    return False


def displayNode(node):
    print(node.id, node.capacite)


def placer_au_plus_pres(donnee, user, list_node):
    node = find_node(user.idNode, list_node)
    visited_node = [node]
    try:
        if placer_donnee_node(donnee, node):
            return True
    except:
        print(" 1 An exception occurred for data", donnee.id)

    while len(visited_node) != len(list_node):
        if len(node.listIdNode) == 1:
            node_bis = find_node(node.listIdNode)
            if node_bis not in visited_node:
                try:
                    if placer_donnee_node(node_bis):
                        return True
                except:
                    print("2 An exception occurred for data", donnee.id)
                visited_node.append(node_bis)
        else:
            for neighbor in node.listIdNode:
                node_bis = find_node(neighbor, list_node)
                if node_bis not in visited_node and node_bis is not None:
                    try:
                        if placer_donnee_node(donnee, node_bis):
                            return True
                    except:
                        print("3 An exception occurred for data", donnee.id)
                    visited_node.append(node_bis)
    return False


if __name__ == '__main__':
    data0 = Donnees(40)
    data1 = Donnees(50)
    data2 = Donnees(40)

    hugo = Users(1, [7], 6)
    adam = Users(2, [8], 6)
    benoit = Users(3, [8], 6)

    node0 = NoeudsSysteme(4, 40, [], [5])
    node1 = NoeudsSysteme(5, 40, [], [4, 6])
    node2 = NoeudsSysteme(6, 50, [], [5, 1, 2, 3])

    listNode = [node0, node1, node2]

    placer_au_plus_pres(data1, hugo, listNode)
    placer_au_plus_pres(data0, hugo, listNode)
    placer_au_plus_pres(data2, adam, listNode)
