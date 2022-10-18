class Solution:
    def romanToInt(self,s:str):
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000, 'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        length = len(s)
        char = ['IV','IX','XL','XC','CD','CM']
        num = 0
        i = 0
        a=''
        while i < length: 
            if i < (length-1):
                a = s[i]+s[i+1]
            if a in char:
                num = num + d[a]
                i += 2
                a =''
                continue
            else:
                num = num+d[s[i]]
                i += 1
        return(num)
            
        
