from typing import List, Set

if __name__ == "__main__":
    list_ = {0: [1, 2],
             1: [0, 5],
             2: [0],
             3: [6],
             4: [],
             5: [1],
             6: [3]} 
    
    groups: List[Set] = []
    for person in list_:
        person_found = False
        for group in groups:
            if person in group:
                person_found = True
                for other_person in list_[person]:
                    group.add(other_person)
                break
        if not person_found:
            groups.append(set([person]))
            for other_person in list_[person]:
                groups[-1].add(other_person)
    print(len(groups))
    print(groups)
        
        