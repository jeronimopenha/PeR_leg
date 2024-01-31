from src.util.per_graph import PeRGraph


class Stage2YOTT:
    def __init__(self, itl: list[list], per: PeRGraph, annotations: list[dict], num_threads: int):
        """

        @param itl:
        @type itl:
        @param per:
        @type per:
        @param annotations:
        @type annotations:
        @param num_threads:
        @type num_threads:
        """
        super().__init__()
        self.threads_edges = itl
        self.len_edges = len(itl)
        self.num_threads = num_threads
        self.annotations = annotations
        self.per = per

        self.new_output = {
            'thread_index': 0,
            'thread_valid': 0,
            'A': 0,
            'B': 0,
            'C': -1,
            'dist_CB': 0,
            'edge_index': 0

        }

        self.old_output = self.new_output

    def compute(self, stage1):
        """

        @param stage1:
        @type stage1:
        """
        self.old_output = self.new_output.copy()
        out_previous_stage = stage1.old_output
        thread_index = out_previous_stage['thread_index']
        edge_index = out_previous_stage['edge_index']

        # print(self.threads_edges[thread_index])

        a, b = self.threads_edges[thread_index][edge_index]
        # print(A,B,edge_index,out_previous_stage['thread_valid'])
        annotations = list(self.annotations[thread_index].values())[edge_index]
        # print(self.annotations[thread_index].values())
        if len(annotations) == 0:
            annotation = [-1, -1]
        else:
            annotation = [self.per.nodes_to_idx[annotations[0][0]], annotations[0][1] + 1]
        c, dist_cb = annotation
        # print(annotation)

        self.new_output = {
            'thread_index': thread_index,
            'thread_valid': out_previous_stage['thread_valid'],
            'A': a,
            'B': b,
            'C': c,
            'dist_CB': dist_cb,
            'edge_index': edge_index
        }
