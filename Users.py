class Users:
    def __init__(self, i, l, n):
        self.id = i
        self.listIdData = l
        self.idNode = n

    def add_id(self, id_data):
        self.listIdData.append(id_data)
