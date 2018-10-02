import time
import pandas as pd
import numpy as np

data = {'chicago': '/Users/Saleh/Desktop/Udacity/python/chicago.csv',
        'new york city': '/Users/Saleh/Desktop/Udacity/python/new_york_city.csv',
        'washington': '/Users/Saleh/Desktop/Udacity/python/washington.csv'}

name = input('Enter your name: ')
print('Hello {},\n\nWelcome to the US bikeshare Data. \
        \nNow, let\'s explore some of the data, Enjoy!'.format(name.title()))

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input('Which city would you like to explore? (chicago, new york city, or washington)\n> ').lower()
        if city in cities:
            break
        else:
            print('\n\nYour choice is not one of the available cities, please choose one of Chicago, New York City, or Washington!\n')

    # get user input for month (all, january, february, ... , june)

    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = input('Which month would you like to explore? (all, january, february, ... , june) -all- will apply no month filter\n> ').lower()
        if month in months or month == 'all':
            break
        else:
            print('\n\nYour choice is not one of the available months, please choose another month!\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = input('Which day would you like to explore? (all, monday, tuesday, ... sunday) -all- will apply no month filter?\n> ').lower()
        if day in days or day == 'all':
            break
        else:
            print('\n\nYour choice is not one of the available days, please choose another day!\n')

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
    df = pd.read_csv(data[city])

    if 'Gender' and 'Birth Year' in df.columns:
        df.columns = ['Trip ID', 'Start Time', 'End Time', 'Trip Duration',
        'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']
    else:
        df.columns = ['Trip ID', 'Start Time', 'End Time', 'Trip Duration',
        'Start Station', 'End Station', 'User Type']

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month and day of week if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """
    #1 Popular times of travel

    Displays statistics on the most frequent times of travel."""

    print('\nPopular times of travel\n')
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is: ', most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', most_common_day_of_week)
    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def station_stats(df):
    """
    #2 Popular stations and trip

    Displays statistics on the most popular stations and trip."""

    print('\nPopular stations and trip\n')
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is :', most_commonly_used_start_station)

    # display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is :', most_commonly_used_end_station)

    # display most frequent combination of start station and end station trip
    #most_frequent_combination = df['Start Station', 'End Station'].mode()[0]
    #print('The most commonly combination of start station and end station trip is: ', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """
    #3 Trip duration

    Displays statistics on the total and average trip duration."""

    print('\nTrip duration\n')
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is :', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is :', mean_travel_time)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

def users_stats(df):
    """
    #4 Users Stats

    Displays statistics on bikeshare users."""

    print('\nUser info\n')
    print('\nCalculating Users Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('Counts of user types is :', counts_of_user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print('Counts of gender is :', counts_of_gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year_of_birth = int(df['Birth Year'].min())
        print('The earliest year of birth :', earliest_year_of_birth)
        most_recent_year_of_birth = int(df['Birth Year'].max())
        print('The most recent year of birth :', most_recent_year_of_birth)
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print('The most common year of birth :', most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_info(df):
    """
    #5 Trip Info

    Displays raw bikeshare data by trip id."""

    print('\nUser Info\n')

    df.set_index('Trip ID', inplace=True)

    # print the data at a time per the user's ID, then ask the user if they would like to see 5 more random users
    for t in range(len(df)):
        t1 = input('\n\nIf you have chosen to not filter by month or day, would you like to see a specified trip\'s data? Enter y or n.\n').lower()
        if t1 != 'y':
            break
        trip_id = int(input('\nCould you please enter the trip ID\n'))
        if trip_id in df.index.values:
            data_info1 = df.ix[trip_id]
            print(data_info1)
        else:
            print('\n\nYour trip id does not match one of the available trip ids in the data, please double check!\n')

    print('-'*40)

def users_info(df):
    """
    #6 Users Info

    Displays raw bikeshare data per 5 user."""

    print('\nUsers Info\n')

    df.reset_index(level=0, inplace=True)

    # ask the users if they would like to see data of 5 random users
    for d in range(0, len(df), 5):
        df1 = input('\n\nWould you like to see 5 users\' trip data? Enter y or n.\n').lower()
        if df1 != 'y':
            break
        data_info = df.ix[d: d+4]
        print(data_info)

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        users_stats(df)
        trip_info(df)
        users_info(df)

        restart = input('\nWould you like to restart? Enter y or n.\n')
        if restart.lower() != 'y':
            break

if __name__ == "__main__":
	main()
