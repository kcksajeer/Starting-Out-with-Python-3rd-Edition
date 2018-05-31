correct_list = ['A', 'C', 'A', 'A', 'D', 'B']
answers_list = ['A', 'C', 'B', 'A', 'X', 'B']
que_nums = []

que_no = 0
correct = 0
incorrect = 0

for i in range(6):
    if correct_list[i]==answers_list[i]:
        print("Correct")
        correct+=1
        
    else:
        print("Incorrect")
        incorrect+=1
        que_nums.append(correct_list.index(i))

print("No. of correct questions: ",correct)
print("No. of incorrect questions: ",incorrect)
print(que_nums)
