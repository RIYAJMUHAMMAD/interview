class BubbleSort:

    def __init__(self, input_data):
        self.data = input_data

    def sort(self):
        for j in range(0, len(self.data)):
            sorted= True
            for i in range(0, len(self.data)-1-j):
                if self.data[i+1] < self.data[i]:
                    self.data[i],self.data[i+1] = self.data[i+1],self.data[i]
                    sorted= False
            if sorted:
                return self.data
            

if __name__=="__main__":
    l=[5,7,9,3,2,1]
    print(BubbleSort(l).sort())