from typing import List, Tuple

def create_intervals(ii: List[Tuple[int,int]]):
    ii.sort() # O(nlogn)
    output_intervals = []
    for idx in range(1, len(ii)): # O(n)
        if ii[idx-1][1] < ii[idx][0]:
            output_intervals.append(ii[idx-1])
            continue
        ii[idx] = (ii[idx-1][0], max(ii[idx-1][1], ii[idx][1]))
    output_intervals.append(ii[-1])
    return output_intervals

def main():
    print("*"*50)
    input_tuples = [(1,3), (5,8), (4,10), (20,24)]
    output = create_intervals(input_tuples)
    print(output)
    
    print("*"*50)
    input_tuples = [(1,10), (2,3), (4,5), (6,7)]
    output = create_intervals(input_tuples)
    print(output)
    
    print("*"*50)
    input_tuples = [(1,3), (2,4), (3,5), (4,6)]
    output = create_intervals(input_tuples)
    print(output)
    
    print("*"*50)
    input_tuples = [(1,2), (2,3), (3,4), (4,5)]
    output = create_intervals(input_tuples)
    print(output)

if __name__ == "__main__":
    main()