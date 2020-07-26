from .nodeheapmap import Node, NodeHeapMap


class SolutionWithoutHeapMap:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        result = []
        height = []
        paired_item = {}
        for left, right, h in buildings:
            neg_node = Node(-h)
            pos_node = Node(h)
            height.append([left, neg_node])
            height.append([right, pos_node])
            paired_item[neg_node] = pos_node
            paired_item[pos_node] = neg_node

        height = sorted(height, key=lambda x: (x[0], x[1].val))
        nodeheapmap = NodeHeapMap()
        q = []
        nodeheapmap.heap_push(q, Node(0))

        pre = 0
        for x, h_node in height:
            if h_node.val < 0:
                nodeheapmap.heap_push(q, h_node) # it is already minimum
            else:
                nodeheapmap.heap_pop(q, paired_item[h_node])

            curr = nodeheapmap.peek(q).val

            if pre != curr:
                result.append([x, abs(curr)])
                pre = curr

        return result
