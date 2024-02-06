from random import choice
class Placement:
    @staticmethod
    def random_placement(vertexes:list[int], PEs : list[tuple]) -> list[dict[int,tuple],dict[tuple,int]]:
        assert len(vertexes) <= len(PEs)
        placement_n2c = {}
        placement_c2n = {}
        free_PEs = PEs.copy()
        for pe in free_PEs:
            placement_c2n[pe] = None
        for vertex in vertexes:
            pe = choice(free_PEs)
            free_PEs.remove(pe)
            placement_n2c[vertex] = pe
            placement_c2n[pe] = vertex
        return placement_n2c,placement_c2n
    
