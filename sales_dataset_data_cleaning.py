# importing the libraries
import pandas as pd

# importing the datasets
lst_of_Ord_dataset = "C:/Users/HIMANSHU GUPTA/Data analysis folder/sales_data_analysis/List of Orders.csv"
ord_dtl_dataset = "C:/Users/HIMANSHU GUPTA/Data analysis folder/sales_data_analysis/Order Details.csv"
sal_trg_dataset = "C:/Users/HIMANSHU GUPTA/Data analysis folder/sales_data_analysis/Sales target.csv"

df_ol = pd.read_csv(lst_of_Ord_dataset)
df_od = pd.read_csv(ord_dtl_dataset)
df_st = pd.read_csv(sal_trg_dataset)

# merging the df_ol and df_od dataframes
df = df_ol.merge(df_od,on = 'Order ID')

## data pre-processing ##

# checking duplicates values.
#df1 = df.loc[df.duplicated(keep = False),:]
# droping duplicate values
#df = df.loc[df.drop_duplicates(inplace = True),:]

# removing unwanted columns.
unwanted_columns = ['Order ID','CustomerName']
df = df[df.drop(unwanted_columns, axis = 1, inplace = True)]

# stripping the empty spaces in state column.
#df.State.unique()
df.State = df.State.apply(lambda x: x.strip())

# creating a new column called Region 
North = ["Jammu and Kashmir", "Punjab","Himachal Pradesh", "Delhi","Uttarakhand",
         "Haryana","Uttar Pradesh","Chandigarh"]
South = ["Kerala","Tamil Nadu", "Andhra Pradesh","Karnataka"]
West  = ["Maharashtra", "Gujarat","Goa","Rajasthan"]
East  = ["Nagaland","Sikkim","West Bengal","Bihar"]
Central = ["Madhya Pradesh"]

# Function for region column.
def region(x):
    if x in East:
        return "East"
    if x in South:
        return "South"
    if x in West:
        return "West"
    if x in North:
        return "North"
    if x in Central:
        return "Central"
    else: return 'None'
# applying function
df['Region'] = df['State'].apply(region)

# renaming the order_date column into date column
df = df.rename(columns = {'Order Date': 'Order_date'})

# converting Order_Date column into datetime datatype
df['Order_date'] = pd.to_datetime(df['Order_date'])

# taking month,year from Order_Date column.
df['Month'] = df['Order_date'].dt.month
df['Year']  = df['Order_date'].dt.year
df['Date']  = df['Order_date'].dt.date

# Function for date column.
def month(x):
    if x == 1:
        return 'January'
    elif x == 2:
        return 'February'
    elif x == 3:
        return 'March'
    elif x == 4:
        return 'April'
    elif x == 5:
        return 'May'
    elif x == 6:
        return 'June'
    elif x == 7:
        return 'July'
    elif x == 8:
        return 'August'
    elif x == 9:
        return 'September'
    elif x == 10:
        return 'october'
    elif x == 11:
        return 'November'
    elif x == 12:
        return 'December'
    else: return 'None'
# applying function    
df['Month'] = df['Month'].apply(month)

# converting category column string datatype into category datatype.
df['Category'] = df['Category'].astype('category')

# making new csv file.
df.to_csv(r'C:/Users/HIMANSHU GUPTA/Data analysis folder/sales_data_analysis/sales_analysis_cleaned_dataset.csv',index=False)
