class Solution:
    def bitwiseComplement(self, n: int) -> int:
        count = 1
        tmp = n
        while n>=2:
            count +=1
            n = n//2

        return pow(2,count)-tmp-1


class Solution2:
    def numPairsDivisibleBy60(self, time):
        len1 = len(time)
        count = 0;
        map =[0]*61
        for i in range(len1):
            time[i] = time[i]%60
            if time[i]==0:
                count+=map[0]
            else:
                count+=map[60-time[i]]
            map[time[i]] += 1
        return count

dis = 0

##该题为计数题,解法通过外层递归和内层循环遍历所有的数。bs 记录val各位已经出现过的数字。
##比如:go（0*10+i,0|(1<<i)),这里的bs已经记录上i已经出现到val中了。
class Solution4:
    def numDupDigitsAtMostN(self,N):
        n = N
        def go (val,bs):
            print(val,bs)
            global dis
            if val <= n:
                dis+=1
            if val*10 > n :
                return
            for i in range(10):
                if (not bs)and ( i==0  ):continue
                if (bs & ( 1 << i)) :
                    continue;
                go(val*10+i,bs|(1<<i))
        go(0,0)
        return N+1-dis


s = Solution4()
print(s.numDupDigitsAtMostN(120))
