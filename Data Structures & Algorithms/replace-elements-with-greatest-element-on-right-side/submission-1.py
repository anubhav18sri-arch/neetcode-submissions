class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output=[]
        for i in range(len(arr)):
            temp = []
            for j in range(i + 1, len(arr)):
                 temp.append(arr[j])
            if temp:
                 output.append(max(temp))
            else:
                 output.append(-1)
            
        return output