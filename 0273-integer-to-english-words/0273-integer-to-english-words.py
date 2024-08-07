class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        names = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
            19: "Nineteen"
        }   

        tens = {
            20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
        }

        scales = ["", "Thousand", "Million", "Billion"]
        
        def helper(chunk):
            if int(chunk) == 0:
                return ""

            result = ""

            if len(chunk) == 3:
                if chunk[0] != "0":
                    result += names[int(chunk[0])] + " Hundred"
                chunk = chunk[1:]

            if len(chunk) == 2:
                if chunk[0] == "1":  # handle teens
                    result += " " + names[int(chunk)]
                    return result.strip()

                if chunk[0] != "0":
                    result += " " + tens[int(chunk[0] + "0")]
                chunk = chunk[1:]

            if len(chunk) == 1 and chunk != "0":
                result += " " + names[int(chunk)]

            return result.strip()

        res = ""
        num = str(num)
        i = len(num)
        scale = 0

        while i > 0:
            ch = num[max(0, i-3):i]
            part = helper(ch)
            if part:
                res = part + (" " + scales[scale] if scales[scale] else "") + " " + res
            i -= 3
            scale += 1

        return res.strip()
