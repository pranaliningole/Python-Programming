import numpy as np

class DataAnalyzer:
    def Exit(Self):
        print("Exiting NumPy Data Analyzer. Goodbye!")
        
    def Search_Data(Self, Numbers):
        search_num = int(input("Which number would you like to search for? \n"))
        result = np.isin(Numbers, search_num)
        found = np.any(result)
        if found == True:
            print(search_num," is found.")
        else:
            print(search_num," is not found.")


    def Show_Dataset(Self):
        print("Data : ")
        for item in Self.Numbers:
            print(item)
        print("Number of values: ",Self.Numbers.size)

    def __init__(Self, Numbers):
        Self.Numbers = Numbers

    def Basic_Statistics(Self):
        print("========================================\n")
        print("             BASIC STATISTICS\n")
        print("========================================\n")

        sum = np.sum(Self.Numbers)
        mean = np.mean(Self.Numbers)
        mini = np.min(Self.Numbers)
        maxi = np.max(Self.Numbers)

        print("Sum : ",sum)
        print("Mean : ",mean)
        print("Minimum : ",mini)
        print("Maximum : ",maxi)
        print("Range : ",maxi-mini)

    def Advanced_Statistics(Self):
        print("========================================\n")
        print("             ADVANCED STATISTICS\n")
        print("========================================\n")

        median = np.median(Self.Numbers)
        Standard_Deviation = np.std(Self.Numbers)
        Variance = np.var(Self.Numbers)
        Percentile_25 = np.percentile(Self.Numbers, 25)
        Percentile_50 = np.percentile(Self.Numbers, 50)
        Percentile_75 = np.percentile(Self.Numbers, 75)

        print("Median : ",median)
        print("Standard Deviation : ",Standard_Deviation)
        print("Variance : ",Variance)
        print("25th Percentile : ",Percentile_25)
        print("50th Percentile : ",Percentile_50)
        print("75th Percentile : ",Percentile_75)
        


def main():

    print("========================================\n")
    print("        NUMPY DATA ANALYZER\n")
    print("========================================\n")
    num = input("Enter your numbers separated by spaces: \n")
    Numbers = num.split()
    Numbers = [int(item) for item in Numbers]
    Numbers = np.array(Numbers)
    data = DataAnalyzer(Numbers)
        
    print()

    while True:
        print("========================================\n")
        print("             MAIN MENU\n")
        print("========================================\n")

        print("1. Show Dataset")
        print("2. Basic Statistics")
        print("3. Advanced Statistics")
        print("4. Search Data")
        print("5. Exit\n")

        choice = int(input("Enter your choice : \n"))

        if choice == 1:
            data.Show_Dataset()

        elif choice == 2:
            data.Basic_Statistics()

        elif choice == 3:
            data.Advanced_Statistics()

        elif choice == 4:
            data.Search_Data(Numbers)

        elif choice == 5:
            data.Exit()
            break 

        else:
            print("Invalid Choice.")
            

main()