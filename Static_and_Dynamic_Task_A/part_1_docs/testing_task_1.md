### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #should be: if card.value == 1:
      return True
    else
      return False
   

  dif highest_card(self, card1 card2): #Spelling for def is wrong and there is a comma missing between card1 and card2.
  if card1.value > card2.value:
    return card #card is not one of the objects passed into the function, it should be card1.
  else:
    return card2 #Indentation is incorrect.
  


def cards_total(self, cards):
  total #total is undefined
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
