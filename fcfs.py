n = int(input("Enter number of processes: "))
pid = []
at = []
bt = []

for i in range(n):
    pid.append(input(f"Enter Process ID {i+1}: "))
    at.append(int(input(f"Enter Arrival Time of {pid[i]}: ")))
    bt.append(int(input(f"Enter Burst Time of {pid[i]}: ")))

for i in range(n):
    for j in range(i+1, n):
        if at[i] > at[j]:
            at[i], at[j] = at[j], at[i]
            bt[i], bt[j] = bt[j], bt[i]
            pid[i], pid[j] = pid[j], pid[i]

ct = [0] * n
tat = [0] * n
wt = [0] * n
time = 0
gantt = []
gantt_time = [0]

for i in range(n):
    # If CPU is idle
    if time < at[i]:
        gantt.append("IDLE")
        time = at[i]
        gantt_time.append(time)

    gantt.append(pid[i])
    time += bt[i]
    ct[i] = time
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