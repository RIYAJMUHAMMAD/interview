class InsertionSort:
    def __init__(self, data):
        self.input_data = data
    
    def sort(self):
        if len(self.input_data)<2:
            return self.input_data
        try:
            for pointer_index in range(len(self.input_data)-1):
                if self.input_data[pointer_index]>self.input_data[pointer_index+1]:
                    self.input_data[pointer_index+1], self.input_data[pointer_index] = self.input_data[pointer_index],self.input_data[pointer_index+1]
                if pointer_index>1 and self.input_data[pointer_index]<self.input_data[pointer_index-1]:
                    self.sort_sorted_part(pointer_index)
            return self.input_data
        except TypeError:
            print(f"Wrong data types. enter numeric")

        
    def sort_sorted_part(self,pointer_index):
        for reverse_pointer_index in range(pointer_index,0,-1):
            if self.input_data[reverse_pointer_index]<=self.input_data[reverse_pointer_index-1]:
                self.input_data[reverse_pointer_index], self.input_data[reverse_pointer_index-1] = self.input_data[reverse_pointer_index-1], self.input_data[reverse_pointer_index]
            else:
                break
    


if __name__ == "__main__":
    l=[5,7,9,3,2,1,2]
    z= ["o",1]
    print(InsertionSort(l).sort())
            
