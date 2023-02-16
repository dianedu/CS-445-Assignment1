# Main file to run for the simulation for the CPE 400 Final Project
# CPE 400 - Final Project
# Diane Du, Kalista Hong, Abida Mim
# December 12, 2022

import graph
from graph import *
import node
from node import *

correct_path =[6,5,4,3,2,1,0]
num_correct = 0
num_wrong = 0

def analyze_node_sampling(packets: list):
    nodes_dict = dict()
    for packet in packets:
        if packet.get_start_mark() != None:
            if packet.get_start_mark() in nodes_dict.keys():
                nodes_dict[packet.get_start_mark()] = nodes_dict[packet.get_start_mark()] + 1
            else:
                nodes_dict[packet.get_start_mark()] = 1
    return sorted(nodes_dict.items(), key=lambda x:x[1], reverse=True)

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
    
    for trial in range(10):
        for i in range(100):
            g1.get_nodes()[0].receive_packet(copy.deepcopy(packet1))

        for i in range(10):
            g1.get_nodes()[7].receive_packet(copy.deepcopy(packet2))
            g1.get_nodes()[11].receive_packet(copy.deepcopy(packet3))
            g1.get_nodes()[16].receive_packet(copy.deepcopy(packet4))

        if TYPE == "NODE":
            result = analyze_node_sampling(g1.get_nodes()[20].get_accepted_packets())
            if len(result) < 7:
                num_wrong += 1
            else:
                result_list = []
                for i in range(7):
                    result_list.append(result[i][0])
                if result_list == correct_path:
                    print("Correct",result_list, correct_path)
                    num_correct += 1
                else:
                    num_wrong += 1
                print("all",result_list, correct_path)
        elif TYPE == "EDGE":
            analyze_edge_sampling(g1.get_nodes()[20].get_accepted_packets())

    print(f"Num correct: {num_correct}, Num wrong: {num_wrong}, Total: {num_wrong + num_correct}, Accuracy: {num_correct/(num_wrong + num_correct)}")