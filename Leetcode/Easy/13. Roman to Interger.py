class solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        Test Cases (s):
        III
        LVIII
        MCMXCIV
        """
        # create a dictionary to store the roman numerals
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
        # set the result to 0 to later add the roman numerals
        result = 0
        # loop through the string
        for i in range(len(s)):
            # if the current roman numeral is greater than the previous one, subtract the previous one from the current one
            if i > 0 and roman[s[i]] > roman[s[i-1]]:
                # add the result to the current roman numeral
                result += roman[s[i]] - 2 * roman[s[i-1]]
            # else add the current roman numeral to the result
            else:
                result += roman[s[i]]
        # return the result
        return result
