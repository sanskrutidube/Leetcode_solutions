class Solution:
    def countAsterisks(self, s):
        return(sum([a.count('*') for a in s.split('|')][0::2]))
----------------------------------------------------------------------

class Solution:
    def countAsterisks(self, s: str) -> int:
        lst=[] 
        for i in s: 
            if '|' not in lst: 
                lst.append(i) 
            elif '|' in lst and i=='|': 
                lst.pop() 
        return lst.count('*')
 --------------------------------------------------------------------
 
 class Solution:
    def countAsterisks(self, s: str) -> int:
        l = []
        temp = ''
        for i in s:
            if i == '|':
                temp += i
               
                if temp.count('|') == 2:
                    temp = ''
            
            if '|' in temp:
                continue
            
            elif i != '|':
                l.append(i)
        return ''.join(l).count('*')
