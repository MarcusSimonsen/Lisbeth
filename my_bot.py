from poker_game_runner.state import Observation
from poker_game_runner.utils import Range, HandType
import time
import random

class Bot:
  def get_name(self):
      return "Lisbeth"

  def act(self, obs: Observation):
    my_hand = obs.get_my_hand_type()
    board_hand = obs.get_board_hand_type()

    if my_hand > board_hand and obs.current_round >= 1:
       return obs.get_max_raise()

    if obs.get_call_size() == obs.get_max_raise():
       return 0
    
    # If hand is good
    # raise a little bit
    #good_hand = Range("66+, A7s+, K9s+, QTs+, JTs, ATo+, KJo+")
    good_hand = Range("66+, A7s+, K9s+, QTs+, JTs, ATo+, KJo+")
    if good_hand.is_hand_in_range(obs.my_hand):
       return int(obs.get_max_raise() * 0.05)
    
    bad_hand = Range("82o, 72o, 62o, 52o, 42o, 32o")
    if bad_hand.is_hand_in_range(obs.my_hand):
       if obs.get_call_size() == 0:
          return 1
       return 0


    return obs.get_min_raise()
