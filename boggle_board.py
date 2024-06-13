import random
import string

class BoggleBoard:

  game_board = "____\n____\n____\n____"
  
  def __init__(self):
    print(BoggleBoard.game_board)
    


  def shake(self):
    self.dice = [
      "AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO",
      "EHRTVW", "CIMOTU", "DISTTY", "EIOSST", 
      "DELRVY", "ACHOPS", "HIMNQU", "EEINSU", 
      "EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"
      ]
    BoggleBoard.game_board = ""

    """This for loop works for creating the correct board but doesnt use the dice variable"""
    # for row in range(4): 
    #   BoggleBoard.game_board += "\n" 
    #   for column in range(4): 
    #       BoggleBoard.game_board += random.choice(string.ascii_letters.upper())
    # print(BoggleBoard.game_board)

    """this loop uses the dice variable"""
    index_count = 0
    for dice_face in self.dice:
      letter = random.choice(dice_face)
      if index_count % 4 == 0:
        BoggleBoard.game_board += "\n"
        BoggleBoard.game_board += letter
      else:
        BoggleBoard.game_board += '  '
        BoggleBoard.game_board += letter
      final = BoggleBoard.game_board.replace("Q ", "Qu") 
      index_count += 1
    print(final)





new_game = BoggleBoard()
new_game.shake()

# P  N  O  T
# S  A  F  G
# S  V  L  T
# L  Qu Z  F