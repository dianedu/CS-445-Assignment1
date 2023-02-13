# Class to hold the topology of the network and to aid in the simulation
import node
from node import *

class Graph():
    # The Graph constructor takes in the number of nodes in the network and how the nodes are connected
    # The Nodes in the network are created in the Graph constructor
    def __init__(self, num_nodes : int, adjacency : list[list[int]]) -> None:
        self.nodes = []
        for i in range(num_nodes):
            self.nodes.append(Node(i))

        self.adjacency_matrix = adjacency
        for i, neighbors in enumerate(self.adjacency_matrix):
            for j,connection in enumerate(neighbors):
                if connection == 1:
                    self.nodes[i].add_neighbor(self.nodes[j])

    def __repr__(self) -> str:
        node = sorted(str(n) for n in self.nodes)
        return '\n'.join(node)

    def get_nodes(self) -> list[Node]:
        return self.nodes

    def get_adjacency_matric(self) -> list[list[int]]:
        return self.adjacency_matrix

# for ease of testing
if __name__ == "__main__":
# TEST:

    adj_list1 = [
                [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                                            ]

    g1 = Graph(21, adj_list1)
    print(g1,"\n")

    packet1 = Packet(0, 20)
    packet2 = Packet(7, 20)
    packet3 = Packet(11, 20)
    packet4 = Packet(16, 20)
    g1.get_nodes()[0].receive_packet(packet1)
    g1.get_nodes()[7].receive_packet(packet2)
    g1.get_nodes()[11].receive_packet(packet3)
    g1.get_nodes()[16].receive_packet(packet4)
    # for packet in  g1.get_nodes()[20].get_accepted_packets():
    #     print(packet)
   
    # cache_packet1 = RREQ_Packet(0, 4, 50)

    # for i in range(100):
    #     g1.get_nodes()[0].get_packet(copy.deepcopy(cache_packet1))

    # print(f"\nSuccess: {get_num_successes()}, Failures: {get_num_failures()}, Prob link Failure: {probability_of_link_failure}")
    # print(g1,"\n")