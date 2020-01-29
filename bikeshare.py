import time
import pandas as pd
import numpy as np
import datetime as dt

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Select a city that you want to explore bikeshare data '
                     'Chicago, New York City, or Washington?\n').lower()

        if city.lower() in CITY_DATA:

            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Select a month All, January '
                      'February, March, April, May, or June?\n').lower()

        if month.lower() in ['all', 'january', 'february', 'march',

                             'april', 'may', 'june']:

            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which weekday would you like to use to filter data '

                    'All, Monday, Tuesday, Wednesday, Thursday, Friday, ' +

                    'Saturday, Sunday?\n').lower()

        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday',

                           'friday', 'saturday', 'sunday']:

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

    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('This is the most common Traveled Month:')
    print(df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('With the selected filter this is the most common Day of Travel:')
    print(df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('With selected filter this is the most common Start Hour of Travel:')
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The Most Common Start Station:')
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The Most Common End Station:')
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The Most Frequent Start & Stop Combination:')
    print(df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time:')
    print(dt.timedelta(seconds=int(df['Trip Duration'].sum())))

    # TO DO: display mean travel time
    print('Travel Time Mean:')
    print(dt.timedelta(seconds=int(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Counts:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('\nGender Counts:')

    try:

        print(df['Gender'].value_counts())

    except:

        print('Gender Info not included in Data')

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nEarliest, Latest & Most Common Date of Birth:')

    try:

        print('Earliest: {}\nLatest: {}\nMost Common: {}'

              .format(df['Birth Year'].min(), df['Birth Year'].max(),

                      df['Birth Year'].mode()[0]))
    except:

        print('Date of Birth not included in Data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def raw_data(df):
    """Displays 5 rows of Raw Data for every Yes."""

    raw = 'yes'
    while raw == 'yes':
        for i in df.iterrows():
            count = 0
            while count < 5:
                print(i)
                count += 1

            question = input('\nView 5 rows of raw data entries from your selected city? yes or no?\n')


            if question.lower() == 'no':
                raw = 'no'
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
