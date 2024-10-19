
def eval(s, bool_val):
    r = s[0]
    b = s[1]
    if bool_val:  
        return (2*r + 3*b)
    else:  
        return -(2*r + 3*b)

def is_terminal(s):
    r = s[0]
    b = s[1]
    if r == 0 or b == 0:
        return True
    return False

def max_value(s, type, alpha, beta):
    bool = False
    if type == 'misere':
        bool = True
    if is_terminal(s):
        return eval(s, bool), s
    r = s[0]
    b = s[1]
    

    val = float('-inf')
    state = s
    terminal_val = 0
    if r >= 2:
        terminal_val, _ = min_value([r-2, b], type, alpha, beta)
        if terminal_val > val:
            val = terminal_val
            state = [r-2, b]  
            print(state)
            if val > alpha:
                alpha = val
            if alpha >= beta:
                return val, state    
    if b >= 2:
        terminal_val, _ = min_value([r, b-2], type, alpha, beta)
        if terminal_val > val:
            val = terminal_val
            state = [r, b-2]
            print(state)
            if val > alpha:
                alpha = val
            if alpha >= beta:
                return val, state  
    if r >= 1:
        terminal_val, _ = min_value([r-1, b], type, alpha, beta)
        if terminal_val > val:
            val = terminal_val
            state = [r-1, b]
            print(state)
            if val > alpha:
                alpha = val
            if alpha >= beta:
                return val, state
    
    if b >= 1:
        terminal_val, _ = min_value([r, b-1], type, alpha, beta)
        if terminal_val > val:
            val = terminal_val
            state = [r, b-1]
            print(state)
            if val > alpha:
                alpha = val
            if alpha >= beta:
                return val, state
    return val, state

def min_value(s, type, alpha, beta):
    bool = True
    if type == 'misere':
        bool = False
    if is_terminal(s):
        return eval(s, bool), s
    r = s[0]
    b = s[1]
    val = float('inf')
    state = s
    terminal_val = 0
    if r >= 2:
        terminal_val, _ = max_value([r-2, b], type, alpha, beta)
        
        if terminal_val < val:
            val = terminal_val
            state = [r-2, b]
            print(state)
            if val < beta:
                beta = val
            if alpha >= beta:
                return val, state
    if b >= 2:
        terminal_val, _ = max_value([r, b-2], type, alpha, beta)
        if terminal_val < val:
            val = terminal_val
            state = [r, b-2]
            print(state)
            if val < beta:
                beta = val
            if alpha >= beta:
                return val, state        
    
    if r >= 1:
        terminal_val, _ = max_value([r-1, b], type, alpha, beta)
        if terminal_val < val:
            val = terminal_val
            state = [r-1, b]
            print(state)
            if val < beta:
                beta = val
            if alpha >= beta:
                return val, state
    
    if b >= 1:
        terminal_val, _ = max_value([r, b-1], type, alpha, beta)
        if terminal_val < val:
            val = terminal_val
            state = [r, b-1]
            print(state)
            if val < beta:
                beta = val
            if alpha >= beta:
                return val, state
    
    return val, state
    

v = 9


red = 3
blue = 3
s = [red, blue]
print(s)
type = "misere"

if type == 'misere':
    while 1:
        if is_terminal(s):
            print(f"Player wins by {eval(s, True)} points")
            exit()
        choice = input("""Choose one of the following move:
              1. Pick 1 red marble
              2. Pick 2 red marble
              3. Pick 1 blue marble
              4. Pick 2 blue marble 
              """)
        if choice == "1":
            s[0] -= 1
        elif choice == "2":
            if s[0] < 2:
                print("Invalid move")
                continue
            s[0] -= 2
        elif choice == "3":
            s[1] -= 1
        else:
            if s[1] < 2:
                print("Invalid move")
                continue
            s[1] -= 2
        print(s)
        if is_terminal(s):
            print(f"Computer wins by {eval(s, True)} points")
            exit()
        _, s = max_value(s, type, float("-inf"), float("inf"))
        print(s)
else:
    while 1:
        
        choice = input("""Choose one of the following move:
              1. Pick 1 red marble
              2. Pick 2 red marble
              3. Pick 1 blue marble
              4. Pick 2 blue marble 
              """)
        if choice == "1":
            s[0] -= 1
        elif choice == "2":
            if s[0] < 2:
                print("Invalid move")
                continue
            s[0] -= 2
        elif choice == "3":
            s[1] -= 1
        else:
            if s[1] < 2:
                print("Invalid move")
                continue
            s[1] -= 2
        if is_terminal(s):
            print(f"Player wins by {eval(s, True)} points")
            exit()    
        print(s)
        
        _, s = max_value(s, type)
        print(s)
        if is_terminal(s):
            print(f"Computer wins by {eval(s, True)} points")
            exit()


