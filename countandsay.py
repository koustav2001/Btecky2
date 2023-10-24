class Solution:
    def countandsay(self,n:int)->str
        if(n==1):
            return "1"

        prev=self.countandsay(n-1)
        res=""
        c=1
        for i in range(0,len(prev)):
            if(prev[i]!=prev[i+1] or i==len(prev)-1):
                res+=str(c)+prev[i]
                c=1
            else:
                c+=1
                
        return res
                
