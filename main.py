class Data:
    def __init__(self):
        self.student_list8 = [] #listfor8
        self.student_list9 = [] #listfor9
        self.student_list10 = [] #listfor10
        self.avgMarks = 0
        self.totalDays = 0
        self.totalEarning = 0

    def add_std (self):
        print("1 for class 8")
        print("2 for class 9")
        print("3 for class 10")
        cls = input()
        if cls == '1':
            while True:
                print('Press 1 if you  want to add student.')
                print('Or press any key for exit from add student')
                a = int(input('press number: '))
                if a == 1:
                    d1 = {}
                    d1['name'] = input('student name: ')
                    d1['math'] = int(input('Press 1 if yes or 0 for no:'))
                    d1['english'] = int(input('Press 1 if yes or 0 for no:'))
                    d1['bangla'] = int(input('Press 1 if yes or 0 for no:'))
                    d1['ID'] = int(input('Student ID:'))
                    d1['avgMarks'] = int(input('avg marks: '))
                    d1['totalDays'] = int(input('Total Days taught: '))
                    d1['totalEarnings'] = int(input('Total Earnings: '))
                    self.student_list8.append(d1)
                    print('Successfully add student')
                    self.totalDays = self.totalDays + self.student_list8['totalDays']
                    self.avgMarks = self.avgMarks +self.student_list8['avgMarks']
                    self.totalEarning = self.totalEarning +self.student_list8['totalEarnings']
                    print('--------*--------------*---------')
                else:
                    self.main_menu()
                    break
        elif cls == '2':
            while True:
                print('Press 1 if you  want to add student.')
                print('Or press any key for exit from add student')
                a = int(input('press number: '))
                if a == 1:
                    d2 = {}
                    d2['name'] = input('student name: ')
                    d2['math'] = int(input('Press 1 if yes or 0 for no:'))
                    d2['english'] = int(input('Press 1 if yes or 0 for no:'))
                    d2['bangla'] = int(input('Press 1 if yes or 0 for no:'))
                    d2['ID'] = int(input('Student ID:'))
                    d2['avgMarks'] = int(input('avg marks: '))
                    d2['totalDays'] = int(input('Total Days taught: '))
                    d2['totalEarnings'] = int(input('Total Earnings: '))
                    self.student_list9.append(d2)
                    print('Successfully add student')
                    self.totalDays = self.totalDays + self.student_list9['totalDays']
                    self.avgMarks = self.avgMarks + self.student_list9['avgMarks']
                    self.totalEarning = self.totalEarning + self.student_list9['totalEarnings']
                    print('--------*--------------*---------')
                else:
                    self.main_menu()
                    break
        elif cls =='3':
            while True:
                print('Press 1 if you  want to add student.')
                print('Or press any key for exit from add student')
                a = int(input('press number: '))
                if a == 1:
                    d3 = {}
                    d3['name'] = input('student name: ')
                    d3['math'] = int(input('Press 1 if yes or 0 for no:'))
                    d3['english'] = int(input('Press 1 if yes or 0 for no:'))
                    d3['bangla'] = int(input('Press 1 if yes or 0 for no:'))
                    d3['ID'] = int(input('Student ID:'))
                    d3['avgMarks'] = int(input('avg marks: '))
                    d3['totalDays'] = int(input('Total Days taught: '))
                    d3['totalEarnings'] = int(input('Total Earnings: '))
                    self.student_list10.append(d3)
                    print('Successfully add student')
                    self.totalDays = self.totalDays + self.student_list10['totalDays']
                    self.avgMarks = self.avgMarks + self.student_list10['avgMarks']
                    self.totalEarning = self.totalEarning + self.student_list10['totalEarnings']
                    print('--------*--------------*---------')
                else:
                    self.main_menu()
                    break


    def edit_std (self):
        while True:
            marks = 0
            count=0
            print('Press 1 for edit student or Press anything:')
            a = int(input('press number: '))
            if a == 1:
                print("1 for class 8")
                print("2 for class 9")
                print("3 for class 10")
                cls =int(input('Enter class:'))
                if cls == 1:
                    b = int(input('Enter the student id that you want to edit in class 8: '))
                    t = int(input('Enter the total days:'))
                    for i in range(len(self.student_list8)):
                        if b == self.student_list8[i]:
                            self.student_list8[i]['totalDays']= self.student_list8[i]['totalDays']+t
                        if self.student_list8[i]['math'] == 1:
                            m = int(input('Enter the math marks:'))
                            marks=marks+m
                            count = count+1
                        if self.student_list8[i]['english'] == 1 :
                            m = int (input('Enter the english marks:'))
                            marks = marks + m
                            count = count + 1
                        if self.student_list8[i]['bangla'] == 1:
                            m = int(input('Enter the bangla marks:'))
                            marks = marks + m
                            count = count + 1

                    e = t*count*1
                    AVG = marks/count
                    self.student_list8[i]['totalEarnings']= self.student_list8[i]['totalEarnings']+e
                    totalEarning = totalEarning + self.student_list8[i]['totalEarnings']
                    self.student_list8[i]['avgMarks'] = self.student_list8[i]['avgMarks'] + AVG
                    avgMarks = avgMarks + self.student_list8[i]['avgMarks']
                elif cls == 2:
                    b = int(input('Enter the student id that you want to edit in class 9: '))
                    t = int(input('Enter the total days:'))
                    for i in range(len(self.student_list8)):
                        if b == self.student_list9[i]:
                            self.student_list9[i]['totalDays']= self.student_list9[i]['totalDays']+t
                        if self.student_list9[i]['math'] == 1:
                            m = int(input('Enter the math marks:'))
                            marks=marks+m
                            count = count+1
                        if self.student_list9[i]['english'] == 1 :
                            m = int (input('Enter the english marks:'))
                            marks = marks + m
                            count = count + 1
                        if self.student_list9[i]['bangla'] == 1:
                            m = int(input('Enter the bangla marks:'))
                            marks = marks + m
                            count = count + 1

                    e = t*count*1
                    AVG = marks/count
                    self.student_list9[i]['totalEarnings']= self.student_list9[i]['totalEarnings']+e
                    totalEarning = totalEarning + self.student_list9[i]['totalEarnings']
                    self.student_list8[i]['avgMarks'] = self.student_list9[i]['avgMarks'] + AVG
                    avgMarks = avgMarks + self.student_list9[i]['avgMarks']
                elif cls == 3:
                    b = int(input('Enter the student id that you want to edit in class 10: '))
                    t = int(input('Enter the total days:'))
                    for i in range(len(self.student_list10)):
                        if b == self.student_list10[i]:
                            self.student_list10[i]['totalDays']= self.student_list8[i]['totalDays']+t
                        if self.student_list10[i]['math'] == 1:
                            m = int(input('Enter the math marks:'))
                            marks=marks+m
                            count = count+1
                        if self.student_list10[i]['english'] == 1 :
                            m = int (input('Enter the english marks:'))
                            marks = marks + m
                            count = count + 1
                        if self.student_list10[i]['bangla'] == 1:
                            m = int(input('Enter the bangla marks:'))
                            marks = marks + m
                            count = count + 1

                    e = t*count*1
                    AVG = marks/count
                    self.student_list10[i]['totalEarnings']= self.student_list10[i]['totalEarnings']+e
                    totalEarning = totalEarning + self.student_list10[i]['totalEarnings']
                    self.student_list10[i]['avgMarks'] = self.student_list8[i]['avgMarks'] + AVG
                    avgMarks = avgMarks + self.student_list10[i]['avgMarks']
            else:
                self.main_menu()
                break
    def delete_std (self):
        while True:
            print('Press 1 if you  went to delete product.')
            print('Or press any key for exit from delete product')
            a = int(input('Press number: '))
            if a == 1:
                print("1 for class 8")
                print("2 for class 9")
                print("3 for class 10")
                cls =int(input('Enter class:'))
                if cls == 1:
                    b = int(input('Enter student id: '))
                    for i in range(len(self.student_list8)):
                        if self.student_list8[i]['ID'] == b:
                            del self.student_list8[i]
                            print('Successfully deleted student from list')
                            print('------*----------------*-----------')
                        else:
                            print('Not in student list')
                            print('-------*-----------------*-----------')
                elif cls == 2:
                    b = int(input('Enter student id: '))
                    for i in range(len(self.student_list8)):
                        if self.student_list9[i]['ID'] == b:
                            del self.student_list8[i]
                            print('Successfully deleted student from list')
                            print('------*----------------*-----------')
                        else:
                            print('Not in student list')
                            print('-------*-----------------*-----------')
                elif cls == 3:
                    b = int(input('Enter student id: '))
                    for i in range(len(self.student_list8)):
                        if self.student_list10[i]['ID'] == b:
                            del self.student_list8[i]
                            print('Successfully deleted student from list')
                            print('------*----------------*-----------')
                        else:
                            print('Not in student list')
                            print('-------*-----------------*-----------')
            else:
                self.main_menu()
                break

    def list_std (self):
        print("1 for class 8")
        print("2 for class 9")
        print("3 for class 10")
        cls = int(input('Enter class:'))
        if cls == 1:
            print("Name" + " " + "Total Earnings" + " " + "Average Marks" )
            for i in range(len(self.student_list8)):
                print(self.student_list8[i]['name'] + "   " + str(self.student_list8[i]['totalEarnings']) + "   " + str(
                    self.student_list8[i]['avgMarks']))
                print('\n')
            print('-----*---------------*-----------')
        elif cls == 2:
            print("Name" + " " + "Total Earnings" + " " + "Average Marks")
            for i in range(len(self.student_list9)):
                print(self.student_list8[i]['name'] + "   " + str(
                    self.student_list8[i]['totalEarnings']) + "   " + str(
                    self.student_list8[i]['avgMarks']))
                print('\n')
            print('-----*---------------*-----------')
        elif cls == 3:
            print("Name" + " " + "Total Earnings" + " " + "Average Marks")
            for i in range(len(self.student_list10)):
                print(self.student_list8[i]['name'] + "   " + str(
                    self.student_list8[i]['totalEarnings']) + "   " + str(
                    self.student_list8[i]['avgMarks']))
                print('\n')
            print('-----*---------------*-----------')
            self.main_menu()




    def overall_info (self):
        print(totalDays)
        print(avgMarks)
        print(totalEarning)

    def main_menu (self):
        print('1.Add Student')
        print('2.Edit Student')
        print('3.Delete Student')
        print('4.See list of student')
        print('5.See overall information')
        print('-----------------------------------------------')
        print('Enter the number what you want to do:')
s = Data()
s.main_menu()

while True:
    num = input()
    if num == '1':
        s.add_std()
    elif num == '2':
        s.edit_std()
    elif num == '3':
        s.delete_std()
    elif num == '4':
        s.list_std()
    elif num == '5':
        s.overall_info()
    else:
        s.main_menu()



