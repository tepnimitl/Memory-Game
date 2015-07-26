# implementation of card game - Memory
import simplegui
import random

card = range(8)*2
num = 0
best_score = ""
cur_pos = [0,0]

# helper function to initialize globals
def new_game():
    label1.set_text("Turns = 0")
    random.shuffle(card)
    global state, exposed, match, card_a, card_b, num
    state = 0
    exposed = {}
    match = {}
    card_a = [False,'']
    card_b = [False,'']
    num = 0
    
    for a in range(len(card)) : 
        exposed[a] = False
        match[a] = False
        
# define event handlers
def mouseclick(pos):
    global cur_pos, num, state, exposed, index
    cur_pos = pos
    index = cur_pos[0] // 50	# Position of the card
    
    # add game state logic here
    if exposed[index] == True :
        pass
    else :
        if state == 0 :
            state = 1
        elif state == 1 :
            state = 2
            num += 1				# Count of Turns
            label1.set_text("Turns = %i" % (num))
        else :
            state = 1
   
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, index, best_score, card_a, card_b
    index = cur_pos[0] // 50
    
    if exposed[index] == True :				# Do nothing for exposed card
        pass
    else :
        if state == 1 :
            if (match[card_a[0]] == False) or (match[card_b[0]] == False) :
                exposed[card_a[0]] = False
                exposed[card_b[0]] = False
            card_a = [index,card[index]]	# card_a [Key,Value]
            exposed[index] = True
        elif state == 2 : 
            exposed[index] = True
            card_b = [index,card[index]]	# card_b [Key,Value]
            if card_a[1] == card_b[1] :		# Compare card_a and card_b
                match[card_a[0]] = True
                match[card_b[0]] = True
            else :
                match[card_a[0]] = False
                match[card_b[0]] = False
        else :
            exposed[index] = False

    for x in range(len(card)) :				# Drawing
        card_pos = 50 * x
        if (exposed[x] == True) or (match[x] == True) :
            canvas.draw_polygon([[card_pos,0],[card_pos,100],[card_pos+50,100],
                                 [card_pos+50,0],[0,0]], 2, 'Orange',"Green")
            canvas.draw_text(str(card[x]), (card_pos+10,75),70,"White")
        elif (exposed[x] == False) or (match[x] == False) :
            canvas.draw_polygon([[card_pos,0],[card_pos,100],[card_pos+50,100],
                                 [card_pos+50,0],[0,0]], 2, 'Orange',"Black")

    if all(y == True for y in match.values()) :			# Check if Game Over?
        canvas.draw_text("You Win !", (200,80),100,"Black")
        if num < best_score:
            best_score = num
        label2.set_text("Best Score = %i" % (best_score))	# Add Best Score
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label1 = frame.add_label("Turns = 0")
label2 = frame.add_label("Best Score = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
