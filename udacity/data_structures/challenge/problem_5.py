import datetime
import hashlib


class Block:

    def __init__(self, data, previous_block):
        self.timestamp: str = self.get_timestamp()
        self.data = data
        self.previous_block = previous_block
        if previous_block is not None:
            self.previous_hash = previous_block.hashcode
        self.hashcode = self.calc_hash()

    def calc_hash(self) -> str:
        sha = hashlib.sha256()

        string_to_hash = ""

        if self.data is not None:
            string_to_hash += self.data

        if self.timestamp is not None:
            string_to_hash += str(self.timestamp)

        if self.previous_block is not None:
            string_to_hash += self.previous_block.hashcode

        sha.update(string_to_hash.encode("utf-8"))

        return sha.hexdigest()

    @staticmethod
    def get_timestamp():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    def __str__(self):
        return self.data


class BlockChain:
    def __init__(self):
        self.tail = None
        self.blocks = dict()

    def register_transaction(self, data):
        if data is None:
            return

        block = Block(
            data=data,
            previous_block=self.tail
        )

        self.tail = block
        self.blocks.setdefault(block.hashcode, block)

        return block.hashcode

    def get_data(self, hashcode: str):
        return self.blocks.get(hashcode)

    def print_transactions_by_oldest(self):
        block: Block = self.tail
        while block:
            print(block)
            block = block.previous_block


block_chain = BlockChain()

first_transaction_hash = block_chain.register_transaction("first transaction")
second_transaction_hash = block_chain.register_transaction("second transaction")
third_transaction_hash = block_chain.register_transaction("third transaction")
fourth_transaction_hash = block_chain.register_transaction(None)

block_chain.print_transactions_by_oldest()
