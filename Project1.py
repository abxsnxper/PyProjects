def main(file_name,age_group,country):
    op1=student_details(country,file_name)
    op2=list_of_countries(age_group,file_name)
    op3=age_statistics(age_group,file_name)
    op4=correlation(file_name)
    return op1,op2,op3,op4

def read_file(file_name):
    '''Read the file from the csv file

    Parameters;
    file_name: Name of the csv file

    Returns:
    dict1(dict): a dictionary containing the data read from the file using string functions
    '''
    dict1={}
    with open(file_name,"r") as file:
        lines=file.readlines()
    for line in lines[1:]:
        data=line.strip('\n').split(',')
        dict1[data[0]]=[int(data[1]),data[2],float(data[3]),data[4],data[5],data[6],data[7],data[8],float(data[9]),data[10]]
        
    return dict1

def student_details(country,file_name):
    '''Function to get student details for a specific country
    with debt status True and spent more than 7 hours on social media

    Parameters:
    country(str): the country specified
    file_name:the csv file to be read

    Data:
    value[5]=country
    value[9]=debt_status
    value[2]=average time

    Return:
    student_details(list): a list containing the details of the student details(ID, Income)
    '''
    dict1 = read_file(file_name) 
    student_details=[]
    for key,value in dict1.items():
        if value[5]==country.capitalize() and value[9]=='TRUE' and float(value[2])>7:
               student=[key,float(value[8])]
               student_details.append(student)
    return student_details

def list_of_countries(age_group,file_name):
    '''
    Function to find list of unique countries for a specific age group

    Parameters:
    age_group(list): the age group given to find the unique countries
    file_name: the csv file given

    Return:
    list_of_countries(list): the list of countries in ascending order using the sorted() function
    '''
    dict3=read_file(file_name)
    list_of_countries=[]
    for key,value in dict3.items():
        if value[0] in range(age_group[0],age_group[1]+1):
            if value[5] not in list_of_countries:
                list_of_countries.append(value[5])
                
    return sorted(list_of_countries)

def age_statistics(age_group,file_name):
    '''
    Function to find the age statistics for the given age group.

    Parameters:
    age_group(list): the given age_group
    file_name: the given csv file

    Return:
    avg_time(float): the average time spent in hours
    std_deviation(float): the standard deviation of income
    ans(str): the demography that spent the lowest average time on social media
    '''
    dict4=read_file(file_name)
    income=[]
    time=[]
    for key,value in dict4.items():
        if value[0] in range(age_group[0],age_group[1]+1):
            time.append(value[2])
            income.append(value[8])
    avg_time=sum(time)/len(time)
    income_mean=sum(income)/len(income)
    std_dev_num=0
    for i in income:
        std_dev_num+=(i-income_mean)**2
    std_dev=(std_dev_num/(len(income)-1))**0.5


    urban_time=[]
    rural_time=[]
    sub_urban_time=[]
    for key,value in dict4.items():
        if value[0] in range(age_group[0],age_group[1]+1):
            if value[6] in ['Urban','urban']:
                urban_time.append(value[2])
            elif value[6] in ['Sub_Urban','sub_urban','suburban','Suburban']:
                sub_urban_time.append(value[2])
            elif value[6] in ['Rural','rural']:
                rural_time.append(value[2])
    urban_avg_time=sum(urban_time)/len(urban_time)
    rural_avg_time=sum(rural_time)/len(rural_time)
    sub_urban_avg_time=sum(sub_urban_time)/len(sub_urban_time)
    lowest=min(urban_avg_time,rural_avg_time,sub_urban_avg_time)

    if lowest==urban_avg_time:
        ans='urban'
    elif lowest==rural_avg_time:
        ans='rural'
    else:
        ans='sub_urban'


            
    return round(avg_time,4), round(std_dev,4), ans


def correlation(file_name):
    '''
    Function to calculate the correlation between age and income for platform that has the highest number of users.

    Parameters:
    file_name: the csv file given

    Returns:
    correlation(float): the correlation between ages and income for highest number of users.
    '''
    dict5=read_file(file_name)
    platform_count={}
    age_income=[]
    age=[]
    for key,value in dict5.items():
        if value[3] in platform_count:
            platform_count[value[3]]+=1
        else:
            platform_count[value[3]]=1
    
    max_count=0
    for key,value in platform_count.items():
        if value>max_count:
            max_count=value
            platform_max=key
    
    for key,value in dict5.items():
        if value[3]==platform_max:
            age_income.append(value[8])
            age.append(value[0])
    
    income_avg=sum(age_income)/len(age_income)
    age_avg=sum(age)/len(age)
    
    num=0
    den1=0
    den2=0
    for i in range(len(age)):
            num+=(age[i]-age_avg)*(age_income[i]-income_avg)
            den1+=(age[i]-age_avg)**2
            den2+=(age_income[i]-income_avg)**2
    den=den1*den2
    den_root=(den1*den2)**0.5
    
    correlation=num/den_root

    return round(correlation,4)



        






