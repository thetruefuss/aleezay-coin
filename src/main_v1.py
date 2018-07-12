import hashlib


class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash = hashlib.sha256()
        hash.update(
            (str(self.index)
            +str(self.previous_hash)
            +str(self.timestamp)
            +str(self.data)).encode()
        )
        hash = str(hash.hexdigest())
        return hash


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "01/01/2017", "Genesis block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


aleezay_coin = Blockchain()
aleezay_coin.add_block(Block(1, "20/07/2017", { "amount": 4 }))
aleezay_coin.add_block(Block(2, "20/07/2017", { "amount": 8 }))

print("Blockchain valid? ", aleezay_coin.is_chain_valid())

print("Changing a block...")
aleezay_coin.chain[1].data = { "amount": 100 }

print("Blockchain valid? ", aleezay_coin.is_chain_valid())
