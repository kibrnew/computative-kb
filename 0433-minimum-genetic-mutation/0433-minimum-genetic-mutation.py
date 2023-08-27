class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        bank= set(bank)
        mutations = {'A', 'C', 'G', 'T'}
        queue = deque([(startGene, 0)])

        while queue:
            current, steps = queue.popleft()
            if current == endGene:
                return steps
            for i in range(8):
                for base in mutations:
                    nextg = current[:i] + base + current[i+1:]
                    if nextg in bank:
                        bank.remove(nextg)  
                        queue.append((nextg, steps + 1))

        return -1
