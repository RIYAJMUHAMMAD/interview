class SelectionSort:

    def __init__(self, input_data):
        self.list= input_data

    def sort(self):
        for i in range(0,len(self.list)-1):
            j = self.find_lowest_index(i)
            self.swap_value(i, j)
        return self.list
            

    def find_lowest_index(self, lowest):
        for j in range(lowest, len(self.list)):
            if self.list[j]<self.list[lowest]:
                lowest=j
        print(lowest)
        return lowest
            
    def swap_value(self, i, j):
        if i==j:
            pass
        else:
            (self.list[i], self.list[j]) = (self.list[j], self.list[i])

if __name__== "__main__":
    l=[5,2,4, 10 ,3,1,2]
    print(SelectionSort(l).sort())
    
