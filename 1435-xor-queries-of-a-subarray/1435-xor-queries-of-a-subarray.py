class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        pref = [0] * (len(arr) +1)

        for i in range(1, len(arr)+1):
            pref[i] = pref[i-1] ^ arr[i-1]

        
        for left, right in queries:
            answer.append(pref[right+1] ^ pref[left])
        
        return answer