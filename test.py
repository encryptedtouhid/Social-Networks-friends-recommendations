filepath = 'net1.txt'
result = []
rev_result = []
with open(filepath) as fp:
  line = fp.readline()
  #print(line)
  split_val = []
  pre_val = -1
  curr_val = -1
  single_result = []
  while line:
    split_val = line.split()
    #print(split_val)
    curr_val = int(split_val[0])
    if pre_val != -1 and curr_val != pre_val:
      #print(single_result)
      result.append([pre_val,single_result])
      single_result = []
      # ================== SEARCH IN REVERSE ==============
      for i in range(len(rev_result)):
        if curr_val == rev_result[i][0]:
          single_result = rev_result[i][1]
          del rev_result[i]
          break
      # ================== SEARCH IN REVERSE ==============
    single_result.append(split_val[1])
    # ================== ADD IN REVERSE ==============
    if len(rev_result) == 0:
      rev_result.append([ int(split_val[1]),[split_val[0]] ])
    else:
      tmp = int(split_val[1])
      #rev_result[0][1].append(1)
      for i in range(len(rev_result)):
        if tmp==rev_result[i][0]:
          rev_result[i][1].append(split_val[0])
          tmp = -1
          break
        elif tmp < rev_result[i][0]:
          rev_result.insert(i, [tmp,[split_val[0]]])
          tmp = -1
          break
      if tmp != -1:
        rev_result.append([tmp,[split_val[0]]])
        tmp = -1
    # ================== ADD IN REVERSE ==============
    #print(split_val[0])
    pre_val = curr_val
    line = fp.readline()
if len(single_result) !=0 :
  result.append([pre_val,single_result])
for entry in rev_result:
  result.append(entry)
print(result)
