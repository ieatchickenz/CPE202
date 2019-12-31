from sep_chain_ht import *

def make_list(filename):
    """This function opens a file and makes a list of words that appear in the file
        Args:
            filename(File) - the file that is read
        Return:
            list_words(list) - a list of words that appear in the file
    """
    file = open(filename, "r")
    list_lines = file.readlines()
    file.close()
    list_words = []

    for item in list_lines:
        table = str.maketrans("?!,./:;'",8*" ")
        new_str = item.translate(table)
        word = new_str.split()
        list_words.append(word)
    for i in list_words:
        for word in range(0, len(i)):
            i[word] = i[word].lower()
    return list_words

def remove_stopwords(list_words):
    """This function removes the stop words from the list of words
        Args:
            list_words(list) - a list of words that appear in the file
        Return:
            new(list) - list_words that doesn't contain stop words
    """
    new = list_words.copy()
    h = MyHashTable()
    h.make_table("stop_words.txt")
    for i in list_words:
        if h.contains(i):
          new.remove(i)
    return new

def get_lines(line_list, key):
    """This function finds the lines that each words in a list is found in a file
        Args:
            line_list(list) - a list of lines froms the file
            key(string) - a certain word
        Returns:
            lines(list) - a list of integers that represent line numbers
    """
    lines = []
    for i in range(0, len(line_list)):
        for j in line_list[i]:
            if j == key:
                lines.append(i + 1)
    return lines

class LinearHash():
    """A hash table that utilizes linear probing
        Args:
            table(list) - the hash table
            tsize(int) - the size of the table
            items(int) - the number of items stored in the table
    """
    def __init__(self, table_size=11):
        self.table = [None]* table_size
        self.tsize = table_size
        self.items = 0

    def __repr__(self):
        items = ""
        for item in self.table:
            items += "%s" % (str(item)) + "->"
        items = items[:-2]
        return "Hash Table: [" + items + "]"

    def __eq__(self, other):
        return isinstance(other, MyHashTable) and self.table == other.table

    def put_linear(self, key, line_list):
        """This function inserts a key into a hash table
            Args:
                key(string) - the key that determines its location in the hash table
                line_list(list) - the list of lines from the file to determine int location
            Returns:
                This function returns nothing but updates the hash.table
        """
        hash_val = hash_string(key, self.tsize)
        og_hash = hash_string(key, self.tsize)
        line = get_lines(line_list, key)
        node = (key, line)
        while self.table[hash_val] is not None:
            if self.table[hash_val][0] == key:
                return
            hash_val += 1
            if hash_val > self.tsize - 1:
                hash_val = 0
            if hash_val == og_hash:
                return
        self.table[hash_val] = node
        self.items += 1
        if (self.items/self.tsize) > .75:
            old = self.table
            old_size = self.tsize
            self.items = 0
            self.tsize = 2*self.tsize + 1
            self.table = [None] * self.tsize
            for item in old:
                if item is not None:
                    self.put_linear(item[0], line_list)

    def make_table_linear(self, filename):
        """This function takes the list with no stopwords and inserts them
            into a hash table
            Args:
                fliename(file) - the file inputed
            Returns:
                this function updates 
        """
        file = open(filename, "r")
        lines = file.readlines()
        for i in lines:
            words = i.split()
        for j in words:
            self.put_linear(j, j)   

    def get_tablesize(self):
        """This 
        """
        return self.tsize

    def read_file(self, filename):
        """
        """
        file = open(filename, "r")
        list_lines = file.readlines()
        file.close()
        list_words = []

        for item in list_lines:
            table = str.maketrans("?!,./:;'",8*" ")
            new_str = item.translate(table)
            word = new_str.split()
            list_words.append(word)
        list_use_words = []
        sorted_list = []
        for string in list_words:
            for word in string:
                lower = word.lower()
                list_use_words.append(lower)

        sorted_list = sorted(list_use_words, key=str.lower)
        final = remove_stopwords(sorted_list)
        line_list = make_list(filename)
        self.make_new_hash(final, line_list)

    def make_new_hash(self, list_no_stop, line_list):
        """
        """
        for i in list_no_stop:
            self.put_linear(i, line_list)

    def save_concordance(self, output_file):
        """
        """
        string = ""
        sort = []
        sorted_list = []
        file = open(output_file, "w")
        for i in self.table:
            if i is not None:
                sort.append(i)
        def custom_sort(listings):
            """
            """
            return listings[0]
        sorted_list = sorted(sort, key=custom_sort)
        for i in sorted_list:
            for j in i[1]:
                string += (" " + str(j))
            file.write(i[0] + " :" + string + "\n")
            string = ""
        file.close()

    def get_load_factor(self):
        """
        """
        return self.items/self.tsize

    def hash_string(self, key, table_size):
        """The hash value equation
            Args:
                key(string) - the object being put into the hash table
                table_size(int) - the size of the table
            Returns:
                hash(int) - an integer that determines the index at which to place the key
        """
        hash = 0
        for c in key:
            hash = (hash*31 + ord(c)) % table_size
        return hash

