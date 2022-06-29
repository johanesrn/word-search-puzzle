def Backtracking(puzzle, word):
  firstLetter = word[0]
  secondLetter = word[1]
  lenWord = len(word)
  totRow = len(puzzle)
  totCol = len(puzzle[0])

  for row in range(len(puzzle)):
    for col in range(len(puzzle[row])):
      if (puzzle[row][col] == firstLetter):
        
        # Cek Arah ATAS
        try:
          if ((puzzle[row-1][col] == secondLetter) and (row-1 >= 0)) and (row-(lenWord-1) >= 0):
            match = True
            idx = 2
            while (idx < lenWord) and match:
              if (puzzle[row-idx][col] == word[idx]) and (row-idx >= 0):
                idx += 1
              else:
                match = False
            if match:
              print('Kata Tersembunyi ditemukan di Posisi: [{},{}]'.format(row+1,col+1))
              print("Arah : ", end="")
              print("VERTIKAL KE ATAS")
              return;
        except IndexError:
          pass
        
        # Cek Arah KANAN ATAS
        try:
          if ((puzzle[row-1][col+1] == secondLetter) and (row-1 >= 0)) and (row-(lenWord-1) >= 0 and col+lenWord <= totCol):
            match = True
            idx = 2
            while (idx < lenWord) and match:
              if (puzzle[row-idx][col+idx] == word[idx]) and (row-idx >= 0):
                idx += 1
              else:
                match = False
            if match:
              print('Kata Tersembunyi ditemukan di Posisi: [{},{}]'.format(row+1,col+1))
              print("Arah : ", end="")
              print("DIAGONAL KE KANAN ATAS")
              return;
        except IndexError:
          pass

        # Cek Arah KANAN
        try:
          if (puzzle[row][col+1] == secondLetter) and (col+lenWord <= totCol):
            match = True
            idx = 2
            while (idx < lenWord) and match:
              if (puzzle[row][col+idx] == word[idx]):
                idx += 1
              else:
                match = False
            if match:
              print('Kata Tersembunyi ditemukan di Posisi: [{},{}]'.format(row+1,col+1))
              print("Arah : ", end="")
              print("HORIZONTAL KE KANAN")
              return;
        except IndexError:
          pass
        
        # Cek Arah KANAN BAWAH
        try:
          if (puzzle[row+1][col+1] == secondLetter) and (row+lenWord <= totRow and col+lenWord <= totCol):
            match = True
            idx = 2
            while (idx < lenWord) and match:
              if (puzzle[row+idx][col+idx] == word[idx]):
                idx += 1
              else:
                match = False
            if match:
              print('Kata Tersembunyi ditemukan di Posisi: [{},{}]'.format(row+1,col+1))
              print("Arah : ", end="")
              print("DIAGONAL KE KANAN BAWAH")
              return;
        except IndexError:
          pass

        # Cek Arah BAWAH
        try:
          if (puzzle[row+1][col] == secondLetter) and (row+lenWord <= totRow):
            match = True
            idx = 2
            while (idx < lenWord) and match:
              if (puzzle[row+idx][col] == word[idx]):
                idx += 1
              else:
                match = False
            if match:
              print('Kata Tersembunyi ditemukan di Posisi: [{},{}]'.format(row+1,col+1))
              print("Arah : ", end="")
              print("VERTIKAL KE BAWAH")
              return;
        except IndexError:
          pass

        # Cek Arah KIRI BAWAH
        try:
          if ((puzzle[row+1][col-1] == secondLetter) and (col-1 >= 0)) and (row+lenWord <= totRow and col-(lenWord-1) >= 0):
            match = True
            idx = 2
            while (idx < lenWord) and match:
              if (puzzle[row+idx][col-idx] == word[idx]) and (col-idx >= 0):
                idx += 1
              else:
                match = False
            if match:
              print('Kata Tersembunyi ditemukan di Posisi: [{},{}]'.format(row+1,col+1))
              print("Arah : ", end="")
              print("DIAGONAL KE KIRI BAWAH")
              return;
        except IndexError:
          pass
        
        # Cek Arah KIRI
        try:
          if ((puzzle[row][col-1] == secondLetter) and (col-1 >= 0)) and (col-(lenWord-1) >= 0):
            match = True
            idx = 2
            while (idx < lenWord) and match:
              if (puzzle[row][col-idx] == word[idx]) and (col-idx >= 0):
                idx += 1
              else:
                match = False
            if match:
              print('Kata Tersembunyi ditemukan di Posisi: [{},{}]'.format(row+1,col+1))
              print("Arah : ", end="")
              print("HORIZONTAL KE KIRI")
              return;
        except IndexError:
          pass
        
        # Cek Arah KIRI ATAS
        try:
          if ((puzzle[row-1][col-1] == secondLetter) and (row-1 >= 0 and col-1 >= 0)) and (row-(lenWord-1) >= 0 and col-(lenWord-1) >= 0):
            match = True
            idx = 2
            while (idx < lenWord) and match:
              if (puzzle[row-idx][col-idx] == word[idx]) and (row-idx >= 0 and col-idx >= 0):
                idx += 1
              else:
                match = False
            if match:
              print('Kata Tersembunyi ditemukan di Posisi: [{},{}]'.format(row+1,col+1))
              print("Arah : ", end="")
              print("DIAGONAL KE KIRI ATAS")
              return;
        except IndexError:
          pass

  print("Kata Tidak Ditemukan")
  return;
