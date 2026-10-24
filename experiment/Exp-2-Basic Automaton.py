def check_string(s):
    state = 0

    for ch in s:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'a':
                state = 1
            elif ch == 'b':
                state = 2
            else:
                state = 0

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    if state == 2:
        print(s, "Accepted")
    else:
        print(s, "Rejected")


check_string("ab")
check_string("aab")
check_string("abc")
check_string("abab")
