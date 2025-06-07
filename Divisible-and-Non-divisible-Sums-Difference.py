class Solution:
    # def differenceOfSums(self, n: int, m: int) -> int:
    #     div1 = 0
    #     no_div = 0
    #     for i in range(1, n+1):
    #         if i%m ==0:
    #             div1+=i
    #         else:
    #             no_div+=i
    #     return no_div - div1
    def differenceOfSums(self, n: int, m: int) -> int:
        div1 = 0
        no_div = n * (n+1) //2
        for i in range(m, n+1, m):
            div1+=i
            no_div-=i
        return no_div - div1


        