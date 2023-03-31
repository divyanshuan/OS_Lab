def findWaitingTime(processes, n, bt, wt, at):
    service_time = [0] * n
    service_time[0] = 0
    wt[0] = 0
    for i in range(1, n):

        # Add burst time of previous processes
        service_time[i] = (service_time[i - 1] +bt[i - 1])

        # Find waiting time for current
        # process = sum - at[i]
        wt[i] = service_time[i] - at[i]

        # If waiting time for a process is in
        # negative that means it is already
        # in the ready queue before CPU becomes
        # idle so its waiting time is 0
        if (wt[i] < 0):
            wt[i] = 0

# Function to calculate turn around time


def findTurnAroundTime(processes, n, bt, wt, tat):

    # Calculating turnaround time by
    # adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]


# Function to calculate average waiting
# and turn-around times.
def findavgTime(processes, n, bt, at):
    wt = [0] * n
    tat = [0] * n

    # Function to find waiting time
    # of all processes
    findWaitingTime(processes, n, bt, wt, at)

    # Function to find turn around time for
    # all processes
    findTurnAroundTime(processes, n, bt, wt, tat)

    # Display processes along with all details
    print("Processes\t" + "Burst Time\t"+
           "Arrival Time\t"	+" Waiting Time\t"+" Turn-Around Time \t"+
             "Completion Time"+ "\n")
    total_wt = 0
    total_tat = 0
    for i in range(n):

        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time = tat[i] + at[i]
        print(" ", processes[i], "\t\t", bt[i], "\t\t", at[i],
              "\t\t", wt[i], "\t\t ", tat[i], "\t\t\t ", compl_time)

    print("Average waiting time = %.5f " % (total_wt / n))
    print("\nAverage turn around time = ", total_tat / n)


# Driver code
if __name__ == "__main__":

    n = int(input("Enter the number of processes : "))

    processes = []
    for i in range(n):
        processId = input("Enter the process number {} : ".format(i+1))
        processes.append(processId)

    print("Processes : ", processes)

    burst_time = []
    for i in range(n):
        burstTime = int(input("Enter the burst time for process {} : ".format(i+1)))
        burst_time.append(burstTime)

    print("Burst Time : ", burst_time)

    arrival_time = []
    for i in range(n):
        arrivalTime = int(
            input("Enter the Arrival time for process {} : ".format(i+1)))
        arrival_time.append(arrivalTime)

    print("Arrival time : ", arrival_time)

    findavgTime(processes, n, burst_time, arrival_time)
