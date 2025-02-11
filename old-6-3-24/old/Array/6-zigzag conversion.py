class Solution:
    def make_template(self, numRows: int) -> list:
        front_of_template = list(range(numRows))
        back_of_template = list(range(numRows - 2, 0, -1))
        return front_of_template + back_of_template

    def convert(self, s: str, numRows: int) -> str:
        template = self.make_template(numRows)
        template_length = len(template)
        result = [''] * numRows
        for idx, char in enumerate(s):
            template_num = template[idx % template_length]
            result[template_num] += char
        return ''.join(result)

s = "PAYPALISHIRING"
numRows = 3
print(Solution().convert(s, numRows))
