# Uno Game

Uno is a classic card game that is simple to learn but can be complex to master. The goal is to be the first player to use all your cards, using strategies to combat your opponents. This version of Uno is a simplified, console-based game that allows you to play against AI opponents.

## Setup
- Number of Players: 2 to 10
- Deck: 108 cards, including four suits (Red, Green, Blue, Yellow), numbered cards, and special action and wild cards.

## Game Components
- Number Cards: 0 to 9 for each color.
- Action Cards: Skip, Reverse, Draw Two for each color.
- Wild Cards: Wild and Wild Draw Four.

## How to Play
1. Start: Each player is dealt 7 cards. The remaining deck forms the draw pile. The top card from the draw pile is turned over to start the discard pile.
2. Turns: Players take turns in a clockwise direction, starting from Player 1.
3. Playing Cards: On your turn, play a card from your hand that matches the color, number, or action of the top card on the discard pile.
   - If you cannot play a card, draw one from the draw pile. If the drawn card can be played, play it.
4. Special Cards:
   - Skip: The next player is skipped.
   - Reverse: Reverses the direction of play.
   - Draw Two: The next player draws two cards and is skipped.
   - Wild: Play this card to change the color being matched.
   - Wild Draw Four: Change the color and force the next player to draw four cards and lose their turn. Cannot be played if you have another playable card.
5. Saying 'Uno': When you have only one card left, you must say 'Uno'. (Note: In this console version, you'll need to mentally note this as the game won't prompt you.)
6. Winning: The first player to use all their cards wins.

## Running the Game
To start the game, ensure Python is installed on your system. Navigate to the game's directory in your terminal or command prompt and run:

python uno_game.py


