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
	h.heapifyUp(len(h.nodes) - 1)
}

// Helper function to maintain heap property when a node is added
func (h *MinHeap) heapifyUp(index int) {
	for index > 0 {
		parent := (index - 1) / 2
		if h.Less(index, parent) {
			h.Swap(index, parent)
			index = parent
		} else {
			break
		}
	}
}

func (h *MinHeap) Pop() interface{} {
	n := len(h.nodes)
	node := h.nodes[n-1]
	h.nodes = h.nodes[:n-1]

	delete(h.indexMap, node.coords)
	// Heapify down from the root to restore the heap property
	h.heapifyDown(0)

	return node
}

// Helper function to maintain heap property when a node is removed
func (h *MinHeap) heapifyDown(index int) {
	n := len(h.nodes)
	for {
		left := 2*index + 1
		right := 2*index + 2
		smallest := index

		if left < n && h.Less(left, smallest) {
			smallest = left
		}
		if right < n && h.Less(right, smallest) {
			smallest = right
		}
		if smallest == index {
			break
		}
		h.Swap(index, smallest)
		index = smallest
	}
}

// O(1) function to get the node at given coordinates
func (h *MinHeap) GetNodeAtCoords(coords Coords) (Node, bool) {
	index, found := h.indexMap[coords]
	if !found {
		return Node{}, false
	}
	return h.nodes[index], true
}
