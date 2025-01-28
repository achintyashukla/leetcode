class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if (not word1) or (not word2):
            return None

        newStr = []

        l1 = len(word1)
        l2 = len(word2)
        k = 0

        for i in range(max(l1,l2)):
            if i < l1:
                newStr.append(word1[i])
                k += 1

            if i < l2:
                newStr.append(word2[i])
                k += 1

        return ''.join(newStr)