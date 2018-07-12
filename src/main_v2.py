import hashlib


class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash = hashlib.sha256()
        hash.update(
            (str(self.index)
            +str(self.previous_hash)
            +str(self.timestamp)
            +str(self.data)
            +str(self.nonce)).encode()
        )
        hash = str(hash.hexdigest())
        return hash

    def mine_block(self, difficulty):
        difficulty_str = "".join(["0" for i in range(0, difficulty)])
        while self.hash[0:difficulty] != difficulty_str:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("BLOCK MINED: ", self.hash)


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 5

    def create_genesis_block(self):
        return Block(0, "01/01/2017", "Genesis block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
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

print("Mining block 1...")
aleezay_coin.add_block(Block(1, "20/07/2017", { "amount": 4 }))

print("Mining block 2...")
aleezay_coin.add_block(Block(2, "20/07/2017", { "amount": 8 }))
