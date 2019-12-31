"""
Alex Petrov
CPE 202
Project 3
"""
class Node:
    """Node class
        Args:
            frequency - frequency of item
            letter - letter stored in Node
            left - left child
            right - right child
            min_val - the minimum value of the letters stored in the children
    """
    def __init__(self, frequency, letter=None, left=None, right=None, min_val=None):
        self.key = frequency
        self.data = letter
        self.left = left
        self.right = right
        self.min_val = min_val
    def __repr__(self):
        return "Node(freq:%s, letter:%s, left:%s, right:%s, min_val:%s)" %\
         (self.key, self.data, self.left, self.right, self.min_val)
    def __eq__(self, other):
        return isinstance(other, Node) and self.data == other.data

def swap(arr, idx_one, idx_two):
    """This function swaps the data at two indicies
        Args:
            arr(list) - the list of items
            a(int) - index of first item in array
            b(int) - index of second item in array
        Returns:
            This function returns nothing
    """
    temp = arr[idx_one]
    arr[idx_one] = arr[idx_two]
    arr[idx_two] = temp

def insert(lists, data):
    """This function inserts data into a min heap
        Args:
            lists(list) - the min heap
            data - the data to be inserted
        Returns:
            This function returns nothing but updates the min heap
    """
    lists.append(data)
    shift_up(lists, len(lists)-1)

def shift_up(lists, idx):
    """This function shifts a min heap node up
        Args:
            lists(list) - the min heap
            idx(int) - the index that needs to shifted
        Returns:
            This function updates the min heap
    """
    idx_parent = index_parent(idx)
    if idx_parent < 0 or lists[idx_parent].key <= lists[idx].key:
        return
    swap(lists, idx, idx_parent)
    return shift_up(lists, idx_parent)

def dequeue(lists):
    """This function dequeues from the top of the min heap then shifts everything down
        Args:
            lists(list) - the min heap
        Returns:

    """
    if lists is None or lists == []:
        raise IndexError("Heap is Empty!")
    if len(lists) == 1:
        return lists.pop()
    min_item = lists[0]
    last_item = lists.pop()
    lists[0] = last_item
    shift_down(lists, 0)
    return min_item

def shift_down(lists, idx, end=None):
    """This function shifts everything in a tree down
        Args:
            lists(list) - the min heap
            idx(int) - the index at which everything shifts down
            end(int) - keeps track of the end of the tree
    """
    length = len(lists)
    if end is None:
        end = length - 1
    imin = index_minchild(lists, idx, end)
    if imin < 0:
        return None
    swap(lists, idx, imin)
    return shift_down(lists, imin, end)

def heapify(lists):
    """This function creates a min heap
        Args:
            lists(list) - a list of items
        Returns:
            This function returns nothing but modifys the list to become a min heap
    """
    length = len(lists)
    idx = index_parent(length - 1)
    while idx >= 0:
        shift_down(lists, idx)
        idx -= 1

def index_parent(idx):
    """This function finds the parent nodes from a specific index in a min heap
        Args:
            idx(int) - a specified index
        Returns:
            an integer which represents the index of the parent node
    """
    return (idx - 1)//2

def index_left(idx):
    """This function finds the left child nodes from a specific index in a min heap
        Args:
            idx(int) - a specified index
        Returns:
            an integer which represents the index of the left child node
    """
    return 2 * idx + 1

def index_right(idx):
    """This function finds the right child nodes from a specific index in a min heap
        Args:
            idx(int) - a specified index
        Returns:
            an integer which represents the index of the right child node
    """
    return 2 * idx + 2

def index_minchild(lists, idx, end):
    """This function finds the index of the child with the minimum value stored
        Args:
            lists(list) - the min heap
            idx(int) - starting index
            end - the end of the heap
    """
    idx_left = index_left(idx)
    idx_right = index_right(idx)
    if (idx_left > end or lists[idx].key <= lists[idx_left].key)\
        and (idx_right > end or lists[idx].key <= lists[idx_right].key):
        return -1
    if idx_right > end or lists[idx_left].key <= lists[idx_right].key:
        return idx_left
    return idx_right

def cnt_freq(filename):
    """This file parses through a file and creates a list of frequencies whos indecies
        correspond to ASCII values
        Args:
            filename(file) - the file that is opened and looked through
        Returns:
            freq_arr(list) - the list of frequencies
    """
    freq_arr = [0] * 255
    file = open(filename, 'r', encoding='utf-8')
    content = file.readlines()
    file.close()
    for i in content:
        for j in i:
            idx = ord(j)
            freq_arr[idx] += 1
    return freq_arr

def comes_before(var_one, var_two):
    """This function determines whether one node should come before the other
        Args:
            var_one(Node) - the first node
            var_two(Node) - the second node
        Returns:
            This function returns true if var_one is less than var_two, otherwise false
    """
    if var_one.key < var_two.key:
        return True
    if var_one.key == var_two.key:
        if ord(var_one.min_val) < ord(var_two.min_val):
            return True
        return False
    return False

