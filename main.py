import random
from state import State, Property as P




def choose_random_word(W):
    return random.choice(W)








if __name__=="__main__":

    target_word = "agons"
    print(f'target word is {target_word}')

    s=State()

    
    # s.update_from_eval(evaluate_guess(target_word,"alert"))
    # s.update_from_eval(evaluate_guess(target_word,"steak"))
    # s.update_from_eval(evaluate_guess(target_word,"atgsz"))

    # print(s)
    # s.get_all_words()


    
    #e=evaluate_guess(target_word,"steak")


