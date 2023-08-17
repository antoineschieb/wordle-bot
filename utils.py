class Property:
    def __init__(self,color,info) -> None:
        assert color in ["green","yellow","white","gray"]
        self.color = color
        assert isinstance(info,list)
        self.info = info

    def __repr__(self) -> str:
        return f'<{self.color} {self.info}>'

def load_words(prefix): #"allowed" or "possible"
    W=list()
    
    # with open('data/words.txt') as f:
    if prefix=="allowed":filestr = "data/words.txt"
    else: filestr = "data/possible_words.txt"

    with open(filestr) as f:
            for line in f:
                W.append(line[:-1])
    return W
AW = load_words("allowed")
PW = load_words("possible")

def evaluate_guess(target,guess,verbose=True):
    assert len(target)==len(guess)==5
    props = [Property("gray",[]),Property("gray",[]),Property("gray",[]),Property("gray",[]),Property("gray",[])]
    for idx,(t,g) in enumerate(zip(target,guess)):
        if t==g:
            props[idx]=Property("green",[idx])
        elif g in target:
            props[idx]=Property("yellow",[idx])
    
    list_ret = list()
    for i,letter in enumerate(guess):
        list_ret.append((letter,props[i]))

    if verbose:
        print(f'eval: {list_ret}')
        print('\n')
    
    return list_ret


def best_words_from_set(s,verbose=False):
    global AW
    max_l = 0
    ret = []
    for w in AW:
        ws = set(w)
        inter = ws.intersection(s)
        l = len(inter)
        if l >= max_l:
            if l!=max_l:
                ret=[]
            ret.append(w)
            max_l = l
    if verbose:print(f'{max_l} : words {ret}')
    return ret


