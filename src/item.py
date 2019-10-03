class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on__take(self):
        print(f"You have picked up: {self.name}")

    def on__drop(self):
        print(f"You have dropped: {self.name}")
