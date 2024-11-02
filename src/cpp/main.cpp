//
// Created by jeronimo on 01/11/24.
//

#include <iostream>
#include  "util.h"
#include "graph.h"


int main() {
    // std::string root_path = get_project_root(); // Supondo que essa função existe
    const std::string root_path = getProjectRoot(); // Exemplo de função que busca o root path
    auto files = getFilesListByExtension(root_path + "/benchmarks/fpga/bench_test/", ".dot");
    // std::vector<std::vector<std::string>> files = {{"path/to/file.dot", "file.dot"}};

    for (const auto &[fst, snd]: files) {
        std::cout << fst << std::endl;
        Graph g(fst, snd.substr(0, snd.size() - 4)); // Remove a extensão ".dot"
        auto a = g.getMeshDistances();
        int b = 1;
        /*FPGAPeR per(g);

        // Componente desconectado para DAG
        auto disconnected_components = g.getWeaklyConnectedComponents();

        int n_exec = 11;
        std::string base_folder = "reports/fpga/outputs/";
        std::vector<std::string> placers = {"yoto"};
        std::vector<EdAlgEnum> yoto_algs = {EdAlgEnum::DEPTH_FIRST_WITH_PRIORITY};

        for (const auto &placer: placers) {
            std::unordered_map<std::string, ReportType> reports;
            // Supondo que ReportType é um tipo que armazena o relatório
            std::string file_name_prefix;
            auto start = std::chrono::high_resolution_clock::now();

            if (placer == "yoto") {
                for (const auto &alg: yoto_algs) {
                    reports = per.per(PeR_Enum::YOTO, {alg}, n_exec);
                    auto end = std::chrono::high_resolution_clock::now();
                    std::cout << "Tempo: "
                            << std::chrono::duration_cast<std::chrono::seconds>(end - start).count()
                            << " segundos" << std::endl;

                    file_name_prefix = "yoto_" + std::to_string(static_cast<int>(alg));
                    save_reports(per, verifyPath(root_path) + base_folder, file_name_prefix, reports);
                }
            } else if (placer == "yott") {
                reports = per.per(PeR_Enum::YOTT, {}, n_exec);
                file_name_prefix = "yott";
                save_reports(per, verifyPath(root_path) + base_folder, file_name_prefix, reports);
            } else if (placer == "sa") {
                reports = per.per(PeR_Enum::SA, {}, n_exec);
                file_name_prefix = "sa";
                save_reports(per, verifyPath(root_path) + base_folder, file_name_prefix, reports);
            }
        }*/
    }

    //generate_pic(); // Supondo que essa função exista em C++
    return 0;
}
