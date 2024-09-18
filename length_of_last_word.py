class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        #creating an empty list to store the substring
        result = []

        #removing the trailing places
        s=s.rstrip()

        #iterating over the string in reverse
        for char in s[::-1]:

        # stopping the iteration if a space is encountered
            if char == " ":
                break
        # Append non-space characters to result
            result.append(char)
        
       
       # Join the result list into a string
        reversed_string = ''.join(result)

        return len(reversed_string)
    

#alternate solution

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split()

        if s:
            return len(s[-1])
        else:
            return 0
        