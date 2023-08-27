class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        bank_set = set(bank)
        mutations = {'A', 'C', 'G', 'T'}
        queue = deque([(startGene, 0)])

        while queue:
            current_gene, steps = queue.popleft()
            if current_gene == endGene:
                return steps
            for i in range(8):
                for mutation in mutations:
                    next_gene = current_gene[:i] + mutation + current_gene[i+1:]
                    if next_gene in bank_set:
                        bank_set.remove(next_gene)  
                        queue.append((next_gene, steps + 1))

        return -1
