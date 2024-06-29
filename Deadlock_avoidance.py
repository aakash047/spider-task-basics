class BankersAlgorithm:
    def __init__(self, processes, available, max_claim, allocation):
        self.processes = processes
        self.available = available
        self.max_claim = max_claim
        self.allocation = allocation
        self.need = [[max_claim[i][j] - allocation[i][j] for j in range(len(available))] for i in range(len(processes))]

    def calculate_work_and_finish(self):
        work = self.available.copy()
        finish = [False] * len(self.processes)
        return work, finish

    def find_safe_sequence(self, work, finish):
        safe_sequence = []
        while len(safe_sequence) < len(self.processes):
            found_process = False
            for i in range(len(self.processes)):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(len(work))):
                    for j in range(len(work)):
                        work[j] += self.allocation[i][j]
                    safe_sequence.append(self.processes[i])
                    finish[i] = True
                    found_process = True
                    break
            if not found_process:
                break
        return safe_sequence, finish

    def is_safe(self):
        work, finish = self.calculate_work_and_finish()
        safe_sequence, finish = self.find_safe_sequence(work, finish)

        if len(safe_sequence) == len(self.processes):
            print("The system is in a safe state.")
            print("Safe sequence:", safe_sequence)
            return True
        else:
            print("The system is not in a safe state. Deadlock is possible.")
            return False

# Example usage
processes = ['P0', 'P1', 'P2', 'P3', 'P4']
available = [3, 3, 2]  # Initial available resources
max_claim = [
    [7, 5, 3],  # Maximum resources needed by P0
    [3, 2, 2],  # Maximum resources needed by P1
    [9, 0, 2],  # Maximum resources needed by P2
    [2, 2, 2],  # Maximum resources needed by P3
    [4, 3, 3]   # Maximum resources needed by P4
]
allocation = [
    [0, 1, 0],  # Resources currently allocated to P0
    [2, 0, 0],  # Resources currently allocated to P1
    [3, 0, 2],  # Resources currently allocated to P2
    [2, 1, 1],  # Resources currently allocated to P3
    [0, 0, 2]   # Resources currently allocated to P4
]

bankers = BankersAlgorithm(processes, available, max_claim, allocation)
bankers.is_safe()
