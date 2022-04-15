import csv


def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])

        writer.writerow(info_list)


if __name__ == '__main__':
    flag = True
    stud_num = 1
    while(flag):
        stud_info = input(
            'Enter information for student #{} in the following format: (Name Age Contact_Number Email_ID):'.format(stud_num))

        # split
        stud_info_list = stud_info.split(' ')
        print("\nThe entered information is -\nName: {}\nAge: {}\nContact Number: {}\nEmail ID: {}".format(
            stud_info_list[0], stud_info_list[1], stud_info_list[2], stud_info_list[3]))
        choice_check = input('Is the entered information correct? (y/n): ')
        if choice_check == 'y':
            write_into_csv(stud_info_list)
            flag_check = input(
                'Enter (y/n) if you want to enter another student information')
            if flag_check == 'y':
                flag = True
                stud_num += 1
            elif flag_check == 'n':
                flag = False
        elif choice_check == 'n':
            print("\nPlease re-enter the values:")


        
        
