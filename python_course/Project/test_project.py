import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def validate_entry(value,valid_values,type_validation):

    while value not in valid_values:
        if value == '':
            value = input('Write a {}: '.format(type_validation))
        else:
            value = input('Write a {}: '.format(type_validation))
        value = value.lower()

    return value


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = ''

    month = ''

    day = ''

    valid_cities = ['chicago', 'new york city', 'washington']

    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    valid_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

    month = validate_entry(month,valid_months,'month')

    day = validate_entry(day,valid_days,'day')

    city = validate_entry(city,valid_cities,'city')


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


     #   if city == '':
        #    city = input('Write a city: ') #si pongo : fuera del '' dara error // 2na opcion .lower() aquí modifica el valor que ha escrito
      #  else:
      #      city = input('Write a valid city, PLEASE: ')
      #  city = city.lower()    #3era opcion: asignamos que la variable city sea minuscula y solo usamos lower() 1 vez (por fuera del if)

    # TO DO: get user input for month (all, january, february, ... , june)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

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
    global CITY_DATA


    # load dataframe acourding to city
    df = pd.read_csv('./datasets/' + CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    months = {
        1: 'january',
        2: 'february',
        3: 'march',
        4: 'april',
        5: 'may',
        6: 'june'
    }

    df['month'] = df['Start Time'].dt.month.map(months)
    df['day'] = df['Start Time'].dt.day_name()


    if day != 'all':
        df = df[df['day'] == day.capitalize()] # Monday  ---- monday.capitalize() -> Monday

    if month != 'all':
        df = df[df['month'] == month]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()
    print('The most common month is {}'.format(most_common_month[0]))

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()
    print('The most common day of week is {}'.format(most_common_day[0]))

    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()
    print('The most common start hour is {}'.format(most_common_hour[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station = df['Start Station'].mode()
    print('The most common start_station is {}'.format(most_common_start_station[0]))


    # TO DO: display most commonly used end station

    most_common_end_station = df['End Station'].mode()
    print('The most common end_station is {}'.format(most_common_end_station[0]))


    # TO DO: display most frequent combination of start station and end station trip
    df_station = df.groupby(['Start Station', 'End Station']).count()
    df_station = df_station['Start Time']
    start_end_station = df_station.idxmax()
    print('The most frequent combination of start station and end station trip is {}'
          .format(start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {} seconds'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_user_counts = df['User Type'].value_counts()
    print(type_user_counts.reset_index().rename(columns={'index': 'User Type',
                                                     'User Type': 'Frequency'}))

    # TO DO: Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print(gender_counts.reset_index().rename(columns={'index': 'Gender',
                                                     'Gender': 'Frequency'}))

    # TO DO: Display earliest, most recent, and most common year of birth
    min_birth = df['Birth Year'].min()
    max_birth = df['Birth Year'].max()
    mode_birth = df['Birth Year'].mode()
    print('year of birth --> Earliest: {}, most recent: {}, most common: {}'.
          format(min_birth, max_birth, mode_birth[0]))

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
