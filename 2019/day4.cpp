#include "aoc.h"

vector<int> int_to_vector(const int num) {
    vector<int> v;
    v.push_back(num % 1000000 / 100000);
    v.push_back(num % 100000 / 10000);
    v.push_back(num % 10000 / 1000);
    v.push_back(num % 1000 / 100);
    v.push_back(num % 100 / 10);
    v.push_back(num % 10);
    return v;
}

int main() {
    // my personal input
    constexpr int low  = 273025;
    constexpr int high = 767253;

    vector<int> numerals;

    int possible_passwords_part1 = 0;
    int possible_passwords_part2 = 0;

    for (int i = low; i <= high; i++) {
        numerals.clear();
        numerals = int_to_vector(i);

        bool exactly_one_double = false;

        if (!is_sorted(numerals.begin(), numerals.end())) {
            continue;
        }

        auto it = adjacent_find(numerals.begin(), numerals.end());
        if (it == numerals.end()) {
            continue;
        }

        unordered_map<int, int> counts;
        int run_length = 1;

        for (int j = 1; j < numerals.size(); ++j) {
            if (numerals[j] == numerals[j - 1]) {
                run_length++;
            } else {
                if (run_length >= 2) {
                    counts[numerals[j - 1]] = run_length;
                }
                run_length = 1;
            }
        }
        if (run_length >= 2) {
            counts[numerals.back()] = run_length;
        }

        for (auto& [digit, count] : counts) {
            if (count == 2) {
                exactly_one_double = true;
                break;
            }
        }
        possible_passwords_part1 += 1;
        if (exactly_one_double) {
            possible_passwords_part2 += 1;
        }
    }
    cout << "Part 1: " << possible_passwords_part1 << endl;
    cout << "Part 2: " << possible_passwords_part2 << endl;
}
