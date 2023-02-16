# Class to create each router and each router's information 
import packet
from packet import *
import copy
import random

TYPE = "NODE" # "NODE" for node sampling, "EDGE" for edge sampling
P = 0.2 # prob of node marking the packet

# The Node class represents each router in the network and its neighbors
class Node():
    # The Node class contructor requires a Node label for identification
    # The Node class constructor is invoked in the Graph class
    def __init__(self, name : int) -> None: 
        self.label = name #ID of router
        self.adjacency_list = [] # Neighbors of the router
        self.packet = None  # Packet to forward
        self.packets_accepted = [] # packets accepted

    def __repr__(self) -> str:
        return f"{self.label}: {[n.get_label() for n in self.adjacency_list]}"

    def set_adjacency(self, adjacent_nodes : list) -> None:
        self.adjacency_list = adjacent_nodes

    def get_adjacency(self) -> list:
        return self.adjacency_list
    
    def get_label(self) -> int:
        return self.label

    def get_packet(self) -> Packet:
        return self.packet
    
    def get_accepted_packets(self):
        return self.packets_accepted

    def add_neighbor(self, new_neighbor) -> None:
        self.adjacency_list.append(new_neighbor)
        self.adjacency_list.sort(key=Node.get_label)

    # Method to broadcast RREQ packets to neighbors
    # @param    Packet to be transmitted
    # @return   None
    def broadcast_packet(self, packet : Packet) -> None:
        if packet != None:
            # print(f"\n{self.label} is attempting to broadcast packet: {packet.get_id()}")
            # print(f"RREQ Packet {packet.get_id()} is broadcasted to {[n.get_label() for n in self.adjacency_list]}\n")
            for node in self.adjacency_list:
                    node.receive_packet(copy.deepcopy(packet))

    # Method get packet transmitted
    # @param    Packet received
    # @return   None
    def receive_packet(self, packet : Packet) -> None:
        # print(f"{self.label} has received packet {packet.get_id()}")
        if packet != None:
            self.process_packet(copy.deepcopy(packet))

    # Upon getting packet, method to process the packet
    # @param    Packet to be processed
    # @return   None
    def process_packet(self, packet: Packet) -> None:
        # print(f"{self.label} is processing packet {packet.get_id()}")
        if packet != None:
            if packet.get_dest() == self.label:
                self.accept_packet(packet)
            else:
                if random.random() <= P:
                    if TYPE == "NODE":
                        packet.set_start_mark(self.label)
                    elif TYPE == "EDGE":
                        pass
                    else:
                        print("Invalid mode set")
                self.broadcast_packet(packet)
        
    # Method accept RREQ packet and perform any required actions when accepted
    # @param    Packet to be accept
    # @return   None
    def accept_packet(self, packet : Packet) -> None:
        if packet != None:
            # print(f"{self.label} accepted packet {packet.get_id()}")
            self.packets_accepted.append(packet)

    # Method to discard packets
    # @param    Packet to be discarded
    # @return   None
    def discard_packet(self, packet : Packet) -> None:
        # print(f"Packet with id {packet.get_id()} is discarded by {self.label}")
        packet = None

    # Helper method to get neighbor Node from its label
    # @param    Neighbor node label
    # @return   Node of desired neighbor
    def get_neighbor_node_from_label(self, label : int):
        for node in self.adjacency_list:
            if label == node.get_label():
                return node
 

# for ease of testing
if __name__ == "__main__":
    n1 = Node(1)
    #print(n1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1_neighbors = [n2,n3,n4,n5]
    n1.set_adjacency(n1_neighbors)
    print(n1)

    print("Testing random number generator")
    print(random.random())
    print(random.random())