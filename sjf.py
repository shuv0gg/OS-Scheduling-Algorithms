n = int(input("Enter number of processes: "))
pid = []
at = []
bt = []

for i in range(n):
    pid.append(input(f"Enter Process ID {i+1}: "))
    at.append(int(input(f"Enter Arrival Time of {pid[i]}: ")))
    bt.append(int(input(f"Enter Burst Time of {pid[i]}: ")))

completed = [False] * n
ct = [0] * n
tat = [0] * n
wt = [0] * n

time = 0
done = 0
gantt = []
gantt_time = [0]

while done < n:
    idx = -1
    min_bt = 9999

    for i in range(n):
        if at[i] <= time and not completed[i]:
            if bt[i] < min_bt:
                min_bt = bt[i]
                idx = i

    if idx == -1:
        gantt.append("IDLE")
        time += 1
        gantt_time.append(time)
    else:
        gantt.append(pid[idx])
        time += bt[idx]
        ct[idx] = time
        completed[idx] = True
        done += 1
        gantt_time.append(time)

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

print("\nGantt Chart:")
print("|", end="")
for g in gantt:
    print(f" {g} |", end="")

print("\n", end="")
for t in gantt_time:
    print(f"{t}\t", end="")