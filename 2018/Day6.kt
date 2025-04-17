package day06

import java.io.File
import kotlin.math.absoluteValue

private fun generateMarkers(): Sequence<String> = sequence {
    val letters = ('A'..'Z').toList()
    var i = 0
    while (true) {
        val index = i % letters.size
        val repeat = i / letters.size + 1
        yield(letters[index].toString().repeat(repeat))
        i++
    }
}

fun readInput(): List<Pair<Int, Int>> {
    var cleanedLines = mutableListOf<Pair<Int, Int>>()
    val lines = File("./src/day6.txt").readLines()
    //process and return list of Int pairs
    for (line in lines){
        var splitLine = line.split(", ")
        cleanedLines.add(Pair(splitLine[0].toInt(), splitLine[1].toInt()))
    }
    return cleanedLines
}

fun manhattanDistance(x1: Int, y1: Int, x2: Int, y2: Int):Int {
    // d = |x_1 - x_2| + |y_1 - y_2|
    return (x1 - x2).absoluteValue + (y1 - y2).absoluteValue
}

fun plotGridInitial(
    coords: List<Pair<Int, Int>>,
    grid: MutableList<MutableList<String>>): MutableList<MutableList<String>> {
    val markers = generateMarkers().iterator()
    val coordMarkers = coords.associateWith { markers.next() }
    for (coordinate in coords) {
        grid[coordinate.first][coordinate.second] = coordMarkers[coordinate].toString()
    }

    // plot manhattan-distance closest coord
    for (r in grid.indices) {
        for (c in grid[r].indices) {
            if (coords.contains(r to c)) continue

            var closestDist = Int.MAX_VALUE
            var closestCoord: Pair<Int, Int>? = null
            var tie = false

            for (coord in coords) {
                val dist = manhattanDistance(r, c, coord.first, coord.second)

                when {
                    dist < closestDist -> {
                        closestDist = dist
                        closestCoord = coord
                        tie = false
                    }
                    dist == closestDist -> {
                        tie = true
                    }
                }
            }

            grid[r][c] = if (tie) {
                "#"
            } else {
                coordMarkers[closestCoord]!!.lowercase()
            }
        }
    }
    return grid
}

fun countMarkersInGrid(s: String, grid: MutableList<MutableList<String>>):Int{
    var count = 0
    for (r in grid.indices) {
        for (c in grid[r].indices) {
            if (grid[r][c] == s) {
                count++
            }
        }
    }
    // add one for the original coordinate pair
    return count + 1
}

fun findLargestArea(grid: MutableList<MutableList<String>>):Int {
    var markerList = generateMarkers().take(50).toList() //.toMutableSet()
    markerList = markerList.map { it.lowercase() }
    val markerSet = markerList.toMutableSet()
    val numRows = grid.size
    val numCols = grid[0].size

    // Top and bottom rows
    for (c in 0 until numCols) {
        if (grid[0][c] in markerSet) {
            markerSet.remove(grid[0][c])
        }
        if (grid[numRows - 1][c] in markerSet) {
            markerSet.remove(grid[numRows-1][c])
        }
    }

    // Left and right columns
    for (r in 1 until numRows - 1) {
        if (grid[r][0] in markerSet) {
            markerSet.remove(grid[r][0])
        }
        if (grid[r][numCols - 1] in markerSet) {
            markerSet.remove(grid[r][numCols - 1])
        }
    }

    val sizePerArea = markerSet.associateWith { countMarkersInGrid(it, grid) }
    return sizePerArea.maxBy { it.value }.value
}

fun partTwo(coords: List<Pair<Int, Int>>, rows: Int, cols: Int): Int {
    var count = 0
    for (r in 0 until rows) {
        for (c in 0 until cols) {
            val distances = mutableListOf<Int>()
            for (coord in coords) {
                distances.add(manhattanDistance(r, c, coord.first, coord.second))
            }
            if (distances.sum() < 10000) {
                count++
            }
        }
    }
    return count
}

fun main() {
    val coordinates = readInput()
    val maxFirst = coordinates.maxOf { it.first }
    val maxSecond = coordinates.maxOf { it.second }
    var grid = MutableList(maxFirst + 1) { MutableList(maxSecond + 1) { "." } }

    grid = plotGridInitial(coordinates, grid)
    // part 1
    println(findLargestArea(grid))
    // part 2
    println(partTwo(coordinates, maxFirst + 1, maxSecond + 1))
}

