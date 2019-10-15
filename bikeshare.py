import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore the US bikeshare data!')

# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','new york city','washington']
    while True:
        city = input("What city do you want to explore? Choose one of these options: Chicago, New York City, Washington ->> your call:").lower()
        if city not in cities:
            print("Please make sure you choose one of the three options given.")
            continue
        else:
            break

# TO DO: get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june','all']
    while True:
        month = input("Do you have a specific month you want to explore? Options are between January and June. You may also choose all ->> your call:").lower()
        if month not in months:
            print("Please make sure you choose one of the months between January and June, or all. Notice: Plz type the full month, not use abbreviations.")
            continue
        else:
            break

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        day = input("How's about a specific day you are interested in? You can choose any day of the week or all ->> your call:").lower()
        if day not in days:
            print("Please make sure you type correctly a day of the week, or all, try again. Notice: Plz type the full month, not use abbreviations.")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is:',most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is:',most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour of the day is:',most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is:',most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('The most commonly used end station is:',most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_combination = df[['Start Station','End Station']].groupby(['Start Station','End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip is:',most_common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = sum(df['Trip Duration'])
    print('Total travel time in seconds is:',total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time in seconds is:',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_type = df['User Type'].value_counts()
    print('User types are:',count_type)

    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print('Gender counts are:',count_gender)
    except KeyError:
        print('There is no gender data in this dataset.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        min_dob = df['Birth Year'].min()
        print('Earliest year of birth is:',min_dob)
    except KeyError:
        print('There is no birth year data in this dataset')

    try:
        max_dob = df['Birth Year'].max()
        print('Most recent year of birth is:',max_dob)
    except KeyError:
        print('There is no birth year data in this dataset')

    try:
        common_dob = df['Birth Year'].mode()[0]
        print('Most common year of birth is:',common_dob)
    except KeyError:
        print('There is no birth year data in this dataset')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
