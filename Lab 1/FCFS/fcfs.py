def findWaitingTime(processes, n, bt, wt):
	wt[0] = 0

	for i in range(1, n ):
		wt[i] = bt[i - 1] + wt[i - 1]

def findTurnAroundTime(processes, n, bt, wt, tat):
	for i in range(n):
		tat[i] = bt[i] + wt[i]

def findavgTime( processes, n, bt):

	wt = [0] * n
	tat = [0] * n
	total_wt = 0
	total_tat = 0

	findWaitingTime(processes, n, bt, wt)

	findTurnAroundTime(processes, n, bt, wt, tat)

	print( "Processes Burst time " +
				" Waiting time " +
				" Turn around time")

	for i in range(n):
	
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" " + processes[i] + "\t\t" +
					str(bt[i]) + "\t " +
					str(wt[i]) + "\t\t " +
					str(tat[i]))

	print( "Average waiting time = "+
				str(total_wt / n))
	print("Average turn around time = "+
					str(total_tat / n))


# Driver code
if __name__ =="__main__":
	
	n = int(input("Enter the numberf of process : "))
	
	processes = []
	for i in range(n):
		processId = input("Enter the process number {} : ".format(i+1))
		processes.append(processId)
	    
	print("Processes : ", processes)
	    
	burst_time = []
	for i in range(n):
		burstTime = int(input("Enter the burst time {} : ".format(i+1)))
		burst_time.append(burstTime)
	
	print("Burst Time : ", burst_time)

	findavgTime(processes, n, burst_time)











