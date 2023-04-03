import heapq
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


def display_node(node):
    print(node.id, node.capacite)


def placer_au_plus_pres(donnee, user, list_node):
    if isinstance(user, Users):
        node = find_node(user.idNode, list_node)
        visited_node = [node]
        try:
            if placer_donnee_node(donnee, node):
                return True
        except:
            print(" 1 An exception occurred for data", donnee.id)

        while len(visited_node) < len(list_node):
            if len(node.listIdNode) == 1:
                node_bis = find_node(node.listIdNode)
                if node_bis not in visited_node:
                    try:
                        if placer_donnee_node(node_bis):
                            return True
                    except:
                        print("2 An exception occurred for data", donnee.id)
                    visited_node.append(node_bis)
                    print(visited_node)
            else:
                for neighbor in node.listIdNode:
                    node_bis = find_node(neighbor, list_node)
                    if node_bis not in visited_node and node_bis is not None:
                        try:
                            if placer_donnee_node(donnee, node_bis):
                                return True
                        except:
                            print("3 An exception occurred for data", donnee.id)
                    if node_bis is not None:
                        visited_node.append(node_bis)
                    for node in visited_node:
                        None
        print("plus de place disponible")
        return False
    if len(user) == 2:
        start = find_node(user[0].idNode, listNode)
        distance_user1, path1 = dijkstra(start, list_node)
        distance_user2, path2 = dijkstra(find_node(user[1].idNode, list_node), list_node)
        '''
        cpt = 1
        for no1, no2 in path2.items():
            print("cpt = ", cpt)
            display_node(no1)
            display_node(no2)
            cpt += 1
        '''
        # Initialisation de la file et du dictionnaire de visite
        queue = deque([start])
        visited = {node: False for node in list_node}

        # Marquer le nœud de départ comme visité
        visited[start] = True
        while queue:
            # Retirer le nœud le plus ancien de la file
            current_node = queue.popleft()
            # display_node(current_node)
            # on verifie que le noeud ai de la place puis on regarde la distance au deux users
            if current_node.capacite >= donnee.taille:
                if len(listNode) % 2 == 0 and distance_user1[current_node] - 1 <= distance_user2[current_node] <= \
                        distance_user1[current_node] + 1:
                    return placer_donnee_node(donnee, current_node)
                if len(listNode) % 2 == 1 and distance_user1[current_node] <= distance_user2[current_node]:
                    return placer_donnee_node(donnee, current_node)

                # Parcourir les voisins du nœud actuel
            for neighbors in current_node.listIdNode:
                neighbor = find_node(neighbors, list_node)
                # Si le voisin n'a pas été visité, le marquer comme visité et l'ajouter à la file
                if neighbor is not None:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)


def dijkstra(start_node, list_node):
    # Initialisation des distances et du chemin
    distances = {node: float('inf') for node in list_node}
    distances[start_node] = 0
    path = {}

    # Création d'une file de priorité pour stocker les nœuds à visiter
    pq = [(0, start_node)]
    while pq:
        # Obtenir le nœud avec la plus petite distance
        (current_dist, current_node) = heapq.heappop(pq)

        # Si on a déjà visité ce nœud, passer au suivant
        if current_dist > distances[current_node]:
            continue

        # Parcourir les voisins du nœud actuel
        for neighbor in current_node.listIdNode:
            neighbors = find_node(neighbor, list_node)
            if neighbors is not None:
                # Calculer la nouvelle distance
                distance = 1  # On suppose que le graphe est non pondéré
                new_distance = distances[current_node] + distance

                # Si la nouvelle distance est plus courte que la distance actuelle, mettre à jour la distance et le chemin
                if new_distance < distances[neighbors]:
                    distances[neighbors] = new_distance
                    path[neighbors] = current_node
                    # Ajouter le voisin à la file de priorité pour être visité plus tard
                    heapq.heappush(pq, (new_distance, neighbors))

    return distances, path


def mkp_glouton(list_donnee, liste_node):
    """
    Résout le problème du sac à dos multiple à l'aide d'un algorithme glouton.

    :param list_donnee: une liste d'objets à placer dans les sacs à dos
    :param liste_node: une liste de sacs à dos avec leur capacité maximale
    :return: une solution au problème du sac à dos multiple
    """

    # Tri des objets par ordre de valeur décroissante par unité de poids
    list_donnee = sorted(list_donnee, key=lambda obj: obj.taille, reverse=True)

    # Initialisation des sacs à dos avec des quantités nulles pour chaque objet
    solution = {obj: {knapsack: 0 for knapsack in liste_node} for obj in list_donnee}

    # Placement des objets dans les sacs à dos
    for obj in list_donnee:
        for knapsack in liste_node:
            if obj.taille <= knapsack.capacite:
                solution[obj][knapsack] = 1
                placer_donnee_node(obj, knapsack)
                break

    return solution




def get_donnee_by_user(user, id_donnee):
    for iddonne in user.listIdData:
        if iddonne == id_donnee:
            print("vous avez acces à la donnee")
            return True
    print("vous n'avez pas acces à la donnee")
    return False


if __name__ == '__main__':
    data0 = Donnees(40)
    data1 = Donnees(50)
    data2 = Donnees(40)
    data3 = Donnees(30)

    hugo = Users(1, [7], 6)
    adam = Users(2, [8], 4)
    benoit = Users(3, [8], 6)

    node0 = NoeudsSysteme(4, 40, [], [7, 5])
    node1 = NoeudsSysteme(5, 40, [], [4, 6, 2])
    node2 = NoeudsSysteme(6, 50, [], [5, 1])
    node3 = NoeudsSysteme(7, 40, [], [4])

    listNode = [node0, node1, node2, node3]

    '''Question 2
    placer_au_plus_pres(data1, adam, listNode)
    placer_au_plus_pres(data0, hugo, listNode)
    placer_au_plus_pres(data2, adam, listNode)
    placer_au_plus_pres(data3, benoit, listNode)'''

    '''Question 3
    placer_au_plus_pres(data3, adam, listNode)
    placer_au_plus_pres(data0, hugo, listNode)
    placer_au_plus_pres(data2, [adam, benoit], listNode)'''

    # Question 4
    mkp_glouton([data0, data1, data2, data3], [node1, node2, node0, node3])
