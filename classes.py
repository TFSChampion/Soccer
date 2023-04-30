class Bot:

    def __init__(self, name: str, leader: bool):
        
        self.name = name
        self.leader = bool

    def test(self):

        if self.leader:

            print(f"Hello, my name is {self.name} and I am the leader.")

        else:

            print(f"Hello, my name is {self.name} and I am not the leader.")