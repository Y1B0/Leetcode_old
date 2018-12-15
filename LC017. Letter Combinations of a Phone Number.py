class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits) == 0:
            return []
        res = ['']
        for i,d in enumerate(digits):
            keys = table.get(d)
            new_res = []
            for j,elem in enumerate(keys):
                for item in res:
                    new_res.append(item + elem)
            res = new_res
        return res
                    
