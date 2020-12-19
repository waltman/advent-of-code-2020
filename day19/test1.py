def rule0(s):
    for i in range(1,len(s)):
        if rule1(s[0:i]) and rule2(s[i:]):
            return True
    return False

def rule1(s):
    return s == 'a'

def rule2(s):
    for i in range(1,len(s)):
        if (rule1(s[0:i]) and rule3(s[i:])) or (rule3(s[0:i]) and rule1(s[i:])):
            return True
    return False

def rule3(s):
    return s == 'b'

for s in ['a', 'b', 'aab', 'aba', 'aaa', 'bab']:
    print(s, rule0(s))
