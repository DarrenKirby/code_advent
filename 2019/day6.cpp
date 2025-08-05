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

int main() {
    ifstream inputFile("../input/day6.txt");

    if (!inputFile.is_open()) {
        cerr << "Failed to open file!" << endl;
        return 1;
    }

    unordered_map<string, vector<string>> planet_map;
    string line;

    while (getline(inputFile, line)) {
        // Input format is: "AAA)BBB"
        if (line.size() >= 7 && line[3] == ')') {
            string parent = line.substr(0, 3);
            string child = line.substr(4, 3);
            planet_map[parent].push_back(child);
        }
    }

    cout << count_orbits(planet_map, "COM", 0) << endl;
    return 0;
}
