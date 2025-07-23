#include "aoc.h"

int main() {
    ifstream inputFile("input/day2.txt");
    if (!inputFile) {
        cerr << "Couldn't open file" << endl;
        return 1;
    }

    vector<int> instructions;
    string line;
    getline(inputFile, line);  // read the whole line

    stringstream ss(line);
    string token;
    while (getline(ss, token, ',')) {
        instructions.push_back(stoi(token));
    }

    // part 1
    int idx = 0;            // an instruction pointer
    vector<int> numbers = instructions; // make a copy, as we'll mutate it.
    numbers[1] = 12;        // arbitrary, as per instructions
    numbers[2] = 2;         // arbitrary, as per instructions

    int op, v1, v2, out;
    while (true) {
        op = numbers[idx];       // the opcode
        v1 = numbers[idx + 1];   // operand 1
        v2 = numbers[idx + 2];   // operand 2
        out = numbers[idx + 3];  // destination register

        if (op == 99) { // halt
            break;
        }
        if (op == 1) {
            numbers[out] = numbers[v1] + numbers[v2];
        } else if (op == 2) {
            numbers[out] = numbers[v1] * numbers[v2];
        }
        idx += 4;
    }
    cout << "part 1: " << numbers[0] << endl;

    // part 2
    for (int noun = 0; noun < 100; noun++) {
        for (int verb = 0; verb < 100; verb++) {
            idx = 0;
            vector<int> working = instructions;
            working[1] = noun;
            working[2] = verb;

            while (true) {
                op = working[idx];       // the opcode
                v1 = working[idx + 1];   // operand 1
                v2 = working[idx + 2];   // operand 2
                out = working[idx + 3];  // destination register

                if (op == 99) { // halt
                    break;
                }
                if (op == 1) {
                    working[out] = working[v1] + working[v2];
                } else if (op == 2) {
                    working[out] = working[v1] * working[v2];
                }
                idx += 4;
            }
            if (working[0] == 19690720) {
                cout << "noun : " << noun << " verb: " << verb << endl;
                cout << "working[0]: " << working[0] << endl;
                cout << "part2: " << 100 * noun + verb << endl;
                return 0;
            }
        }
    }
    return 0;
}