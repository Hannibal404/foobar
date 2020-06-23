def answer(s):
    try:
        return max([s.count(s[:x]) for x in range(len(s)) if s[:x]*s.count(s[:x]) == s])
    except Exception:
        return 1
print(answer("abcabcabcabc"))
print(answer("abccbaabccba"))
print(answer("abccbaabccb"))