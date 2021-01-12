# Huffman Encoding implementation (Basic)

import heapq


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def huffman_encode(chars, frequencies):
    min_heap = []
    special_counter = 0
    for i in range(len(chars)):
        heap_node = (frequencies[i], special_counter, Node(chars[i]))
        heapq.heappush(min_heap, heap_node)
        special_counter += 1

    while len(min_heap) > 1:
        w1, _, node1 = heapq.heappop(min_heap)
        w2, _, node2 = heapq.heappop(min_heap)

        node = Node('')
        node.left = node1
        node.right = node2

        heap_node = (w1 + w2, special_counter, node)
        heapq.heappush(min_heap, heap_node)
        special_counter += 1

    _, __, root = heapq.heappop(min_heap)

    huffman_codes = {}
    if not root.right and not root.left:
        huffman_codes[root] = 0
    else:
        encode_values(root, [], huffman_codes)

    # print('Char |', ' Code')
    # for char, code in huffman_codes.items():
    #     print(f'{char}    | {code}')

    return huffman_codes


def encode_values(node, code, huffman_codes):
    if not node.left and not node.right:
        huffman_codes[node.value] = ''.join(code)
    else:
        if node.left:
            code.append('0')
            encode_values(node.left, code, huffman_codes)
            code.pop()

        if node.right:
            code.append('1')
            encode_values(node.right, code, huffman_codes)
            code.pop()


if __name__ == '__main__':
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    frequencies = [40, 20, 15, 7, 5, 5, 2, 2, 1]

    print(huffman_encode(chars, frequencies))