class QuadHash():
    """
    """
    def __init__(self, table_size=11):
        self.table = [None]* table_size
        self.tsize = table_size
        self.items = 0
        self.num_collisions = 0

    def __repr__(self):
        items = ""
        for item in self.table:
            items += "%s" % (str(item)) + "->"
        items = items[:-2]
        return "Hash Table: [" + items + "]"

    def __eq__(self, other):
        return isinstance(other, QuadHash) and self.table == other.table

    def put_quad(self, key, line_list):
        """
        """
        hash_val = hash_string(key, self.tsize)
        og_hash = hash_string(key, self.tsize)
        num_seq = 0
        line = get_lines(line_list, key)
        node = (key, line)
        while self.table[hash_val] is not None:
            if self.table[hash_val][0] == key:
                return
            num_seq += 1
            hash_val += (hash_val + (num_seq)**2)%self.tsize
            if hash_val > self.tsize - 1:
                hash_val = 0
            if hash_val == og_hash:
                return
        num_seq = 0
        self.table[hash_val] = node
        self.items += 1

        if (self.items/self.tsize) > .75:
            old = self.table
            old_size = self.tsize
            self.items = 0
            self.tsize = 2*self.tsize + 1
            self.table = [None] * self.tsize
            for item in old:
                if item is not None:
                    self.put_quad(item[0], line_list)   

    def get_tablesize(self):
        """
        """
        return self.tsize

    def read_file(self, filename):
        """
        """
        file = open(filename, "r")
        list_lines = file.readlines()
        file.close()
        list_words = []

        for item in list_lines:
            table = str.maketrans("?!,./:;'",8*" ")
            new_str = item.translate(table)
            word = new_str.split()
            list_words.append(word)
        list_use_words = []
        sorted_list = []
        for string in list_words:
            for word in string:
                lower = word.lower()
                list_use_words.append(lower)

        sorted_list = sorted(list_use_words, key=str.lower)
        final = remove_stopwords(sorted_list)
        line_list = make_list(filename)
        self.make_new_hash(final, line_list)

    def make_new_hash(self, list_no_stop, line_list):
        """
        """
        for i in list_no_stop:
            self.put_quad(i, line_list)

    def save_concordance(self, output_file):
        """
        """
        string = ""
        sort = []
        sorted_list = []
        file = open(output_file, "w")
        for i in self.table:
            if i is not None:
                sort.append(i)
        def custom_sort(listings):
            return listings[0]
        sorted_list = sorted(sort, key=custom_sort)
        for i in sorted_list:
            for j in i[1]:
                string += (" " + str(j))
            file.write(i[0] + " :" + string + "\n")
            string = ""
        file.close()

    def get_load_factor(self):
        """
        """
        return self.items/self.tsize

    def hash_string(self, key, table_size):
        """The hash value equation
            Args:
                key(string) - the object being put into the hash table
                table_size(int) - the size of the table
            Returns:
                hash(int) - an integer that determines the index at which to place the key
        """
        hash = 0
        for c in key:
            hash = (hash*31 + ord(c)) % table_size
        return hash 

yuh = OtherHash()
yo = QuadHash()
yuh.read_file("linear_probing.txt")
yo.read_file("quadratic_probing.txt")
print(yuh)
print(yo)
# print(yuh==yo)
# yuh.save_concordance("concord2.txt")
# yo.save_concordance("concord2a.txt")