#include "aoc.h"

#define ADD 1
#define MUL 2
#define REA 3
#define WRI 4
#define JIT 5
#define JIF 6
#define LT 7
#define EQ 8
#define EXIT 9

void run(vector<int> instructions, const int input) {
    int idx = 0;

    while (true) {
        int param_1 = 0;
        int param_2 = 0;
        int param_3 = 0;
        int op = instructions[idx];
        string str_op = to_string(op);
        op = stoi(str_op.substr(str_op.size() - 1,1));

        if (str_op.size() == 3) {
            param_1 = stoi(str_op.substr(0, 1));
        }
        else if (str_op.size() == 4) {
            param_1 = stoi(str_op.substr(1, 1));
            param_2 = stoi(str_op.substr(0, 1));
        }
        else if (str_op.size() == 5) {
            param_1 = stoi(str_op.substr(2, 1));
            param_2 = stoi(str_op.substr(1, 1));
            param_3 = stoi(str_op.substr(0, 1));
        }
        int n1, n2, dest;

        switch (op) {
            case ADD:
                param_1 == 1 ? n1 = instructions[idx + 1] : n1 = instructions[instructions[idx + 1]];
                param_2 == 1 ? n2 = instructions[idx + 2] : n2 = instructions[instructions[idx + 2]];
                param_3 == 0 ? dest = instructions[idx + 3] : dest = instructions[instructions[idx + 3]];
                instructions[dest] = n1 + n2;
                idx += 4;
                break;
            case MUL:
                param_1 == 1 ? n1 = instructions[idx + 1] : n1 = instructions[instructions[idx + 1]];
                param_2 == 1 ? n2 = instructions[idx + 2] : n2 = instructions[instructions[idx + 2]];
                param_3 == 0 ? dest = instructions[idx + 3] : dest = instructions[instructions[idx + 3]];
                instructions[dest] = n1 * n2;
                idx += 4;
                break;
            case REA:
                param_1 == 0 ? instructions[instructions[idx + 1]] = input : instructions[idx + 1] = input;
                idx += 2;
                break;
            case WRI:
                param_1 == 0 ? cout << instructions[instructions[idx + 1]] << " " : cout << instructions[idx + 1] << " ";
                idx += 2;
                break;
            case JIT:
                param_1 == 1 ? n1 = instructions[idx + 1] : n1 = instructions[instructions[idx + 1]];
                param_2 == 1 ? n2 = instructions[idx + 2] : n2 = instructions[instructions[idx + 2]];
                n1 == 0 ? idx += 3 : idx = n2;
                break;
            case JIF:
                param_1 == 1 ? n1 = instructions[idx + 1] : n1 = instructions[instructions[idx + 1]];
                param_2 == 1 ? n2 = instructions[idx + 2] : n2 = instructions[instructions[idx + 2]];
                n1 == 0 ? idx = n2 : idx += 3;
                break;
            case LT:
                param_1 == 1 ? n1 = instructions[idx + 1] : n1 = instructions[instructions[idx + 1]];
                param_2 == 1 ? n2 = instructions[idx + 2] : n2 = instructions[instructions[idx + 2]];
                param_3 == 0 ? dest = instructions[idx + 3] : dest = instructions[instructions[idx + 3]];
                n1 < n2 ? instructions[dest] = 1 : instructions[dest] = 0;
                idx += 4;
                break;
            case EQ:
                param_1 == 1 ? n1 = instructions[idx + 1] : n1 = instructions[instructions[idx + 1]];
                param_2 == 1 ? n2 = instructions[idx + 2] : n2 = instructions[instructions[idx + 2]];
                param_3 == 0 ? dest = instructions[idx + 3] : dest = instructions[instructions[idx + 3]];
                n1 == n2 ? instructions[dest] = 1 : instructions[dest]= 0;
                idx += 4;
                break;
            case EXIT:
                cout << endl;
                cout << "PROGRAM STOPPED" << endl;
                return;
            default: cout << "Should never reach here" << endl; return;
        }
    }
}

int main() {
    ifstream inputFile("../input/day5.txt");

    if (!inputFile.is_open()) {
        cerr << "Failed to open file!" << endl;
        return 1;
    }

    vector<int> instructions;
    string line;
    getline(inputFile, line);

    stringstream ss(line);
    string token;
    while (getline(ss, token, ',')) {
        instructions.push_back(stoi(token));
    }

    inputFile.close();

    // Part 1
    run(instructions, 1);
    // Part 2
    run(instructions, 5);
}
