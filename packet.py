# Class for packets that are being transmitted

class Packet():
    id_generator = 0
    def __init__(self, source : int, destination : int) -> None:
        self.id = Packet.id_generator
        self.src = source 
        self.dest= destination
        self.start_mark = None
        self.end_mark = None
        self.mark_distance = 0
        Packet.generate_new_id()

    def __repr__(self) -> str:
        return f"Source: {self.src}\nDestination: {self.dest}\nMark: {self.start_mark}\nEnd mark: {self.end_mark}\nMark distance: {self.mark_distance}"

    def get_src(self) -> int:
        return self.src
    
    def get_dest(self) -> int:
        return self.dest

    def get_id(self) -> int:
        return self.id

    def get_start_mark(self) -> int:
        return self.start_mark

    def get_end_mark(self) -> int:
        return self.end_mark
    
    def get_mark_distance(self) -> int:
        return self.mark_distance

    def set_dest(self, destination : int) -> None:
        self.dest = destination

    def set_start_mark(self, mark : int) -> None:
        self.start_mark = mark

    def set_end_mark(self, mark : int) -> None:
        self.end_mark = mark

    def set_mark_distance(self, distance : int) -> None:
        self.mark_distance = distance

    def increment_mark_dist(self) -> None:
        self.mark_distance += 1

    def nodeSamplingMark(self,router_mark : int) -> None:
        self.set_start_mark(router_mark)

    def edgeSamplingMark(self, router_mark : int) -> None:
        self.set_start_mark(router_mark)
        self.set_mark_distance(0) 
        # might need to reset end router... need to look into again

    @staticmethod
    def generate_new_id() -> None:
        Packet.id_generator += 1

# for testing purposes
if __name__ == "__main__":
    # TESTING Packet class and its methods:
    pass