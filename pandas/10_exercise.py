# Salaries Exercise
# 1. Import Pandas as pd
import pandas as pd

# 2. Read Salaries.csv as a dataframe called sal
sal = pd.read_csv('Salaries.csv')

# 3. Check the head of the DataFrame
sal.head()

# 4. Use the .info() method to find out how many entries there are
sal.info()

# 5. What is the average BasePay?
sal['BasePay'].mean()

# 6. What is the highest amount of OvertimePay in the dataset?
sal['OvertimePay'].max()

# 7. What is the job title of JOSEPH DRISCOLL?
# Note: Use all caps, otherwise you may get an answer that doesn't match up
sal[['EmployeeName'] == 'JOSEPH DRISCOLL']

# 8. How much does JOSEPH DRISCOLL make (including benefit)?
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']

# 9. What is the name of highest paid person (including benefit)?
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']
# or
sal.loc[sal['TotalPayBenefits'].idxmax()]

# 10. What is the name of lowest paid person (including benefits)?
sal.iloc[sal['TotalPayBenefits'].argmin()]

# 11. What was the average BasePay of all employees per year? (2011 - 2014)?
sal.groupby('Year').mean()['BasePay']

# 12. How many unique job titles are there?
sal['JobTitle'].nunique()

# 13. What are the top 5 most common jobs?
sal['JobTitle'].value_counts().head(5)

# 14. How many job titles were represented by only one person in 2013?
# (e.g. Job Titles with only one occurence in 2013?)
sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

# 15. How many people have the word Chief in their job title?

# need a helper method


def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False


# apply the helper method
sal['JobTitle'].apply(lambda x: chief_string(x))

# Is there a correlation between length of the Job Title and Salary?
sal['title_ten'] = sal['JobTitle'].apply(len)

sal[['JobTitle', 'title_ten']].corr()
