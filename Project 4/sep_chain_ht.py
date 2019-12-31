from linked import *

def hash_string(string, size):
    hash = 0
    for c in string:
        hash = (hash*31 + ord(c)) % size
    return hash

class MyHashTable:
    def __init__(self, table_size=11):
        self.table = [None]* table_size
        self.tsize = table_size
        self.items = 0
        self.num_collisions = 0

    def __repr__(self):
        items = ""
        for item in self.table:
            items += "%s" % (item) + "->"
        items = items[:-2]
        return "Hash Table: [" + items + "]"

    def __eq__(self, other):
        return isinstance(other, MyHashTable) and self.table == other.table

    def put(self, key, data):
        hash_val = hash_string(key, self.tsize)
        node = Node((key, data))
        if self.table[hash_val] is not None:
            if self.table[hash_val].data[0] == key:
                return
            node.next = self.table[hash_val]
        self.table[hash_val] = node
        self.items += 1
        if (self.items/self.tsize) > 1.5:
            old = self.table
            old_size = self.tsize
            self.items = 0
            self.tsize = 2*self.tsize + 1
            self.table = [None] * self.tsize
            self.put_list_help(old)

    def put_list_help(self, table):
        for node in table:
            if node is not None:
                cur_node = node
                while cur_node is not None:
                    self.put(cur_node.data[0], cur_node.data[1])
                    cur_node = cur_node.next


    def get(self, key):
        hash_val = hash_string(key, self.tsize)
        item = self.table[hash_val]
        while item is not None:
            if item.data[0] == key:
                return item.data[1]
            item = item.next
        raise LookupError("The key was not found")

    def contains(self, key):
        hash_val = hash_string(key, self.tsize)
        item = self.table[hash_val]
        while item is not None:
            if item.data[0] == key:
                return True
            item = item.next
        return False

    def  remove(self, key):
        hash_val = hash_string(key, self.tsize)
        item = self.table[hash_val]
        temp = self.table[hash_val]
        while item is not None:
            data = item.data
            if item.data[0] == key:
                if temp == item:
                    self.table[hash_val] = item.next
                temp.next = item.next
                return data
            temp = item
            item = item.next
        raise LookupError("key not found")

    def size(self):
        return self.items

    def load_factor(self):
        return self.items/self.tsize

    def collisions(self):
        for item in self.table:
            while item is not None and item.next is not None:
                self.num_collisions += 1
                item = item.next
        return self.num_collisions

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def make_table(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        for i in lines:
            words = i.split()
        for j in words:
            self.put(j, j)
