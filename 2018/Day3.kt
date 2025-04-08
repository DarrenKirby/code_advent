package day03

import java.io.File

fun readInput(): List<String> {
    val lines = File("./src/day3.txt").readLines()
    return lines
}

fun cleanLines(lines: List<String>):MutableList<List<Int>> {
    val regex = Regex("""#(\d+) @ (\d+),(\d+): (\d+)x(\d+)""")
    val result = mutableListOf<List<Int>>()

    for (line in lines) {
        val match = regex.find(line)
        if (match != null) {
            val (id, x, y, w, h) = match.destructured
            result.add(listOf(x.toInt(), y.toInt(), w.toInt(), h.toInt(), id.toInt()))
        }
    }
    return result
}

fun markGrid(
    g: MutableList<MutableList<Char>>,
    arr: List<Int>
): MutableList<MutableList<Char>> {
    val (x, y, w, h, _) = arr
    for (r in y..<y + h) {
        for (c in x..<x + w) {
            if (g[r][c] == '#') {
                g[r][c] = 'X'
            } else if (g[r][c] == '.') {
                g[r][c] = '#'
            }
        }
    }
    return g
}

fun markGrid2(
    g: MutableList<MutableList<Int>>,
    arr: MutableList<List<Int>>
): Set<Int> {
    val allSet = mutableSetOf<Int>()
    val overlapSet = mutableSetOf<Int>()
    for (line in arr) {
        val (x, y, w, h, id) = line
        allSet.add(id)
        for (r in y..<y + h) {
            for (c in x..<x + w) {
                if (g[r][c] == 0) {
                    g[r][c] = id
                } else if (g[r][c] != 0) {
                    overlapSet.add(id)
                    overlapSet.add(g[r][c])
                    g[r][c] = id
                }
            }
        }
    }
    return allSet subtract overlapSet
}

fun main() {
    val lines = readInput()
    val cLines = cleanLines(lines)

    // make an empty grid
    var grid = MutableList(1001) { MutableList(1001) { '.' } }

    // iterate over input and mark the grid
    for (l in cLines) {
        grid = markGrid(grid, l)
    }

    // iterate over grid and count Xs
    var overlap = 0
    for (r in grid.indices) {
        for (c in grid[r].indices) {
            val ch = grid[r][c]
            if (ch == 'X') overlap++
        }
    }
    //part 1
    println(overlap)

    // part 2
    val grid2 = MutableList(1001) { MutableList(1001) { 0 } }
    println(markGrid2(grid2, cLines))
}

