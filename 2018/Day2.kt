package day02

import java.io.File

fun readInput(): List<String> {
    val lines = File("./src/day2.txt").readLines()
    return lines
}

fun partOne(lines: List<String>):Int {
    var twosAndThrees = Pair(0, 0)
    var charCount: Int
    for (line in lines) {
        var foundTwo = false
        var foundThree= false

        for (char in line) {
            charCount = line.count { it == char }

            if (charCount == 2) foundTwo = true
            if (charCount == 3) foundThree = true
        }

        if (foundTwo) twosAndThrees = Pair(twosAndThrees.first + 1, twosAndThrees.second)
        if (foundThree) twosAndThrees = Pair(twosAndThrees.first, twosAndThrees.second + 1)
    }
    return twosAndThrees.first * twosAndThrees.second
}

fun compareStrings(s1: String, s2: String):Boolean {
    val prefix = s1.commonPrefixWith(s2)
    val suffix = s1.commonSuffixWith(s2)
    return prefix.length + suffix.length == s1.length - 1
}

fun partTwo(lines: List<String>):String {
    val strings = lines.toMutableList()
    while (true) {
        val s1 = strings.removeFirst()
        for (s2 in strings) {
            if (compareStrings(s1, s2)) {
                return s1.commonPrefixWith(s2) + s1.commonSuffixWith(s2)
            }
        }
    }
}

fun main() {
    val lines = readInput()
    // part 1
    println(partOne(lines))
    // part 2
    println(partTwo(lines))
}

