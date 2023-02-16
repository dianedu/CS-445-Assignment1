# Main file to run for the simulation for the CPE 400 Final Project
# CPE 400 - Final Project
# Diane Du, Kalista Hong, Abida Mim
# December 12, 2022

import graph
from graph import *
import node
from node import *

def analyze_node_sampling(packets: list):
    nodes_dict = dict()
    for packet in packets:
        if packet.get_start_mark() != None:
            if packet.get_start_mark() in nodes_dict.keys():
                nodes_dict[packet.get_start_mark()] = nodes_dict[packet.get_start_mark()] + 1
            else:
                nodes_dict[packet.get_start_mark()] = 1
    print(sorted(nodes_dict.items(), key=lambda x:x[1]))

def analyze_edge_sampling(packets: list):
    pass


# main function for simluation
if __name__ == "__main__":
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

    for i in range(100):
        g1.get_nodes()[0].receive_packet(copy.deepcopy(packet1))

    for i in range(10):
        g1.get_nodes()[7].receive_packet(copy.deepcopy(packet2))
        g1.get_nodes()[11].receive_packet(copy.deepcopy(packet3))
        g1.get_nodes()[16].receive_packet(copy.deepcopy(packet4))

    if TYPE == "NODE":
        analyze_node_sampling(g1.get_nodes()[20].get_accepted_packets())
    elif TYPE == "EDGE":
        analyze_edge_sampling(g1.get_nodes()[20].get_accepted_packets())