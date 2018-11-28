process=[]
total_processes=input("Enter total number of processes: ")
for index in range(int(total_processes)):
       process.append([])
       process[index].append(input("Enter process name:"))
       process[index].append(int(input("Enter arrival time:")))
       process[index].append(int(input("Enter burst time:")))
process.sort(key=lambda process:process[2])
process.sort(key=lambda process:process[1])
sum=process[0][1]
for index in range(int(total_processes)):
      process[index].append(sum-process[index][1])
      sum+=process[index][2]
      process[index].append(sum-process[index][1])
AvgTurn=0
AvgWait=0
print("Process name    Burst Time    Arrival Time    Waiting time    Turn Around Time")
index=0
for index in range(int(total_processes)):
      print(process[index][0] ,'\t\t\t\t',process[index][1],'\t\t\t\t',process[index][2],'\t\t\t\t',process[index][3],'\t\t\t\t',process[index][4])
      AvgTurn+=process[index][3]
      AvgWait+=process[index][4]
AvgWait=AvgWait/(int)(total_processes)
AvgTurn=AvgTurn/(int)(total_processes)
print("average waiting time is ", AvgWait)
print("average turnaround time is ",AvgTurn)

