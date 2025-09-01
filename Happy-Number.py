class Solution:
    def isHappy(self, n: int) -> bool:
        seen ={}
        current_sum = 0
        trails = 0
        while current_sum !=1 and trails < 10:
            current_sum = 0
            for j in str(n):
                # print(int(j)*int(j), current_sum)
                if j not in seen.keys():
                    seen[j]= int(j)*int(j)
                current_sum = current_sum + seen[j]
                # print(n, j, current_sum)
            n = current_sum
            trails +=1
        return current_sum==1
        