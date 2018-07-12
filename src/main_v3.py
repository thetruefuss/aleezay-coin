import hashlib


class Transaction:
    def __init__(self, from_address, to_address, amount):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount


class Block:
    def __init__(self, timestamp, transactions, previous_hash=''):
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash = hashlib.sha256()
        hash.update(
            (str(self.previous_hash)
            +str(self.timestamp)
            +str(self.transactions)
            +str(self.nonce)).encode()
        )
        hash = str(hash.hexdigest())
        return hash

    def mine_block(self, difficulty):
        while self.hash[0:difficulty] != "".join(["0" for i in range(0, difficulty)]):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("BLOCK MINED: ", self.hash)


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []
        self.mining_reward = 100

    def create_genesis_block(self):
        return Block("01/01/2017", [], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address):
        block = Block("05/16/2018", self.pending_transactions, self.get_latest_block().hash)
        block.mine_block(self.difficulty)

        print('Block successfully mined!')
        self.chain.append(block)

        self.pending_transactions = [Transaction(None, mining_reward_address, self.mining_reward)]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance_of_address(self, address):
        balance = 0

        for block in self.chain:
            for trans in block.transactions:
                if trans.from_address == address:
                    balance -= trans.amount
                if trans.to_address == address:
                    balance += trans.amount

        return balance

    def isChainValid(self):
        for i in range(0, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash:
                return False
            if current_block.hash != previous_block.hash:
                return False
        return True


aleezay_coin = Blockchain()
t1 = Transaction('address1', 'address2', 100)
aleezay_coin.create_transaction(t1)
t2 = Transaction('address2', 'address1', 50)
aleezay_coin.create_transaction(t2)

print('Starting the miner...')
aleezay_coin.mine_pending_transactions('newbie-address')

print('Balance of newbie is ', aleezay_coin.get_balance_of_address('newbie-address'))

print('Starting the miner again...')
aleezay_coin.mine_pending_transactions('newbie-address')

print('Balance of newbie is ', aleezay_coin.get_balance_of_address('newbie-address'))
