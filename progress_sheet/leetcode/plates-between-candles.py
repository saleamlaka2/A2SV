class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []

        for i in range(len(s)):
            if s[i] != '*':
                candles.append(i)

        answer = []

        for left, right in queries:
            if not candles:
                answer.append(0)
                continue
            left_most = bisect_left(candles, left)
            right_most = bisect_right(candles, right)

            right_most = max(right_most - 1, 0)
            if left_most == len(candles):
                left_most = max(left_most - 1, 0)
                
            curr_answer = max(candles[right_most] - candles[left_most] - (right_most - left_most), 0)

            answer.append(curr_answer)
        
        return answer
            


        