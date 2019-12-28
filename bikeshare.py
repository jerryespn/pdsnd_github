## Udacity PythonForDS - Python Project
## BikeShare
## By: JGEL

# Libraries import 
import time
import pandas as pd

# Dictionary location file setup
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# get user input for city (chicago, new york city, washington)
def get_city():

    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
        if city.lower() in ('chicago', 'new york', 'washington'):
            if city.lower() == 'chicago':
                return 'C:/Users/JulioGerardoEspinosa/Desktop/PyDev/BikeShare/DataSets/chicago.csv'
            elif city.lower() == 'new york':
                return 'C:/Users/JulioGerardoEspinosa/Desktop/PyDev/BikeShare/DataSets/new_york_city.csv'
            elif city.lower() == 'washington':
                return 'C:/Users/JulioGerardoEspinosa/Desktop/PyDev/BikeShare/DataSets/washington.csv'
            break
        print('Sorry, I just have information for Chicago, New York or Washington...')

# get user input for month (all, january, february, ... , june)
# data is filtered by month and by day
def get_date(df_city):
    months = ['All','January','Feburary','March','April','May','June']
    days = ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    while True:
        month = input('Please choose a month. You could choose from January to June, you can also choose all those months with All \n')
        if month in months:
            print('\n')
            break
    while True:
        day = input ('Please choose a day of the week \n')
        if day in days:
            print('\n')
            break

    return month, day

def load_data(city):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #print (city) // Enable to check if it is printing the right filename

    df_city = pd.read_csv(city)
    df_city['Start Time'] = pd.to_datetime(df_city['Start Time'])
    df_city['month'] = df_city['Start Time'].dt.month
    df_city['day'] = df_city['Start Time'].dt.weekday_name

    return df_city


def time_stats(df_city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    popular_month = df_city['month'].mode()[0]
    print('Most common month:', popular_month)

    # display the most common day of week

    popular_doweek = df_city['day'].mode()[0]
    print('Most common day of the week:', popular_doweek)

    # display the most common start hour
    df_city['hour'] = df_city['Start Time'].dt.hour
    popular_hour = df_city['hour'].mode()[0]
    print('Most commong start hour:', popular_hour)

    #Time to process the information
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df_city):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    df_city['start'] = df_city['Start Station']
    StartStation = df_city['start'].mode()[0]
    print ('The most common start station is: ', StartStation)
    
    # display most commonly used end station
    df_city['end'] = df_city['End Station']
    EndStation = df_city['end'].mode()[0]
    print('Display most commonly used end station: ', EndStation)
    
    # display most frequent combination of start station and end station trip
    StartAndEnd = df_city['start'] + ' to ' + df_city['end']
    print('Most Frequent combination of start and end station: ', StartAndEnd.mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df_city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_start = pd.to_datetime(df_city['Start Time'])
    trip_end = pd.to_datetime(df_city['End Time'])
    df_city['Total'] = trip_start - trip_end
    total_time =  df_city['Total'].sum()
    print("The total travel time was:" + str(total_time))

    # display mean travel time
    mean_time = df_city['Trip Duration'].mean()
    print("The mean travel time was: " + str(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df_city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df_city['User Type'].value_counts()
    print('User types: ', user_type)

    # Display counts of gender
    gender_number = df_city['Gender'].value_counts()
    print('Counts of gender: ', gender_number)

    # Display earliest, most recent, and most common year of birth
    earliest = df_city.sort_values('Birth Year').iloc[0]
    recent = df_city.sort_values('Birth Year').iloc[-1]
    common_year = df_city['Birth Year'].mode()[0]
    
    print('The earliest, most recent, and most common year of birth :', earliest['Birth Year'],recent['Birth Year'], common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_statswc(df_city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df_city['User Type'].value_counts()
    print('User types: ', user_type)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city = get_city()
        df_city = load_data(city)
        get_date(df_city)
        

        time_stats(df_city)
        station_stats(df_city)
        trip_duration_stats(df_city)
        
        if city == 'C:/Users/JulioGerardoEspinosa/Desktop/PyDev/BikeShare/DataSets/washington.csv':
            user_statswc(df_city)
        else:
            user_stats(df_city)

        restart = input('\nDo you want to check another city? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
