from state import State
from utils import  W, Property as P, best_words_from_set, evaluate_guess



def get_letter_freq_in_W(): #modify init_alphabet: [] -> [0]
    s = State()
    for w in W:
        print(w)
        for l in list(w):
            print(l)
            s.alphabet.update({l : P("white",[s.alphabet[l].info[0]+1])})
    return s



bb = best_words_from_set(set(list("mycup")),verbose=True) #  CHUMP !!!!! 3e guess

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