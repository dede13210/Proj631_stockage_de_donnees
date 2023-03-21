from Donnees import Donnees
from NoeudsSysteme import NoeudsSysteme
from Utilisateurs import Utilisateurs

if __name__ == '__main__':

    data0 = Donnees(7,40)
    data1 = Donnees(8,50)

    hugo = Utilisateurs(1,[7],[6])
    Adam = Utilisateurs(2,[8],[6])
    benoit = Utilisateurs(3,[8],[6])

    node0 = NoeudsSysteme(4,40,[5],[])
    node1 = NoeudsSysteme(5,40,[4,6],[])
    node2 = NoeudsSysteme(6,50,[],[])








