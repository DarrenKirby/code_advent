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

vector<vector<int>> generate_permutations(const bool part_1) {
    vector<int> digits;
    if (part_1) {
        digits = {0, 1, 2, 3, 4};
    } else {
        digits = {5, 6, 7, 8, 9};
    }

    vector<vector<int>> all_perms;

    do {
        all_perms.push_back(digits);
    } while (next_permutation(digits.begin(), digits.end()));

    return all_perms;
}

class IntcodeComputer {
public:
    bool halted = false;
    explicit IntcodeComputer(const vector<int>& program) : memory(program) {}

    void add_input(const int val) { input.push(val); }

    // Returns: {output produced, or std::nullopt if no output yet}
    optional<int> run_until_output();

private:
    vector<int> memory;
    int ip = 0;
    queue<int> input;

};

optional<int> IntcodeComputer::run_until_output() {
    while (true) {
        int param_1 = 0, param_2 = 0;
        int op = memory[ip];
        string str_op = to_string(op);
        op = stoi(str_op.substr(str_op.size() - 1));

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
        }

        int n1, n2, dest, in_val;
        switch (op) {
            case ADD:
                param_1 == 1 ? n1 = memory[ip + 1] : n1 = memory[memory[ip + 1]];
                param_2 == 1 ? n2 = memory[ip + 2] : n2 = memory[memory[ip + 2]];
                dest = memory[ip + 3];
                memory[dest] = n1 + n2;
                ip += 4;
                break;
            case MUL:
                param_1 == 1 ? n1 = memory[ip + 1] : n1 = memory[memory[ip + 1]];
                param_2 == 1 ? n2 = memory[ip + 2] : n2 = memory[memory[ip + 2]];
                dest = memory[ip + 3];
                memory[dest] = n1 * n2;
                ip += 4;
                break;
            case REA:
                if (input.empty()) return std::nullopt;
                in_val = input.front(); input.pop();
                param_1 == 0 ? memory[memory[ip + 1]] = in_val : memory[ip + 1] = in_val;
                ip += 2;
                break;
            case WRI:
                int output;
                param_1 == 0 ? output = memory[memory[ip + 1]] : output = memory[ip + 1];
                ip += 2;
                return output;
            case JIT:
                param_1 == 1 ? n1 = memory[ip + 1] : n1 = memory[memory[ip + 1]];
                param_2 == 1 ? n2 = memory[ip + 2] : n2 = memory[memory[ip + 2]];
                n1 == 0 ? ip += 3 : ip = n2;
                break;
            case JIF:
                param_1 == 1 ? n1 = memory[ip + 1] : n1 = memory[memory[ip + 1]];
                param_2 == 1 ? n2 = memory[ip + 2] : n2 = memory[memory[ip + 2]];
                n1 == 0 ? ip = n2 : ip += 3;
                break;
            case LT:
                param_1 == 1 ? n1 = memory[ip + 1] : n1 = memory[memory[ip + 1]];
                param_2 == 1 ? n2 = memory[ip + 2] : n2 = memory[memory[ip + 2]];
                dest = memory[ip + 3];
                n1 < n2 ? memory[dest] = 1 : memory[dest] = 0;
                ip += 4;
                break;
            case EQ:
                param_1 == 1 ? n1 = memory[ip + 1] : n1 = memory[memory[ip + 1]];
                param_2 == 1 ? n2 = memory[ip + 2] : n2 = memory[memory[ip + 2]];
                dest = memory[ip + 3];
                n1 == n2 ? memory[dest] = 1 : memory[dest]= 0;
                ip += 4;
                break;
            case EXIT:
                halted = true;
                return nullopt;
            default: cout << "Should never reach here" << endl; return -1;
        }
    }
}


int main() {
    ifstream inputFile("../input/day7.txt");

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

    int largest_so_far = -1;
    auto perms = generate_permutations(true);

    for (const vector<int>& ph_settings : perms) {
        int input_signal = 0;

        for (int i = 0; i < 5; ++i) {
            IntcodeComputer amp(instructions);
            amp.add_input(ph_settings[i]);
            amp.add_input(input_signal);

            auto out = amp.run_until_output();
            if (!out.has_value()) {
                cerr << "Amp failed to produce output!" << endl;
                break;
            }
            input_signal = out.value();
        }

        if (input_signal > largest_so_far) {
            largest_so_far = input_signal;
        }
    }

    cout << "Part 1: " << largest_so_far << endl;

    // Part 2
    auto phase_settings = generate_permutations(false);
    largest_so_far = -1;

    for (const vector<int>& ph_settings : phase_settings) {
        vector<IntcodeComputer> amps;
        for (int i = 0; i < 5; ++i) {
            amps.emplace_back(instructions);
            amps[i].add_input(ph_settings[i]);
        }
        amps[0].add_input(0); // Initial signal

        int last_output = 0;
        while (!amps[4].halted) {
            for (int i = 0; i < 5; ++i) {
                auto out = amps[i].run_until_output();
                if (out.has_value()) {
                    int signal = out.value();
                    last_output = signal;
                    amps[(i + 1) % 5].add_input(signal);
                }
            }
        }
        if (last_output > largest_so_far) {
            largest_so_far = last_output;
        }
    }
    cout << "Part 2: " <<  largest_so_far << endl;
}
