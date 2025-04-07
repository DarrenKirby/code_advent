package day01

import java.io.File

fun readInput(): List<Int> {
    val lines = File("./src/day1.txt").readLines()
    val numbers = lines.map { it.removePrefix("+").toInt() }
    return numbers
}

fun findFirstDuplicateFrequency(changes: List<Int>): Int {
    val seen = mutableSetOf(0)
    var freq = 0

    while (true) {
        for (delta in changes) {
            freq += delta
            if (!seen.add(freq)) {
                return freq // found it!
            }
        }
    }
}

fun main() {
    val nums = readInput()
    // part 1
    println(nums.sum())
    // part 2
    println(findFirstDuplicateFrequency(nums))
}

