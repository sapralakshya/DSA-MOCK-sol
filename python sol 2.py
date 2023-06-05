
def find_non_repeat_char(s):
    for i in range(len(s)):
        cnt = s.count(s[i])
        if cnt == 1:
            return i
    return -1
s="leetcode"
print(find_non_repeat_char(s))


