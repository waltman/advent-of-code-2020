def rule0(s):
    for i in range(1,len(s)-1):
        for j in range(i+1, len(s)):
            if rule4(s[0:i]) and rule1(s[i:j]) and rule5(s[j:]):
                return True
    return False

def rule1(s):
    for i in range(1,len(s)):
        if (rule2(s[0:i]) and rule3(s[i:])) or (rule3(s[0:i]) and rule2(s[i:])):
            return True
    return False

def rule2(s):
    for i in range(1,len(s)):
        if (rule4(s[0:i]) and rule4(s[i:])) or (rule5(s[0:i]) and rule5(s[i:])):
            return True
    return False

def rule3(s):
    for i in range(1,len(s)):
        if (rule4(s[0:i]) and rule5(s[i:])) or (rule5(s[0:i]) and rule4(s[i:])):
            return True
    return False

def rule4(s):
    return s == 'a'

def rule5(s):
    return s == 'b'

for s in ['ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb']:
    print(s, rule0(s))
