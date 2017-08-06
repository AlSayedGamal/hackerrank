def is_matched(expression):
    opening = ["{","[", "("]
    closing = ["}", "]", ")"]
    open_close_mapper = {"{":"}", "}":"{", "[":"]", "]":"[", "(":")", ")":"("}
    b_closing = []
    for c in list(expression):
        if c in opening:
            # pushing into the stack
            b_closing.append(open_close_mapper[c])
        elif c in closing:
            #poping from stack
            if len(b_closing):
                matched_closing_bracket = b_closing.pop()
                if matched_closing_bracket != c:
                    return False
            else:
                return False
    if len(b_closing) == 0:
        return True
    else:
        return False

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
