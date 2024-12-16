package day16

type Node struct {
	f, g      int
	coords    Coords
	direction Coords
	parent    *Node
}

type MinHeap struct {
	nodes    []Node
	indexMap map[Coords]int
}

func (h MinHeap) Len() int {
	return len(h.nodes)
}

func (h MinHeap) Less(i, j int) bool {
	return h.nodes[i].f < h.nodes[j].f
}

func (h *MinHeap) Swap(i, j int) {
	h.nodes[i], h.nodes[j] = h.nodes[j], h.nodes[i]
	h.indexMap[h.nodes[i].coords] = i
	h.indexMap[h.nodes[j].coords] = j
}

func (h *MinHeap) Push(x interface{}) {
	node := x.(Node)
	h.nodes = append(h.nodes, node)
	if h.indexMap == nil {
		h.indexMap = make(map[Coords]int)
	}
	h.indexMap[node.coords] = len(h.nodes) - 1
}

func (h *MinHeap) Pop() interface{} {
	n := len(h.nodes)
	node := h.nodes[n-1]
	h.nodes = h.nodes[:n-1]

	delete(h.indexMap, node.coords)
	return node
}

// O(1) function to get the node at given coordinates
func (h *MinHeap) GetNodeAtCoords(coords Coords) (Node, bool) {
	index, found := h.indexMap[coords]
	if !found {
		return Node{}, false
	}
	return h.nodes[index], true
}
