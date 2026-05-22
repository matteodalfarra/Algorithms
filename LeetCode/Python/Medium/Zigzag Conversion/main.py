class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = {}

        vertical = True
        i = 0
        p = 1
        while i < len(s):
            if p in rows:
                rows[p].append(s[i])
            else:                   
                rows[p] = [s[i]]

            if p < numRows and vertical:
                p += 1
                vertical = True
            else:
                p -= 1
                if p == 1:
                    vertical = True
                else:
                    vertical = False
            i += 1

        res = ""
        for v in rows.values():     
            res += "".join(v)

        return res
