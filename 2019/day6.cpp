#include "aoc.h"

int count_orbits(const unordered_map<string, vector<string>>& map, const string& node, int depth) {
    int total = depth;
    auto it = map.find(node);
    if (it != map.end()) {
        for (const string& child : it->second) {
            total += count_orbits(map, child, depth + 1);
        }
    }
    return total;
}

bool find_path(set<string> seen, const string& node, int counter,
    const unordered_map<string, vector<string>>& graph, const string& target) {
    seen.insert(node);
    if (node == target) {
        cout << counter << endl;
        return true;
    }
    auto it = graph.find(node);
    if (it != graph.end()) {
        for (const string& next_node : it->second) {
            if (seen.contains(next_node)) {
                continue;
            }
            if (find_path(seen, next_node, counter + 1, graph, target) == true) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    ifstream inputFile("../input/day6.txt");

    if (!inputFile.is_open()) {
        cerr << "Failed to open file!" << endl;
        return 1;
    }

    unordered_map<string, vector<string>> planet_map;
    unordered_map<string, vector<string>> graph;
    string line;
    string start;
    string target;

    while (getline(inputFile, line)) {
        // Input format is: "AAA)BBB"
        if (line.size() >= 7 && line[3] == ')') {
            string parent = line.substr(0, 3);
            string child = line.substr(4, 3);
            planet_map[parent].push_back(child);
            // for part 2
            graph[child].push_back(parent);
            graph[parent].push_back(child);
            if (child == "YOU") {
                start = parent;
            }
            if (child == "SAN") {
                target = parent;
            }
        }
    }

    // Part 1
    cout << count_orbits(planet_map, "COM", 0) << endl;
    // Part 2
    set<string> seen;
    find_path(seen, start, 0, graph, target);
    return 0;
}
