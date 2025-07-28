with open("input/day17.txt", 'r') as f:
    lines = f.read().splitlines()

# Parse input to populate registers/instruction queue
reg_A = int(lines[0].split(':')[1])
reg_B = int(lines[1].split(':')[1])
reg_C = int(lines[2].split(':')[1])

prog = [int(num) for num in lines[-1].split(":")[1].split(",")]


class ChronospatialComputer:
    def __init__(self, reg_a: int, reg_b: int, reg_c: int, instructions: list):
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.instructions = instructions
        self.instr_ptr = 0
        self.output = []

    def combo_op(self, op: int) -> int:
        if op in [0, 1, 2, 3]:
            return op
        elif op == 4:
            return self.reg_a
        elif op == 5:
            return self.reg_b
        elif op == 6:
            return self.reg_c
        else:
            raise ValueError("Invalid combo operation")

    def adv(self, operand: int) -> None:
        """op 0"""
        self.reg_a = self.reg_a // (2 ** self.combo_op(operand))

    def bxl(self, operand: int) -> None:
        """op 1"""
        self.reg_b = self.reg_b ^ operand

    def bst(self, operand: int) -> None:
        """op 2"""
        self.reg_b = self.combo_op(operand) % 8

    def jnz(self, operand: int) -> None:
        """op 3"""
        if self.reg_a:
            self.instr_ptr = operand
            # this is to offset the global ip increase in run()
            self.instr_ptr -= 2

    def bxc(self) -> None:
        """op 4"""
        self.reg_b = self.reg_b ^ self.reg_c

    def out(self, operand: int) -> None:
        """op 5"""
        self.output.append(self.combo_op(operand) % 8)

    def bdv(self, operand: int) -> None:
        """op 6"""
        self.reg_b = self.reg_a // (2 ** self.combo_op(operand))

    def cdv(self, operand: int) -> None:
        """op 7"""
        self.reg_c = self.reg_a // (2 ** self.combo_op(operand))

    def run(self):
        while self.instr_ptr < len(self.instructions):
            operand = self.instructions[self.instr_ptr + 1]
            match self.instructions[self.instr_ptr]:
                case 0:
                    self.adv(operand)
                case 1:
                    self.bxl(operand)
                case 2:
                    self.bst(operand)
                case 3:
                    self.jnz(operand)
                case 4:
                    self.bxc()
                case 5:
                    self.out(operand)
                case 6:
                    self.bdv(operand)
                case 7:
                    self.cdv(operand)
            self.instr_ptr += 2


# part 1
computer = ChronospatialComputer(reg_A, reg_B, reg_C, prog)
computer.run()
print(",".join([str(n) for n in computer.output]))
# part 2
initial = 0
target_output = prog

for i in reversed(range(len(prog))):
    initial <<= 3
    while True:
        computer = ChronospatialComputer(initial, reg_B, reg_C, prog)
        computer.run()

        if computer.output == target_output[i:]:
            break
        initial += 1

print(initial)
