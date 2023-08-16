class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxi = i = 0
        memo = Counter()
        for j in range(len(answerKey)):
            memo[answerKey[j]] += 1
            maxi = max(maxi,memo[answerKey[j]])
            if j-i+1 > maxi + k:
                memo[answerKey[i]] -= 1
                i += 1
        return j - i + 1

            

 


