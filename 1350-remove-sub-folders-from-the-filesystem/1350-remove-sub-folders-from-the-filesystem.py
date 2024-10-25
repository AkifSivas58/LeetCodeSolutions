class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        last_added = folder[0]
        res = [last_added]
        for i in range(1, len(folder)):
            if folder[i].startswith(last_added + "/"):
                continue
            else:
                res.append(folder[i])
                last_added = folder[i]
        
        return res

        