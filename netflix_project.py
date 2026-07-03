# Load and Understand the data
import pandas as pd
df = pd.read_csv("C:/Users/Hajra Syed/OneDrive/netfilx_1.csv")

print(df.head())
print(df.info())
print(df.shape)

# Check missing value
print(df.isnull().sum())

# Check Duplicate records
print(df.duplicated().sum())

# Convert date_added to datetime
df['date_added'] = pd.to_datetime(
    df['date_added'],
    format='mixed'
)

# Clean text column
text_columns = ['title','director','country','listed_in','description']

for col in text_columns:
    df[col] = df[col].str.replace(r'\s+',' ',regex=True).str.strip()

# Standrize Text Case
df['type'] = df['type'].str.title()

# Handling missing values
# Director(missing values)=2634
df['director'] = df['director'].fillna('Unknown')

# Cast = 825
df['cast'] = df['cast'].fillna('Not Available')

# Country = 831
df['country'] = df['country'].fillna('Unknown')

# date_added = 10  removes those rows where date is missing bcoz vis tools need proper dates
df=df.dropna(subset=['date_added'])

# rating = 4
df['rating'] = df['rating'].fillna('Not Rated')

# duration = 3
df['duration']=df['duration'] .fillna('Unknown')


# clean duration column
df['duration_value'] = df['duration'].str.extract(r'(\d+)')
df['duration_unit'] = df['duration'].str.extract(r'([A-Za-z]+)')

df['duration_value']=pd.to_numeric(
    df['duration_value'] ,
    errors= 'coerce'
)
df['duration_value'] = df['duration_value'].astype('Int64')

# WISHING A HAPPY BIRTHDAY TO HAJRA NAUSHEEN 

# extract primary genre
df['primary_genre'] = (df['listed_in'].str.split(',').str[0].str.strip())


# Create new columns from date_added
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month_name()


# Rename cast column bcoz cast is a keyword in sql
df.rename(columns={'cast': 'cast_members'}, inplace=True)

print(df[['duration', 'duration_value', 'duration_unit']].head(10))

print(df.info())
print(df.isnull().sum())

df.to_csv(
    "netflix_cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully!")

