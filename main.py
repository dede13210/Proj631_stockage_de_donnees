from Donnees import Donnees
from NoeudsSysteme import NoeudsSysteme
from System import System
from Users import Users

if __name__ == '__main__':
    system = System()

    data0 = Donnees(40)
    data1 = Donnees(50)

    hugo = Users(1, [7], 6)
    adam = Users(2, [8], 6)
    benoit = Users(3, [8], 6)

    node0 = NoeudsSysteme(4, 40, [], [5])
    node1 = NoeudsSysteme(5, 40, [], [4, 6])
    node2 = NoeudsSysteme(6, 50, [], [5, 1, 2, 3])

    system.add_node(node0)
    system.add_node(node1)
    system.add_node(node2)

    system.place_donnees(data1, hugo)
    system.place_donnees(data0, adam)
