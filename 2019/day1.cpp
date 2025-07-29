#include "aoc.h"

int main() {
    vector<int> modules;
    ifstream inputFile("../input/day1.txt");

    if (!inputFile.is_open()) {
        cerr << "Failed to open file!" << endl;
        return 1;
    }

    int number;
    while (inputFile >> number) {
        modules.push_back(number);
    }
    inputFile.close();

    // part 1
    int sum = 0;
    for (const int module : modules) {
        const int mass = module / 3 - 2;
        sum += mass;
    }
    cout << "Part 1: " <<  sum << endl;

    // part 2
    sum = 0;
    for (const int module : modules) {
        int local_sum = 0;
        const int fuel = module / 3 - 2;
        local_sum += fuel;

        int local_fuel = fuel;
        while (local_fuel > 0) {
            local_fuel = local_fuel / 3 - 2;
            if (local_fuel > 0) {
                local_sum += local_fuel;
            }
        }

        sum += local_sum;
    }
    cout << "Part 2: " <<  sum << endl;
    return 0;
}
