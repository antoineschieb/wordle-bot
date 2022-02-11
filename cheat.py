

from state import State
from utils import Property as P, best_words_from_set


def generate_user_eval():
    word = input("which word did you type?  ")
    ev = []
    color = input(f"Which colors? (2/1/0)  ")
    for i in range(5):
        if color[i]=="2":ev.append((word[i],P("green",[i])))
        elif color[i]=="1":ev.append((word[i],P("yellow",[i])))
        elif color[i]=="0":ev.append((word[i],P("gray",[i])))
        else: raise ValueError
    return ev

        


def main():
    s = State()
    wc = 1
    while wc<=6:
        print(f'Word number {wc}')
        e = generate_user_eval()
        s.update_from_eval(e)
        s.get_all_words(verbose=True)
        WYS = s.get_white_yellow_set()
        WW = best_words_from_set(WYS)
        print(f'number of words from remaining white/yellow letter : {len(WW)}')

        x = input("do u want to search for a proposition? (y/n) :")
        if x=="y":
            proposition = s.propose_word()
            print(f"found : {proposition}")
        wc+=1

    print("you lost!!!!!!!!!")
    return 

if __name__=="__main__":
    main()
    # s = State()
    # eval1 = [   ('a',P("yellow",[0])) ,
    #             ('l',P("gray",[])) ,
    #             ('e',P("gray",[])) ,
    #             ('r',P("gray",[])) ,                                
    #             ('t',P("yellow",[4]))     
    #         ]
    # s.update_from_eval(eval1)

    # eval2 = [   ('p',P("gray",[])) ,
    #             ('o',P("gray",[])) ,
    #             ('u',P("gray",[])) ,
    #             ('t',P("yellow",[3])) ,                                
    #             ('s',P("gray",[]))     
    #         ]
    # s.update_from_eval(eval2)


    # eval3 = [   ('b',P("gray",[])) ,
    #             ('a',P("green",[1])) ,
    #             ('t',P("green",[2])) ,
    #             ('c',P("green",[3])) ,                                
    #             ('h',P("green",[4]))     
    #         ]
    # s.update_from_eval(eval3)

    # s.get_all_words()