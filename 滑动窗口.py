class Solution():
    def hd(self,nums,k):
        # l,s,m=0,0,float("-inf")
        # for r,n in enumerate(nums):
        #     s+=n
        #     if(r-l+1==k):
        #         m=max(m,s)
        #     if(r+1>=k):
        #         s-=nums[l]
        #         l+=1
        # return m/k
        # # while(r<len(nums)):
        # #     r+=1
        # #     if(r-l==k):
        # #         a=sum(nums[l:r])/k
        # #         avg=max(avg,a)
        # #         l+=1
        # # return avg
        l, avg = 0, float("-inf")
        for r in range(len(nums)):
            if (r - l + 1 == k):
                a = sum(nums[l:r+1])
                avg = max(avg, a)
                l += 1
        return avg / k
p=Solution()
print(p.hd([1,12,-5,-6,50,3],4))
