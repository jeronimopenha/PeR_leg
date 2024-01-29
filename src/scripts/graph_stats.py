from math import ceil
import os
import traceback
from src.util.util import Util
from src.util.per_graph import PeRGraph


def main(_folder: str, _dest_dir: str):
    files_l = Util.get_files_list_by_extension(_folder, '.dot')
    stats = []
    for dot_file, dot_name in files_l:
        stat = {
            'name': dot_name,
            'bench': dot_file,
            'nodes': 0,
            'edges': 0,
            'ideal_cost': 0,
            'max_degree': 0,
            'avg_degree': 0,
            'g_hub': {},
            'top_k_hub': [],  # 20%
            'percent_multicast': 0,  # > 2
            'hist_grade': {}  # per grade
        }

        per_graph = PeRGraph(dot_file, dot_name)

        # Adding the number of edges and nodes to stats
        stat['nodes'] = per_graph.n_nodes
        stat['edges'] = per_graph.n_edges
        stat['ideal_cost'] = per_graph.n_edges

        max_degree = 0
        avg_degree = 0
        hub_sum = 0
        for node in per_graph.nodes:
            # finding the degrees of each node and caculating the average degree for the graph
            degree = per_graph.g.degree[node]
            if degree > max_degree:
                max_degree = degree
            avg_degree += degree

            # creating the degree histogram
            if degree in stat['hist_grade'].keys():
                stat['hist_grade'][degree] += 1
            else:
                stat['hist_grade'][degree] = 1

            # finding the hub for the graph
            n_childs = len(list(per_graph.g._succ[node].keys()))
            if n_childs > 2:
                stat['g_hub'][node] = n_childs
                hub_sum += 1

        avg_degree /= per_graph.n_nodes
        stat['max_degree'] = max_degree
        stat['avg_degree'] = avg_degree
        stat['percent_multicast'] = hub_sum / per_graph.n_nodes
        stat['hist_grade'] = dict(sorted(stat['hist_grade'].items()))

        top_k_hub = sorted(stat['g_hub'].items(),
                           key=lambda item: item[1], reverse=True)
        k = ceil(len(top_k_hub) * 0.2)
        for i in range(k):
            stat['top_k_hub'] = top_k_hub[i]
        stats.append(stat)

    wr_str = ''
    for k in stats[0].keys():
        wr_str += k + ';'
    wr_str = wr_str[:-1] + '\n'
    for i in range(len(stats)):
        wr_str += '%s; ' % stats[i]['name']
        wr_str += '%s; ' % stats[i]['bench']
        wr_str += '%d; ' % stats[i]['nodes']
        wr_str += '%d; ' % stats[i]['edges']
        wr_str += '%d; ' % stats[i]['ideal_cost']
        wr_str += '%d; ' % stats[i]['max_degree']
        wr_str += '%0.3f; ' % stats[i]['avg_degree']
        wr_str += '%s; ' % str(stats[i]['g_hub'])
        wr_str += '%s; ' % str(stats[i]['top_k_hub'])
        wr_str += '%0.3f; ' % stats[i]['percent_multicast']
        wr_str += '%s \n' % stats[i]['hist_grade']
    wr = open(_dest_dir + 'db_stats.csv', 'w')
    wr.write(wr_str)
    wr.close()

    # FIXME
    for j in range(len(stats)):
        wr_str = ''
        for i in range(len(stats[j]['hist_grade'])):
            wr_str += '%d;%d\n' % (i, stats[j]['hist_grade'][str(i)])
        wr = open(_dest_dir + '%s_hist.csv' % stats[j]['name'], 'w')
        wr.write(wr_str)
        wr.close()


if __name__ == '__main__':
    try:
        root_path: str = Util.get_project_root()
        dot_path_base = root_path + '/dot_db/'
        dot_connected_path = dot_path_base + 'connected/'
        output_path = root_path + '/results/db_stats/'

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        main(dot_connected_path, output_path)
        a = 1
    except Exception as e:
        print(e)
        traceback.print_exc()
