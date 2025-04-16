package day04

import java.io.File

fun readInput(): List<String> {
    val lines = File("./src/day4.txt").readLines()
    return lines
}

fun processLogs(logs: List<String>): Map<Int, List<String>> {
    var guardLog = mutableMapOf<Int, MutableList<String>>()
    var currentGuard = 0
    var sleepMinute = 0
    var wakeMinute = 0
    val guardRegex = Regex("""\[1518-\d{2}-\d{2} \d{2}:\d{2}] Guard #(\d+) begins shift""")
    val sleepRegex = Regex("""\[1518-\d{2}-\d{2} \d{2}:(\d{2})] falls asleep""")
    val wakeRegex = Regex("""\[1518-\d{2}-\d{2} \d{2}:(\d{2})] wakes up""")

    for (line in logs) {
        if (line.contains("Guard")) {
            sleepMinute = 0
            wakeMinute = 0
            var match = guardRegex.find(line)
            if (match != null) {
                currentGuard = match.groupValues[1].toInt()
            }
        } else if (line.contains("falls asleep"))  {
            var match = sleepRegex.find(line)
            if (match != null) {
                sleepMinute = match.groupValues[1].toInt()
            }
        } else if (line.contains("wakes up")) {
            var match = wakeRegex.find(line)
            if (match != null) {
                wakeMinute = match.groupValues[1].toInt()
            }
        }
        if (sleepMinute != 0 && wakeMinute != 0) {
            var sleepString = ""
            for (i in 0..59) {
                sleepString += if (i in sleepMinute..<wakeMinute) {
                    "#"
                } else {
                    "."
                }
            }
            if (currentGuard in guardLog) {
                guardLog[currentGuard]?.add(sleepString)
            } else {
                guardLog[currentGuard] = mutableListOf<String>()
                guardLog[currentGuard]?.add(sleepString)
            }
            sleepMinute = 0
            wakeMinute = 0
        }
    }
    return guardLog
}

fun getMostSleptMinute(sleepList: List<String>?): Int {
    var sleepMap = (0 until 60).associateWith { 0 }.toMutableMap()
    if (sleepList != null) {
        for (sleepStr in sleepList) {
            for (i in 0..59) {
                if (sleepStr[i] == '#') {
                    sleepMap[i] = sleepMap.getOrDefault(i, 0) + 1
                }
            }
        }
    }
    return sleepMap.maxByOrNull { it.value }!!.key
}

fun minuteMostSleptThrough(log: Map<Int, List<String>>): Pair<Int, Int> {
    var sleepLog = mutableMapOf<Int, MutableList<Int>>()
    log.forEach { (k, v) ->
        val minutes = MutableList(60) { 0 }
        for (str in v) {
            for (i in 0..59) {
                if (str[i] == '#') {
                    minutes[i] += 1
                }
            }
        }
        sleepLog[k] = minutes
    }
    var maxGuard = 0
    var maxMinute = 0
    var maxMinuteIdx = 0
    sleepLog.forEach { (k, v) ->
        val highest = v.max()
        if (highest > maxMinute) {
            maxGuard = k
            maxMinute = highest
            maxMinuteIdx = v.indexOf(highest)
        }
    }
    return Pair(maxGuard, maxMinuteIdx)
}

fun main() {
    var lines = readInput()
    lines = lines.sorted()

    val guardLog = processLogs(lines)
    var mostSleepyGuard = 0
    var mostMinutesSleeping = 0
    guardLog.forEach { (k, v) ->
        var sleepMinutes = 0
        for (str in v) {
            sleepMinutes += str.count { it == '#' }
        }
        if (sleepMinutes > mostMinutesSleeping) {
            mostMinutesSleeping = sleepMinutes
            mostSleepyGuard = k
        }
    }

    val mmst = minuteMostSleptThrough(guardLog)
    val minutes = getMostSleptMinute(guardLog[mostSleepyGuard])
    // Part 1
    println(mostSleepyGuard * minutes)
    // Part 2
    println(mmst.first * mmst.second)
}

