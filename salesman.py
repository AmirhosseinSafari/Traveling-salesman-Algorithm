import pickle
def main():
    #------------------------------------------------
    # intialization arrays
    #------------------------------------------------
    main_matrix =  []
    previous_level_matrix = [] 
    reduced_matrix = []
    main_costs = {
    }
    vertex = {
    }
    seq = []

    for i in range(5):
        vertex[i+1] = False
        main_costs[i+1] = 0
    #------------------------------------------------
    # filling array by inputs
    #------------------------------------------------
    input_file = open("salesman.txt", "r")
    for line in input_file:
        elements = line.split()
        main_matrix.append(elements)

    main_matrix = [list( map(int,i) ) for i in main_matrix]     #initial all array elements to int 

    #------------------------------------------------
    # first reduce
    #------------------------------------------------

    cost = reducer(main_matrix)     #reduce
    main_costs[1] = cost            #append cost vertex 1
    seq.append(1)
    reduced_matrix = main_matrix    #save the reduced matrix
    previous_level_matrix = main_matrix
    vertex.update({1: True})
    
    with open("salesman_helper.txt","wb") as f:
        pickle.dump(previous_level_matrix,f)

    #helper.write(previous_level_matrix)
    #------------------------------------------------
    # other recations
    #------------------------------------------------
    vertex_counter = 1
    level_counter = 1
    last_varified_vertex = 1
    min_cost_level = -1
    min_cost_level_vertex = 0

    while level_counter < 5: 
        while vertex_counter <= 5:
            if vertex[vertex_counter] == False:
                
                main_matrix = []
                input_file = open("salesman.txt", "r")
                for line in input_file:
                    elements = line.split()
                    main_matrix.append(elements)
            
                main_matrix = [list( map(int,i) ) for i in main_matrix]
                reducer(main_matrix)

                #make_row_column_infint(reduced_matrix, last_varified_vertex-1, vertex_counter-1)
                i = last_varified_vertex-1
                for j in range(5):
                    reduced_matrix[i][j] = -1
            
                j = vertex_counter-1
                for i in range(5):
                    reduced_matrix[i][j] = -1
                
                reduced_matrix[vertex_counter-1][last_varified_vertex-1] = -1

                #print_matrix(reduced_matrix)
                cost = reducer(reduced_matrix)
                print(cost)
                cost += main_matrix[last_varified_vertex-1][vertex_counter-1]
                print(main_matrix[last_varified_vertex-1][vertex_counter-1])
                cost += main_costs[last_varified_vertex]
                print(main_costs[last_varified_vertex])
                #print_matrix(main_matrix)
                #print("-------------------------------------")

                if min_cost_level == -1:    #first time cost
                    min_cost_level = cost
                    min_cost_level_vertex = vertex_counter
                elif cost < min_cost_level:
                    min_cost_level = cost
                    min_cost_level_vertex = vertex_counter
                print_matrix(previous_level_matrix)
                print("//////////////////////////////////////////")
                
                with open("salesman_helper.txt","rb") as f:
                    previous_level_matrix = pickle.load(f)

                reduced_matrix = previous_level_matrix
            vertex_counter += 1

        make_row_column_infint(previous_level_matrix, last_varified_vertex-1, min_cost_level_vertex-1) #update previous level matrix

        with open("salesman_helper.txt","wb") as f:
            pickle.dump(previous_level_matrix,f)
            
        #end of update
        main_costs[min_cost_level_vertex] = min_cost_level  #save the cost of min vertex
        print("level_counter :" + str(level_counter))
        seq.append(min_cost_level_vertex)     #save min vertex
        vertex[min_cost_level_vertex] = True                
        last_varified_vertex = min_cost_level_vertex        #going to next min vertex
        vertex_counter = 1
        min_cost_level = -1
        level_counter += 1

    print_matrix(main_matrix)
    print("#####################################")
    print("Final sequence: ")
    print(seq)
    print("costs of vertexes: ")
    print(main_costs)
    print("total cost: " + str( sum(main_costs.values()) ))
    #print(main_costs)
    #print(vertex)

def make_row_column_infint(matrix, row, column):   
    i = row
    for j in range(5):
        matrix[i][j] = -1

    j = column
    for i in range(5):
        matrix[i][j] = -1
    
    matrix[column][row] = -1

def print_matrix(matrix):
    for i in range (5):
        print(matrix[i])

def reducer(matrix):
    min_row:int = -1
    cost = 0

    #------------------------
    #   recution in rows
    #------------------------
    for i in range(5):

        for j in range(5):
            if matrix[i][j] == -1:
                continue
            else:
                if min_row == -1:           #first not -1 number
                    min_row = matrix[i][j]
                elif matrix[i][j] < min_row:
                    min_row = matrix[i][j]  #find min
        
        #print(min_row)
        for j in range(5):
            if matrix[i][j] == -1:
                continue
            else:
                matrix[i][j] = matrix[i][j] - min_row
        
        if min_row != -1:
            cost += min_row

        min_row = -1

    #------------------------
    #   recution in columns
    #------------------------
    min_column:int = -1

    for j in range(5):
        
        for i in range(5):
            if matrix[i][j] == -1:
                continue
            else:
                if min_column == -1:           #first not -1 number
                    min_column = matrix[i][j]
                elif matrix[i][j] < min_column:
                    min_column = matrix[i][j]  #find min
        
        for i in range(5):
            if matrix[i][j] == -1:
                continue
            else:
                matrix[i][j] = matrix[i][j] - min_column
        
        if min_column != -1:
            cost += min_column
        min_column = -1

    return cost

if __name__ == "__main__":
    main()