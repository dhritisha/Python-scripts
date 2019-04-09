def balanced(open, close):
    if open=='(' and close==')':
        return True
    elif open=='{' and close=='}':
        return True
    elif open=='[' and close==']':
        return True
    else:
        return False


def balance_bracket(text):
    open_bracket=['(', '{', '[']
    close_bracket=[')', '}', ']']
    stack=list()
    for i in range(0,len(text)):

        if text[i] not in open_bracket and text[i] not in close_bracket:
            continue

        if len(text) == 1:
            return str(1)

        if text[i] in open_bracket and len(stack)==0:
            stack.append((text[i], i+1))
            continue
        elif text[i] in close_bracket and len(stack)==0:
            return str(i+1)

        prev=stack.pop(-1)
        prevbracket=prev[0]
        prevpos=prev[1]

        if prevbracket in open_bracket and text[i] in close_bracket:
            check_balance=balanced(prevbracket,text[i])
            if not check_balance:
                return str(i+1)
        elif prevbracket in open_bracket and text[i] in open_bracket:
            stack.append(prev)
            stack.append((text[i],i+1))
        elif prevbracket in close_bracket and text[i] in open_bracket:
            return str(prevpos)

    if len(stack) != 0:
        element=stack[0]
        pos=element[1]
        return str(pos)
    else:
        return "Success"






if __name__=="__main__":
    text=input()
    out=balance_bracket(text)
    if out.isdigit():
        print(out)
    else:
        print("Success")
