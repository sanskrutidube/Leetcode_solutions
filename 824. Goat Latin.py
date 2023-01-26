class Solution:
    def toGoatLatin(self, S: str) -> str:
        temp = []
        ans = " "  
        i = 1
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for word in S.split(" "):
            if word[0] in vowel:
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word = word + "a"*i
            i = i + 1
            temp.append(word)
		
        return ans.join(temp)
    
-------------------------------------------------------------------------------

class Solution:
    def toGoatLatin(self, S):
        words = S.split()
        vowels = set("AEIOUaeiou")
        for i in range(len(words)):
            if words[i][0] in vowels:
                words[i] = words[i] + "ma" + "a"*(i+1)
            else:
                words[i] = words[i][1:] + words[i][0] + "ma" + "a"*(i+1)
                
        return " ".join(words)
        
