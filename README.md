# Blackjack

Blackjack, to be played in the terminal. 

Designed by Gabriel Buchdahl for the Kleiner Perkins Fellowship Engineering Challenge.

In keeping with the spirit of the challenge, I did not spend more than 3 hours making this game, which may in turn mean that the tests are not fully written out. 

### Running Code
First, we must clone the repo and install the dependencies.
After cloning, running
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
should install the library I used. From there, running `python3 game.py` should launch the game.

Running the other files in the repo, such as `python3 printing.py` or `python3 card.py`, should run small unit tests on those modules to make sure they work.

### Design Choices
I chose to write the cards and players as a class, in order to keep a bunch of information and methods easily contained in one location. This allowed me to use mostly arrays to store the hands, which simplified everything. My deck was implemented somewhat like a stack, as well, but I did not really use it like a stack. The deck was intended to be similar enough to a real deck that counting cards would end up being an effective strategy if executed properly.

### Tooling Choices
I chose to write everything in Python as it is the language I am most comfortable with. I used cutie to help me parse input becuase I only had three hours to design everything and it made my game look cleaner without adding much effort at all. I think if I had more time I would have chosen to write everything out myself, as I didn't really need much added functionality.