# Ecommerce Purchase Exercise
# 1. Import Pandas and read in the Ecommerce Purchases csv file
# and set it to a DataFrame called ecom.
import pandas as pd
ecom = pd.read_csv('Ecommerce Purchases.csv')
ecom.head()

# 2. How many rows and columns are there?
len(ecom.columns)

# 3. What is the average purchase price?
ecom['Purchase Price'].mean()

# 4. What were the highest and lowest purchase prices?
ecom['Purchase Price'].max()
ecom['Purchase Price'].min()

# 5. How many people have English 'en' as their Language of choice on the website?
ecom[ecom['Language'] == 'en']['Language'].count()

# 6. How many people have the job title of "Lawyer"?
ecom[ecom['Job'] == 'Lawyer'].count()

# 7. How many people made the purchase during the AM and
# how many people made the purchase during the PM?
ecom['AM or PM'].value_counts()

# 8. What are the 5 most common job titles?
ecom['Job'].value_counts().head(5)

# 9. Someone made a purchase that came from Lot: "90 WT", what was the Purchase Price?
ecom[ecom['Lot'] == '90 WT']['Purchase Price']

# 10. What is the email of the person with the following Credit Card Number: 4926535242672853
ecom[ecom['Credit Card'] == 4926535242672853]['Email']

# 11. How many people have American Express as their Credit Card Provider
# and made a purchase above $95?
ecom[(ecom['CC Provider'] == 'American Express')
     & (ecom['Purchase Price'] > 95)].count()

# 12. How many people have a credit card that expires in 2025?
ecom[ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25')].count()

# 13. What are the top 5 most popular email providers/hosts
ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)
