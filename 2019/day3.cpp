#include "aoc.h"

set<pair<int, int>> trace_wire(const string& line) {
    set<pair<int, int>> coords;
    int x = 0, y = 0;

    stringstream ss(line);
    string token;
    while (getline(ss, token, ',')) {
        const char dir = token[0];
        const int len = stoi(token.substr(1));
        for (int i = 0; i < len; ++i) {
            switch (dir) {
                case 'U': ++y; break;
                case 'D': --y; break;
                case 'L': --x; break;
                case 'R': ++x; break;
                default: cout << "Invalid coordinate in line: " << line << endl;
            }
            coords.insert({x, y});
        }
    }
    return coords;
}

int manhattan(const pair<int, int>& p) {
    return abs(p.first) + abs(p.second);
}

int closest_intersection(const set<pair<int, int>>& a,
                         const set<pair<int, int>>& b) {
    int min_dist = INT_MAX;
    for (const auto& coord : a) {
        if (b.contains(coord)) {
            min_dist = min(min_dist, manhattan(coord));
        }
    }
    return min_dist;
}

set<pair<int, int>> all_intersections(const set<pair<int, int>>& a,
                                      const set<pair<int, int>>& b) {
    set<pair<int, int>> intersections;
    for (const auto& coord : a) {
        if (b.contains(coord)) {
            intersections.insert(coord);
        }
    }
    return intersections;
}

int path_length(const pair<int, int>& end, const string& line) {
    int x = 0, y = 0;
    int steps = 0;

    stringstream ss(line);
    string token;
    while (getline(ss, token, ',')) {
        const char dir = token[0];
        const int len = stoi(token.substr(1));
        for (int i = 0; i < len; ++i) {
            ++steps;
            switch (dir) {
                case 'U': ++y; break;
                case 'D': --y; break;
                case 'L': --x; break;
                case 'R': ++x; break;
                default: cout << "Invalid coordinate in line: " << line << endl;
            }
            if (x == end.first && y == end.second) {
                return steps;
            }
        }
    }
    return steps;  // Should never hit this if all intersections are valid
}

int shortest_combined_walk(const set<pair<int, int>>& intersections,
                           const string& line1,
                           const string& line2) {
    int shortest_combined = INT_MAX;
    for (const auto& intersection : intersections) {

        const int line1_path_len = path_length(intersection, line1);
        const int line2_path_len = path_length(intersection, line2);

        if (line1_path_len + line2_path_len < shortest_combined) {
            shortest_combined = line1_path_len + line2_path_len;
        }
    }
    return shortest_combined;
}

int main() {
    ifstream infile("../input/day3.txt");

    if (!infile.is_open()) {
        cerr << "Failed to open file!" << endl;
        return 1;
    }

    string wire1_line, wire2_line;
    getline(infile, wire1_line);
    getline(infile, wire2_line);

    auto wire1 = trace_wire(wire1_line);
    auto wire2 = trace_wire(wire2_line);

    int part1 = closest_intersection(wire1, wire2);
    cout << "part1: " << part1 << "\n";

    auto intersections = all_intersections(wire1, wire2);
    int part2 = shortest_combined_walk(intersections, wire1_line,wire2_line);
    cout << "part2: " << part2 << "\n";
}
