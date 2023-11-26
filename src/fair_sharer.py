def fair_sharer(values, num_iterations, share=0.1):

    for i in range(num_iterations):

        max_value = max(values)
        max_index = values.index(max_value)

        share_value = max_value * share
        values[max_index-1] = values[max_index-1] + share_value
        values[max_index+1] = values[max_index+1] + share_value
        values[max_index] = max_value - (2 * share_value)
      
    #print(values)
    return values
    




#fair_sharer([0, 1000, 800, 0], 1) # --> [100, 800, 900, 0]
#fair_sharer([0, 1000, 800, 0], 2) # --> [100, 890, 720, 90]
