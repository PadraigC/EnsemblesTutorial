from statistics import mode

def plain_dis(l1, l2):
    m = len(l1)
    count = 0
    for i, j in zip(l1,l2):
        if i != j:
            count += 1
    return count/m

# This function takes a data frame as input and returns a list of predictions 
# that represents the majority vote of the predictions in the columns list.
def get_consensus_prediction (data_frame, columns):
    res_data_frame = data_frame[columns]
    consensus = []
    for row in res_data_frame.iterrows():
        consensus.append(mode(row[1]))
    return consensus