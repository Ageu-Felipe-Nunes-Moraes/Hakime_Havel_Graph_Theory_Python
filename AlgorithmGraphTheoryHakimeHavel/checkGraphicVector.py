
#Hakime Havel

class HakimeHavel:
    
    def __init__(self):
        self.counter = 0 # Counter to help
        self.highest_value = 0 # Get the highest value of vector

    def rearrange_vector(self, vector): # Rearrange the list in decrescente order
        vector.sort(reverse=True)

    def show_vector(self, vector): # Print in the terminal
        print(vector)

    def subtract_positions(self, vector): # Will subtract 1 from each position
        for j in range(self.highest_value):
            vector[j] = vector[j] - 1 # Subtract 1 from each position

    def check_conditions(self, vector): # Checks whether it is a vector graphic or not
        for k in range(len(vector)):
            if vector[k] == 0: # Checks if all the other positions are equal to the zero as well
                self.counter += 1
                if self.counter == len(vector): # Checks the counting of zeros
                    print(f"É um vetor gráfico: [{vector}]")
                    break
            if vector[k] == -1: # Checks if there is any value in the from vector that is equal to "-1"
                print(f"Não é um vetor gráfico: [{vector}]")
                break

        
    # The function that checks if is a graphic vector using Hakime Havel's principles
    def graphic_vector(self, vector):
        self.rearrange_vector(vector)
        # Applying all necessary iterations to reach a satisfactory conclusion
        if len(vector) > vector[0]: # Checks if there is any vertices with a degree greater than the size of the vector
            self.show_vector(vector)
            for _ in range(len(vector)):
                self.highest_value = vector[0]
                del(vector[0]) # Deletes the first item from the vector
                self.subtract_positions(vector)
                self.show_vector(vector)
                self.rearrange_vector(vector)
                self.show_vector(vector)
                if vector[0] == 0: # Checks if the first position is "0"
                    self.check_conditions(vector)
                    break
        else:
            print("Tipo de lista inválida")

hakime = HakimeHavel()
hakime.graphic_vector([3,2,2,2,2]) # input list
    

#not graphic
#[6, 5, 4, 4, 4, 4, 4, 2]
#[4, 3, 3, 3, 3, 3, 2]
#[2, 2, 2, 2, 3, 2]
#[3, 2, 2, 2, 2, 2]
#[1, 1, 1, 2, 2]
#[2, 2, 1, 1, 1]
#[1, 0, 1, 1]
#[1, 1, 1, 0]
#[0, 1, 0]
#[1, 0, 0]
#[-1, 0]
#[0, -1]

# graphic
#[5, 4, 3, 3, 3, 3, 3, 2]
#[3, 2, 2, 2, 2, 3, 2]
#[3, 3, 2, 2, 2, 2, 2]
#[2, 1, 1, 2, 2, 2]
#[2, 2, 2, 2, 1, 1]
#[1, 1, 2, 1, 1]
#[2, 1, 1, 1, 1]
#[0, 0, 1, 1]
#[1, 1, 0, 0]
#[0, 0, 0]
#[0, 0, 0]

