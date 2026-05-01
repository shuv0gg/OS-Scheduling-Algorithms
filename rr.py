n = int(input("Enter number of processes: "))
tq = int(input("Enter Time Quantum: "))
pid = []
at = []
bt = []

for i in range(n):
    pid.append(input(f"Enter Process ID {i+1}: "))
    at.append(int(input(f"Enter Arrival Time of {pid[i]}: ")))
    bt.append(int(input(f"Enter Burst Time of {pid[i]}: ")))

remaining_bt = bt.copy()
ct = [0]*n
time = 0
queue = []
visited = [False]*n
gantt = []
gantt_time = [0]

while True:
    for i in range(n):
        if at[i] <= time and not visited[i]:
            queue.append(i)
            visited[i] = True

    if not queue:
        if all(r == 0 for r in remaining_bt):
            break
        gantt.append("IDLE")
        time += 1
        gantt_time.append(time)
        continue

    p = queue.pop(0)

    if remaining_bt[p] > tq:
        gantt.append(pid[p])
        time += tq
        remaining_bt[p] -= tq
        gantt_time.append(time)
    else:
        gantt.append(pid[p])
        time += remaining_bt[p]
        remaining_bt[p] = 0
        ct[p] = time
        gantt_time.append(time)

    for j in range(n):
        if at[j] <= time and not visited[j]:
            queue.append(j)
            visited[j] = True

    if remaining_bt[p] > 0:
        queue.append(p)

    if all(r == 0 for r in remaining_bt):
        break

tat = [0]*n
wt = [0]*n

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

print("\nGantt Chart:")
for g in gantt:
    print(f"{g} |", end="")

print("\n", end="")
for t in gantt_time:
    print(f"{t}\t", end="")