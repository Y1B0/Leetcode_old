def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    res = []
    if len(digits) == 0:
        return [""]
    old = letterCombinations(digits[:-1]) # combination except the last one
    lastdigit = digits[-1]
    letters = d.get(lastdigit)
    for letter in letters:
        for string in old:
            res.append(string + letter)
#            print letter
#    print res
    return res

print letterCombinations("234")