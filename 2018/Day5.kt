package day05

import java.io.File

fun readInput(): String {
    val input = File("./src/day5.txt").readText().trim()
    return input
}

fun fullyReact(str: String): String {
    var polymer = str
    var working = true
    while (working) {
        working = false
        for (unit in 'a'..'z') {
            if ("${unit}${unit.uppercaseChar()}" in polymer) {
                polymer = polymer.replace("${unit}${unit.uppercaseChar()}", "")
                working = true
            }
            if ("${unit.uppercaseChar()}${unit}" in polymer) {
                polymer = polymer.replace("${unit.uppercaseChar()}${unit}","")
                working= true
            }
        }
    }
    return polymer
}

fun findBestPolymer(str: String): Int {
    var counts = mutableMapOf<Char, Int>()
    for (char in 'a'..'z') {
        var polymer = str.replace("$char", "")
        polymer = polymer.replace("${char.uppercaseChar()}", "")
        counts[char] = fullyReact(polymer).length
    }
    return counts.minByOrNull { it.value }!!.value
}

fun main() {
    var input = readInput()
    val polymer = fullyReact(input)
    // part 1
    println(polymer.length)

    val shortest = findBestPolymer(input)
    // part 2
    println(shortest)
}

