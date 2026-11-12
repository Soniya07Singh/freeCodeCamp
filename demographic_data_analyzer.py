
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', header=None, skipinitialspace=True)

df.columns = [
    'age',
    'workclass',
    'fnlwgt',
    'education',
    'education-num',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'capital-gain',
    'capital-loss',
    'hours-per-week',
    'native-country',
    'salary'
]

    # How many people of each race are represented?
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = round(
        df.loc[df['sex'] == 'Male', 'age'].mean(), 1
    )

    # Percentage of people who have a Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # People with advanced education
    higher_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    # People without advanced education
    lower_education = ~higher_education

    # Percentage of people with advanced education earning >50K
    higher_education_rich = round(
        (
            (df.loc[higher_education, 'salary'] == '>50K').sum()
            / higher_education.sum()
        ) * 100,
        1
    )

    # Percentage of people without advanced education earning >50K
    lower_education_rich = round(
        (
            (df.loc[lower_education, 'salary'] == '>50K').sum()
            / lower_education.sum()
        ) * 100,
        1
    )

    # Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # People who work the minimum number of hours per week
    num_min_workers = df.loc[
        df['hours-per-week'] == min_work_hours
    ]

    # Percentage of minimum-hour workers earning >50K
    rich_percentage = round(
        (
            (num_min_workers['salary'] == '>50K').sum()
            / len(num_min_workers)
        ) * 100,
        1
    )

    # Country with the highest percentage of people earning >50K
    country_counts = df['native-country'].value_counts()

    rich_country_counts = df.loc[
        df['salary'] == '>50K', 'native-country'
    ].value_counts()

    country_percentage = (
        rich_country_counts / country_counts * 100
    ).dropna()

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(
        country_percentage.max(), 1
    )

    # Most popular occupation for people earning >50K in India
    top_IN_occupation = df.loc[
        (df['native-country'] == 'India')
        & (df['salary'] == '>50K'),
        'occupation'
    ].value_counts().idxmax()

    # Optional output
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelor's degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:",
              higher_education_rich)
        print("Percentage without higher education that earn >50K:",
              lower_education_rich)
        print("Minimum work hours:", min_work_hours)
        print("Percentage of minimum-hour workers earning >50K:",
              rich_percentage)
        print("Country with highest percentage earning >50K:",
              highest_earning_country)
        print("Percentage of that country earning >50K:",
              highest_earning_country_percentage)
        print("Most popular occupation for people earning >50K in India:",
              top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
