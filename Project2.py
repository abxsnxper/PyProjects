def main(file_name):
    OP1=profession_records(file_name)
    OP2=dictionary_item(file_name)
    OP3=cosine_similarity(file_name)
    OP4=cohens_d_test(file_name)
    return OP1,OP2,OP3,OP4



def read_file(file_name):
    '''Read the file from the csv file

    Args;
    file_name: Name of the csv file

    Returns:
    dict1(dict): a dictionary containing the data read from the file using string functions
    '''
    dict1 = {}
    with open(file_name, "r") as file:
        lines = file.readlines()
    for line in lines[1:]:
        data = line.strip('\n').split(',')
        dict1[data[0]] = [int(data[1]), data[2], float(data[3]), float(data[4]), data[5].lower(), data[6], data[7], data[8],
                          data[9], float(data[10]),data[11]]

    return dict1

def profession_records(file_name):
    '''
    FuncTion to return OP1

    Args:file_name

    Returns:List of records for student and everyone else

    '''
    dict2=read_file(file_name)
    student={}
    non_student={}
    for key,value in dict2.items():
        if value[8]=='student' or value[8]=='Student' or value[8]=='STUDENT':
            student[key.lower()]=[value[0],value[2],value[3]]
        else:
            non_student[key.lower()]=[value[0],value[2],value[3]]
    return [student, non_student]



def dictionary_item(file_name):
    '''
    Function to return OP2

    Args:file_name

    Returns:A dictionary where key is a platform and value is a list containing total, average and standard deviationof engagement time of users.

    '''
    dict3=read_file(file_name)
    platform=[]
    item={}
    total={}
    avg={}
    time={}
    std_dev={}
    leng={}
    variance={}
    for key,value in dict3.items():
        if value[4] not in platform:
            platform.append(value[4])
    for a,b in dict3.items():
        for i in platform:
            if i==b[4]:
                if i not in total.keys():
                    total[i]=round((b[2]*b[3])/100,4)
                    time[i]=[(b[2]*b[3])/100]
                    leng[i]=1
                else:
                    total[i]+=round((b[2]*b[3])/100,4)
                    time[i].append((b[2]*b[3])/100)
                    leng[i]+=1
    for i in total.keys():
        avg[i]=round(total[i]/leng[i],4)

    for j in avg.keys():
        variance[j]=sum((x-avg[j])**2 for x in time[j])/(leng[j]-1)
        std_dev[j]=round(variance[j]**0.5,4)

    for i in total.keys():
        item[i]=[total[i],avg[i],std_dev[i]]

    return item

def cosine_similarity(file_name):
    '''
    Function to return OP3

    Args:file_name

    Returns:list of cosine similarity values between age and income for students and everyone else

    '''
    dict4=read_file(file_name)
    students_age=[]
    student_income=[]
    non_students_age=[]
    non_students_income=[]
    stu_numer=0
    stu_mag_a=0
    stu_mag_b=0
    non_mag_f=0
    non_mag_e=0
    non_numer=0
    for key,value in dict4.items():
        if value[8]=='student' or value[8]=='Student' or value[8]=='STUDENT':
            students_age.append(value[0])
            student_income.append(value[9])
        else:
            non_students_age.append(value[0])
            non_students_income.append(value[9])

    for i in range(len(students_age)):
        stu_numer+=students_age[i]*student_income[i]
        stu_mag_a+=students_age[i]**2
        stu_mag_b+=student_income[i]**2

    if stu_mag_b!=0 and stu_mag_a!=0:
        cosine_sim_student=round(stu_numer/((stu_mag_a**0.5)*(stu_mag_b**0.5)),4)
    else:
        cosine_sim_student=0

    for j in range(len(non_students_age)):
        non_numer+=non_students_age[j]*non_students_income[j]
        non_mag_e+=non_students_age[j]**2
        non_mag_f+=non_students_income[j]**2

    if non_mag_f!=0 and non_mag_e!=0:
        sim_non_student = round(non_numer / ((non_mag_e**0.5) * (non_mag_f**0.5)), 4)
    else:
        sim_non_student=0

    return [cosine_sim_student,sim_non_student]

def cohens_d_test(file_name):
    '''
    Function to reTurn OP4

    Args:file_name

    Returns:Cohens's d test value for engagement time for students and everyone else

    '''
    dict4=read_file(file_name)
    student_engagement=[]
    non_student_engagement=[]
    variance_x=0
    variance_y=0
    for key, value in dict4.items():
        time=(value[2]*value[3])/100
        if value[8]=='student' or value[8]=='Student' or value[8]=='STUDENT':
            student_engagement.append(time)
        else:
            non_student_engagement.append(time)
    if len(student_engagement)>0 and len(non_student_engagement)>0:
        student_mean=sum(student_engagement)/len(student_engagement)
        non_student_mean=sum(non_student_engagement)/len(non_student_engagement)

        for x in student_engagement:
            variance_x+=(x-student_mean)**2
        std_dev_student=(variance_x/(len(student_engagement)-1))**0.5

        for j in non_student_engagement:
            variance_y += (j - non_student_mean) ** 2
        std_non_student = (variance_y /(len(non_student_engagement) - 1)) ** 0.5

        n_student=len(student_engagement)
        n_non_student=len(non_student_engagement)
        pooled=(((n_student - 1) * std_dev_student ** 2 + (n_non_student - 1) * std_non_student ** 2) / (n_student + n_non_student - 2)) ** 0.5
        cohens_d=(student_mean-non_student_mean)/pooled

        return round(cohens_d, 4)

    else:
        if len(student_engagement)==0:
            ans = 'No students engaged in social media'
        elif len(non_student_engagement)==0:
            ans = 'No non-students engaged in social media'
        else:
            ans = 'No person engaged in social media'
        return ans


