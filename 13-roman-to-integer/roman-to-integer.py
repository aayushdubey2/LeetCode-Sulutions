# The intutuion here is if the current character has the value lesser than the next character 
# then subtract it from the total
# Take example of 9 - IX 
# if we remove value of I and then add the value of X we get the correct answer
# similarly CM is 900
# to get the correct value we need to subtract C that is 100 and then add M that is 1000 to get 900

class Solution:
    def romanToInt(self, s: str) -> int:
        symbolToValue = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        answer = 0

        for i in range(0, len(s)-1):
            if symbolToValue[s[i]]<symbolToValue[s[i+1]]:
                answer -= symbolToValue[s[i]]
            else:
                answer+=symbolToValue[s[i]]
        answer+= symbolToValue[s[-1]]
        return answer

        