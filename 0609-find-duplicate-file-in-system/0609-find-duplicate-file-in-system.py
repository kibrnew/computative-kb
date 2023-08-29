from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        topaths = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]
            for finfo in parts[1:]:
                fparts = finfo.split('(')
                fname = fparts[0]
                content = fparts[1][:-1]
                fullpath = f"{directory}/{fname}"
                topaths[content].append(fullpath)

        groups = [group for group in topaths.values() if len(group) > 1]

        return groups
