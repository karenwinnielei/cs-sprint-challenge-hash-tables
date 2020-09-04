def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    for i in range(length):
        cache[weights[i]] = i

    for i in range(length):
        weight_limit = limit - weights[i]
        if weight_limit in cache:
            return (max(i, cache[weight_limit]), min(i, cache[weight_limit]))

    return None


weights = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights, 5, 21))

   
