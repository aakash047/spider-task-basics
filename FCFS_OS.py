# FCFS/FIFO
# Process : [arrival_time, burst_time, pid]
def FCFS(process_list):
    t = 0
    gantt = []
    completed = {}
    
    # Sort process list based on arrival time
    process_list.sort(key=lambda x: x[0])
    
    while process_list:
        if process_list[0][0] > t:
            t += 1
            gantt.append("Idle")
        else:
            process = process_list.pop(0)
            arrival_time = process[0]
            burst_time = process[1]
            pid = process[2]
            
            # Process starts execution
            gantt.extend([pid] * burst_time)
            t += burst_time
            
            # Calculate times
            completion_time = t
            time_turnaround = completion_time - arrival_time
            waiting_time = time_turnaround - burst_time
            completed[pid] = [completion_time, time_turnaround, waiting_time]
    
    avg_waiting_time = sum(comp[2] for comp in completed.values()) / len(completed)
    avg_turnaround_time = sum(comp[1] for comp in completed.values()) / len(completed)
    
    print("Gantt Chart:", gantt)
    print("Completed Processes:", completed)
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Sample process list for test
sample_list = [[2, 6, "P1"], [1, 3, "P2"], [0, 4, "P3"], [4, 2, "P4"], [5, 3, "P5"]]
FCFS(sample_list)

