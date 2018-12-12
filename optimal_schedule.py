#Figure out which nodes are overlapping

subjects = {'Art':(9,10),
            'Eng':(9.5,10.5),
            'Math':(10,11),
            'CS':(10.5,11.5),
            'Music':(11,12)}
temp_subjects = dict(subjects)
no_overlap = {}

def new_dict_entry(subject,sub):
    if subject not in no_overlap:
        no_overlap[subject] = {}
    if sub not in no_overlap[subject]:
        no_overlap[subject][sub] = []

        
for subject in subjects:
    temp_subjects.pop(subject)
    start,end = subjects[subject]
    
    for sub in temp_subjects:
        istart,iend = subjects[sub]
        latest_start = max(start,istart)
        earliest_end = min(end, iend)
        dt = (earliest_end - latest_start)

        if dt <= 0:
            new_dict_entry(subject, sub)
            no_overlap[subject][sub].append(dt)

graph = dict(no_overlap)
toVisit = list(subjects.keys())
path = []
individual_path = {}
stack = [toVisit.pop(0)]


while len(toVisit)!= 0:
    try:
        while True:
            node = stack.pop(0)
            path.append(node)
            stack.append(list(graph[node].keys())[0])
    except:
        individual_path[path[0]] = list(path)
        del path[:]
        stack.append(toVisit.pop(0))
 
print(individual_path)
