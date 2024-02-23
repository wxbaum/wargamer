# Wargamer

## Overview
Wargamer is a Streamlit based app designed to provide a "servicable" opponent 
in a solitaire wargame. The primary aim of the app is to allow a player to 
fully control one faction in a game, while removing as much decision making as 
possible for the actions of the opposing faction. Doing so means the human 
player faces an army whose actions cannot be fully influenced by the conscious 
or subconcious thoughts and plans of the human player, resulting in a
significantly more satisfying solitaire experience.

## How it Works
The underlying dataset contains three types of actions for each phase of play:
1) Primary action
2) Backup action
3) Secondary backup action

The primary action is a reasonably specific instruction that will be usable in the 
majority of battefield scenarios. Inevitably, the primary action will be too
specific and/or not apply in some situations. In such cases, the backup action
is a more generic instruction with wider applications, and should be used instead. 
In the case that the backup action also cannot be used, the secondary backup action 
is generic to the point where only extreme edge case scenarios cannot have the 
instruction applied. In the case that happens, a new card can be drawn.

The primary, backup, and secondary backup instructions are each selected at random
from a larger list of possible options for all three, respectively. As such, there
are a large number of possible cards that can be drawn. For example, if one phase 
contains five instructions for each of primary, backup, and secondary backup, there
are 125 possible card combinations for that phase. 

The cards should be used on an army-level basis where the card instructions are 
given to all applicable units, or on a unit-level basis where a new card is drawn 
for each unit. Applying a card to a subset of units will introduce a level of 
"choosing" bias from the solitaire human player and should be avoided. 


