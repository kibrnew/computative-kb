class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        # Create a set for faster membership checking.
        bank_set = set(bank)

        # Define possible mutations from one character to another.
        mutations = {'A', 'C', 'G', 'T'}

        # Initialize the queue for BFS with the starting gene and a step count of 0.
        queue = deque([(startGene, 0)])

        while queue:
            current_gene, steps = queue.popleft()

            # If we reach the end gene, return the number of steps.
            if current_gene == endGene:
                return steps

            # Generate all possible next genes with one mutation.
            for i in range(8):  # 8-character long gene
                for mutation in mutations:
                    next_gene = current_gene[:i] + mutation + current_gene[i+1:]
                    
                    # Check if the next gene is in the bank and hasn't been visited.
                    if next_gene in bank_set:
                        bank_set.remove(next_gene)  # Mark as visited to avoid revisiting.
                        queue.append((next_gene, steps + 1))

        # If we can't reach the end gene, return -1.
        return -1
