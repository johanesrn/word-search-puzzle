# MAIN CODE
from bruteforce import *
from backtracking import *
import time

puzzle = [
          ['E', 'D', 'S', 'H', 'O', 'P', 'E', 'F', 'U', 'L'],
          ['T', 'E', 'N', 'S', 'T', 'T', 'J', 'C', 'R', 'N'],
          ['A', 'T', 'E', 'D', 'P', 'P', 'M', 'E', 'A', 'N'],
          ['R', 'E', 'K', 'N', 'O', 'O', 'O', 'D', 'G', 'P'],
          ['E', 'M', 'R', 'A', 'N', 'T', 'I', 'W', 'A', 'R'],
          ['C', 'O', 'A', 'P', 'H', 'R', 'A', 'S', 'E', 'D'],
          ['L', 'C', 'D', 'X', 'T', 'O', 'J', 'O', 'E', 'R'],
          ['U', 'L', 'H', 'E', 'O', 'H', 'O', 'K', 'U', 'M'],
          ['H', 'E', 'W', 'E', 'U', 'P', 'C', 'R', 'N', 'D'],
          ['O', 'W', 'H', 'N', 'G', 'O', 'N', 'E', 'T', 'P'],
          ['S', 'R', 'E', 'T', 'H', 'G', 'I', 'F', 'I', 'H'],
          ['T', 'M', 'E', 'C', 'E', 'H', 'S', 'U', 'D', 'O'],
          ['E', 'J', 'D', 'V', 'N', 'E', 'P', 'S', 'I', 'B'],
          ['L', 'L', 'E', 'T', 'E', 'R', 'E', 'E', 'E', 'I'],
          ['S', 'R', 'D', 'E', 'D', 'F', 'P', 'S', 'R', 'A'],
]

print("Word Search Puzzle")
for row in range(len(puzzle)):
  for col in range(len(puzzle[row])):
    print(puzzle[row][col], end=" ")
  print()

print("""
==========================================================
||                   KATA TERSEMBUNYI                   ||
||------------------------------------------------------||
|| ANTIWAR      | HOPEFUL   | PHRASED       | WELCOME   ||
|| CHOCKED      | JET       | POISE         |           ||
|| DARKENS      | JOT       | POWER         |           ||
|| EGGS         | MEAN      | RAGA          |           ||
|| EXPANDS      | MENU      | REFUSES       |           ||
|| FEVER        | METED     | RETELL        |           ||
|| FIGHTERS     | NADIR     | TELS          |           ||
|| HEEDED       | PACE      | TOUGHENED     |           ||
|| HOKUM        | PEPSIN    | ULCERATE      |           ||
|| HOSTEL       | PHOBIA    | UNTIDIER      |           ||
==========================================================
""")

print("""Strategi Algoritma:
1. Brute Force
2. Backtracking
""")

word = str(input("Kata yang Ingin Dicari: "))
opt = int(input("Algoritma yang Ingin Digunakan (1/2): "))

print()
print("========== MEMULAI PENCARIAN ==========")

start_time = time.time()
if (opt == 1):
  BruteForce(puzzle, word)
  print("Waktu Brute Force: %s seconds ---" % (time.time() - start_time))

else:
  Backtracking(puzzle, word)
  print("Waktu Backtracking: %s seconds ---" % (time.time() - start_time))


print("========== PENCARIAN SELESAI ==========")