def comes_before_letter(var_one, var_two):
    """This function determines whether one node should come before the other
        Args:
            var_one(Node) - the first node
            var_two(Node) - the second node
        Returns:
            This function returns true if var_one is less than var_two, otherwise false
    """
    if ord(var_one.min_val) < ord(var_two.min_val):
        return True
    return False


def create_huff_tree(list_of_freqs):
    """This function takes the frequency list and makes a min heap which
        is then made into a huffman tree
        Args:
            list_of_freqs(list) - a list of frequencies
        Returns:
            This function returns a huffman tree
    """
    node_list = []
    for i in range(0, len(list_of_freqs)-1):
        if list_of_freqs[i] != 0:
            node = Node(list_of_freqs[i], chr(i), None, None, chr(i))
            node_list.append(node)
    heapify(node_list)
    while len(node_list) > 1:
        item1 = dequeue(node_list)
        item2 = dequeue(node_list)
        new_freq = item1.key + item2.key
        if comes_before_letter(item1, item2):
            new_node = Node(new_freq, None, item1, item2, None)
            new_node.min_val = item1.min_val
        else:
            new_node = Node(new_freq, None, item2, item1, None)
            new_node.min_val = item2.min_val
        insert(node_list, new_node)
    return node_list[0]

def create_code(root_node):
    """This function creates a list of code strings that represent the characters in the file
        Args:
            root_node(MyHuffTree) - this is the root of the huffman tree
        Returns:
            str_list(list) - a list of length 255 with code strings at specific indecies
    """
    str_list = [""] * 256
    str_val = ""
    if root_node.left is not None:
        str_val = "0"
        create_code_help(root_node.left, str_val, str_list)
    if root_node.right is not None:
        str_val = "1"
        create_code_help(root_node.right, str_val, str_list)
    return str_list

def create_code_help(node, code, list_str):
    """This is a helper that creates the strings of code
        Args:
            node(Node) - a specific node from the huff tree
            code(str) - the string of code
            list_str(str) - the list of codes
        Returns:
            This function updates the string of code
    """
    if node.left is None and node.right is None:
        list_str[ord(node.data)] = code
        return 
    if node.left is not None:
        create_code_help(node.left, code + "0", list_str)
    if node.right is not None:
        create_code_help(node.right, code + "1", list_str)

def huffman_encode(in_file, out_file):
    """This function takes a file and encodes the content using a huffman tree and then writes
        it to an output file.
        Args:
            in_file(file) - a file to open and read
            out_file(file) - a file to write to
        Returns:
            This function returns nothing but an output file is written
    """
    ord_list = []
    huff_list = []
    freq = cnt_freq(in_file)
    root = create_huff_tree(freq)
    code_list = create_code(root)

    file_in = open(in_file, "r")
    line = file_in.readlines()
    file_in.close()
    for item in line:
        for j in item:
            ord_list.append(ord(j))
    for i in ord_list:
        huff_list.append(code_list[i])
    str_code = ""
    for i in huff_list:
        str_code += i
    file = open(out_file, "w")
    file.write(str_code)
    file.close()

def tree_preorder(hufftree):
    """This function writes a representation of a hufftree as a string of "0"s, "1"s, and letters
        Args:
            hufftree(MyHuffTree) - the huffman tree
        Returns:
            A string of "0"s, "1"s, and letters
    """
    code = [""]
    tree_preorder_help(hufftree, code)
    return "".join(code)

def tree_preorder_help(hufftree, code):
    """Helper function to go through a tree in preorder
        Args:
            hufftree(MyHuffTree) - the huffman tree
            code(str) - the string
        Returns:
            This function updates the code
    """
    if hufftree.left is None and hufftree.right is None:
        bit = ["1"] + [hufftree.data]
        code += bit
    else:
        code += ["0"]
        tree_preorder_help(hufftree.left, code)
        tree_preorder_help(hufftree.right, code)

def huffman_decode(list_of_freqs, encoded_file, decode_file):
    """This function takes a file that has been encoded and decodes it
        Args:
            list_of_freqs(list) - the list of frequency created earlier
            encoded_file(file) - the file that contains the encoded version of a string
            decoded_file(file) - the file that is opened to write the solution to
        Returns:
            This function updates a solution file
    """
    tree = create_huff_tree(list_of_freqs)
    num_items = 0
    item = ""
    freq = 0
    for i in range(0, len(list_of_freqs)):
        if list_of_freqs[i] != 0:
            num_items += 1
            item = chr(i)
            freq = list_of_freqs[i]
    cur_node = tree
    decoded = ""
    try:
        file = open(encoded_file, 'r')
    except IOError:
        raise IOError("This file does not exist!")
    bits = file.readlines()
    file.close()
    for i in bits:
        for j in i:
            if j == "0":
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
            if cur_node.right is None and cur_node.left is None:
                decoded += cur_node.data
                cur_node = tree
    if num_items == 1:
        decoded = item + " " + str(freq) #if the file only contains one letter
    decoded_file = open(decode_file, "w")
    decoded_file.write(decoded)
    decoded_file.close()
