from state import State
from utils import  AW, Property as P, best_words_from_set, evaluate_guess



def get_letter_freq_in_W(): #modify init_alphabet: [] -> [0]
    s = State()
    for w in AW:
        for l in list(w):
            s.alphabet.update({l : P("white",[s.alphabet[l].info[0]+1])})
    return s


#tondi
bb = best_words_from_set(set(list("laser")),verbose=True) #  CHUMP !!!!! 3e guess

## best strat : 
# laser 4/5 most used, except l(7th) replaces o(4th)
# tondi 
# chump 

# s = State()
# for l in list("alertdinos"):
#     s.alphabet.update({l : Property("gray",[])})
# print(s)

# s.propose_word()


# s = State()

# dummyeval1 =[ 
# ('a',P("yellow",[42])),
# ('l',P("yellow",[42])),
# ('e',P("yellow",[42])),
# ('r',P("yellow",[42])),
# ('t',P("yellow",[42])),
# ]

# dummyeval2 =[ 
# ('d',P("yellow",[42])),
# ('i',P("yellow",[42])),
# ('n',P("yellow",[42])),
# ('o',P("yellow",[42])),
# ('s',P("yellow",[42])),
# ]

# s.update_from_eval(dummyeval1)
# s.update_from_eval(dummyeval2)


# s.propose_word()