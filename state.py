import string
from copy import deepcopy

from utils import Property, PW, evaluate_guess, best_words_from_set 




def init_alphabet():
    M = dict()
    for x in string.ascii_lowercase:
        M.update({x:Property("white",[])})
    return M

class State:
    def __init__(self) -> None:
        self.guess_so_far = list('_____')
        self.yellow_set = set()
        self.alphabet = init_alphabet()

    def __repr__(self) -> str:
        ret =   f'\nGuess so far :     {"".join(self.guess_so_far)}\n' + \
                f'yellow letters:    {self.yellow_set}\n' + \
                f'alphabet:          {self.alphabet}\n\n'  
        return ret

    def get_white_yellow_set(self):
        s=set()
        for k,v in self.alphabet.items():
            if v.color=="white" or v.color=="yellow":
                s.add(k)
        return s


    def update_from_eval(self,eval):
        """ Update state from evaluation object (list of 5 tuples where each tuple is ('letter',Property()) """
        for letter,prop in eval:

            assert prop.color!="white" # No eval should ever return a white tile.

            if prop.color=="green":
                self.guess_so_far[prop.info[0]] = letter
                self.alphabet[letter] = prop
                        
            if prop.color=="yellow":
                # Add to yellow set
                self.yellow_set.add(letter)
                
                # change alphabet only if it wasnt a green letter
                if self.alphabet[letter].color != "green":
                    # property is now either white or yellow
                    
                    if self.alphabet[letter].color == "yellow":
                        v = prop.info[0]
                        self.alphabet[letter].info.append(v)
                    
                    if self.alphabet[letter].color == "white":
                        self.alphabet[letter] = prop
            
            if prop.color=="gray":
                # change alphabet only if it wasnt a green letter
                if self.alphabet[letter].color != "green":
                    self.alphabet[letter] = prop
        
        return 

    def could_be(self,word):
        """Check if a word could be the final answer for this current state"""
        # First, check if it matches our guess so far
        
        for i,l in enumerate(self.guess_so_far):
            if l=='_':continue
            if list(word)[i] != l:
                return False

        # Now check that all the letters in the yellow set appear in the candidate word
        for l in self.yellow_set:
            if l not in list(word):return False

        # Finally, check the properties of each letter of the candidate word in our alphabet
        for i,l in enumerate(list(word)):
            if self.alphabet[l].color == "gray":return False
            if self.alphabet[l].color == "yellow" and i in self.alphabet[l].info:return False 

        return True


    def get_all_words(self,verbose=False):
        """Get all words that could be a valid final answer for the current state"""
        global PW
        c=0
        r=list()
        for w in PW:
            if self.could_be(w):
                if verbose:print(w)
                r.append(w)
                c+=1
        if verbose:print(f'{c} possible words.')
        return r



    def propose_word(self):
        # global AW
        possible_words = self.get_all_words()
        min_mean_score = float(len(possible_words))
        idx_ret = 0
        WYS = self.get_white_yellow_set()
        constructible_words = best_words_from_set(WYS)
        print(f'number of words to choose from : {len(constructible_words)}')
        
        for widx,w in enumerate(constructible_words):
            mean_score = 0
            for pw in possible_words:
                """Let's assume that the target is pw"""
                ps = deepcopy(self) # possible state (if pw is the actual target)
                e = evaluate_guess(pw,w,verbose=False)
                ps.update_from_eval(e)
                l = len(ps.get_all_words(verbose=False))
                mean_score += l/len(possible_words)
            # print(f'mean score for word {w} is {mean_score}.')
            print(f'propose_word {round(100*widx/len(constructible_words),2)}%', end="\r")
            if mean_score <= min_mean_score:
                min_mean_score = mean_score
                idx_ret = widx
                print(f'propose_word {round(100*idx_ret/len(constructible_words),2)}% : {min_mean_score} average possibilities for word {w}')
                if mean_score <= 1:
                    return constructible_words[idx_ret]
        print("                       ")
        return constructible_words[idx_ret]
