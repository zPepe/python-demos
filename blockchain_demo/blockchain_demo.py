# import of required libraries
import hashlib as hasher  # library we can use to implement many secure hash and message digest algorithms
import datetime as date  # this one lets you use the date and time of the system and use it in the code


# declaration of the class Block, so that we can create multiple blocks objects from it
class Block:
    # construtor and variables initialization
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

        # This function will take the previous block hash and use it to hash the data of the present block
        # returning an unique hash
        def hash_block():
                # use the library with the method "sha256()", to create a hash of that type
            sha = hasher.sha256()
            # use the variable "sha" to hash the attributes of the block
            sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') +
                       str(self.data).encode('utf-8') +
                       str(self.previous_hash).encode('utf-8'))

            # return one unique hash of everything
            return sha.hexdigest()

        # the variable "hash" will call the function by the name "hash_block", and it will be equal to the value that the
        # function returns
        self.hash = hash_block()


# This function creates the first block of the chain, with hardcoded values
def genesis_block():
    return Block(0, date.datetime.now(), "Microsoft is simply best OS there is...jk", "12345")


# Function returns the next block to be inserted in the blockchain
# Takes the previous block, wich is an object in a specific index of the blockchain, as an argument
def next_block(previous_block):
    # it moves up 1 postion in the index of the blockchain
    this_index = previous_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hi! I'm block number " + str(this_index)
    # the variable "this_hash" is gonna call the function "hash_block" as you can see from the "self.hash" variable in class Block
    # so this hash will be an hash sum of the block data with the previous block hash
    this_hash = previous_block.hash

    # returns the next block to be appended in the blockchain
    return Block(this_index, this_timestamp, this_data, this_hash)



# declaration of the blockchain with the first block hardcoded
blockchain = [genesis_block()]
# variable "previous_block" is equal to the object in position 0, which is the genesis block
previous_block = blockchain[0]

# asking user input for the number of blocks to implement in the blockchain
num_of_blocks_to_add = input("Number of blocks to add in the chain: ")


# for loop, to iterate from 0 to the number of the input received from the user
for i in range(0, int(num_of_blocks_to_add)):
    block_to_add = next_block(previous_block)
    # append the block
    blockchain.append(block_to_add)
    # set the variable "previous_block" to be the block that we just add, so we can use it in the hashing process for the next one
    previous_block = block_to_add
    # print the block index and its hash
    print('Block:' + str(block_to_add.index) + ' has been added to the blockchain!')
    print('Hash:' + block_to_add.hash)
