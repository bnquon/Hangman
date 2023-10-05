import turtle
from wonderwords import RandomWord

sc = turtle.Screen()
sc.setup(800, 440)
t = turtle.Turtle()
r = RandomWord()
t.speed(10)
t.penup()
t.ht()

# Draw the title
def drawTitle(t):
  t.goto(0,150)
  t.write('Hangman', align='center', font=('Verdana',33, 'bold'))
  t.goto(-395,-210)
  t.write('Created by Brandon Quon', font=('Verdana',10, 'normal'))
  t.home()

# Draw the gallows
def drawStand(t):
  t.goto(-335,-75)
  t.pendown()
  t.forward(60)
  t.backward(30)
  t.left(90)
  t.forward(180)
  t.right(90)
  t.forward(60)
  t.right(90)
  t.forward(20)
  t.penup()
  t.home()

# Draw the person
def drawHangman(t, num_wrong):
  # Head
  if num_wrong == 1:
    t.goto(-245,85)
    t.right(90)
    t.pendown()
    t.right(90)
    t.circle(20)
    t.penup()
    t.home()
  # Body
  elif num_wrong == 2:
    t.goto(-245,45)
    t.pendown()
    t.right(90)
    t.forward(65)
    t.penup()
    t.home()
  # Right Arm
  elif num_wrong == 3:
    t.goto(-245,20)
    t.pendown()
    t.right(45)
    t.forward(40)
    t.penup()
    t.home()
  # Left Arm
  elif num_wrong == 4:
    t.goto(-245,20)
    t.pendown()
    t.right(135)
    t.forward(40)
    t.penup()
    t.home()
  # Right Leg
  elif num_wrong == 5:
    t.goto(-245,-20)
    t.pendown()
    t.right(60)
    t.forward(50)
    t.penup()
    t.home()
  # Left Leg
  elif num_wrong == 6:  
    t.goto(-245,-20)
    t.pendown()
    t.right(120)
    t.forward(50)
    t.penup()
    t.home()

# Draw the user's wrong guess box to keep track 
def drawWrongGuess(t):
  t.goto(120,120)
  t.pendown()
  t.forward(170)
  t.right(90)
  t.forward(90)
  t.right(90)
  t.forward(170)
  t.right(90)
  t.forward(90)
  t.right(90)
  t.penup()
  t.goto(145,100)
  t.write('Wrong Guesses', font=('Verdana',10, 'bold'))
  t.penup()
  t.home()

# Draw the actual letter they guessed in the wrong guess box
def wrongGuess(t, n, wrongLetters):
  t.goto(125 + (20*len(wrongLetters)) , 55)
  t.write(wrongLetters[n], True, font=('Verdana', 15, 'normal'))
  t.penup()
  t.home()

def playHangmanGame():
  terminated = False
  while not terminated:
    # Draw the starting graphics
    drawTitle(t)
    drawStand(t)
    drawWrongGuess(t)
    # Generate random word from Wonderwords with the given parameters 
    word = r.word(word_min_length=3, word_max_length=8)
    # Calculate proportionate starting position for the underscores
    xStart = (-20*len(word))
    
    t.goto(xStart, -100)
    # Draw the underscores
    for char in word:
      t.write('_  ', True, font=('Verdana', 25, 'normal'))

    correct = []
    wrongLetters = []
    wrong = 0
    quit = False

    # Guessing and drawing loop 
    while not quit and wrong < 6:
      # Receive user input
      letter = turtle.textinput('Hangman', 'Guess a letter')
      letter = letter.lower()
      # Make sure guessed letter isnt a repeat and doesn't take up another life and that its not in the word
      if letter not in word and letter not in wrongLetters:
        # Increase 'wrong' counter and draw the corresponding part and append the wrong letter into the array of wrong letters
        wrong += 1
        wrongLetters.append(letter)
        drawHangman(t, wrong)
        wrongGuess(t,wrong-1, wrongLetters)
      else:
        # Draw the letter if it's not already guessed correctly
        if letter not in correct:
          # Iterate through loop for multiples of the letter
          for i, char in enumerate(word):
            t.goto(xStart + 44*i, -100)
            if char == letter:
              t.pendown()  
              t.write(letter, False , font=('Verdana', 20, 'normal'))
              t.penup()
              correct.append(letter)
      # Checking if the len of correct matches with the len of the word to indicate a win
      if len(correct) == len(word):
        t.goto(0,-150)
        t.write('Congratulations You Won!!', False, align='center', font=('Verdana', 18, 'bold'))
        quit = True
    # If out of lives then it reveals the missed letters in Red
    if wrong == 6:
      t.goto(xStart, -100)
      t.color('red')
      for i, char in enumerate(word):
        if char not in correct:
          t.goto(xStart + 44*i, -100)
          t.pendown()  
          t.write(char, False , font=('Verdana', 20, 'normal'))
          t.penup()
      t.color('black') 
      t.goto(0,-150)
      t.write("You did not get the word", False, align='center', font=('Verdana', 20, 'normal'))
    # Ask user to play again
    playAgain = ''
    while playAgain != "yes" and playAgain!= "no":
      playAgain = turtle.textinput('Hangman', 'Would you like to play again ("yes" or "no")')
    if playAgain == 'yes':
      t.clear()
    elif playAgain == 'no':
      t.clear()
      t.home()
      turtle.write('Thanks for playing!', False, align='center', font=('Verdana', 22, 'bold')) 
      t.ht()
      break

# Call main loop
playHangmanGame()