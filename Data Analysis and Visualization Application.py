#Group Members: Celine Yeung and Natalie Korczewski
#A terminal-based data analysis and visualization program to allow users to search the number of threatened species and number of subregions in their chosen country 

import matplotlib.pyplot as plt
import numpy as np
class Region:
   """A class used to create a Region object.
 
       Attributes:
           region (str): String that represents the selected region
           number_subregions (int): Integer that represents how many subregions are within the selected region
           number_countries (int): Integer that represents how many countries are within the selected region
   """
   def __init__(self, region, number_subregions, number_countries):
       self.region = region
       self.number_subs = number_subregions
       self.number_countries = number_countries
   def print_stats(self):
       """A function that prints the region name and the number of subregions and countries within it.
 
       Parameters: None
       Return: None
 
       """
       print(f'The {self.region} region contains {self.number_subs} sub-regions and {self.number_countries} countries.\n')
def make_data_array_of_lists(data):
   ''' Function Summary:
       This function converts each row in an array of tuples into a list and creates an array of lists. Therefore, the data can be accessed by index.
       Parameters:
       Data -- An imported csv file that is an array of tuples
       Return Values:
       This function returns an array of lists based on the parameter that was passed in.'''
   list_of_data = [] # A list that will contain multiple sublists that represent each row in the data
   for row in data: # For each row that is a tuple in the array
       make_row_a_list = list(row) # Make the row a list
       list_of_data.append(make_row_a_list) # Add the sublist into list_of_data
   data = np.array(list_of_data) # Make the list of sublists into a array
   return data
#Make a list of the countries for the chosen UN region
def list_of_countries_in_region(region, country_data):
   ''' Function Summary:
       This function makes a list containing all of the countries in the selected UN region.
       Parameters:
       Region -- The UN region name that was selected by the user
       Country_data -- The country data that was converted from an array of tuples to an array of lists in the make_data_array_of_lists function.
       Return Values:
       This function returns a list of all the country names in the selected UN region. '''
   # Gives a tuple of lists - First list : Indexes of rows where the selected UN region can be found. Second list: Indexes of columns where the selected UN region can be found
   row_column_indexes = np.where(country_data == region)
   row_indexes = row_column_indexes[0] # Gets the list of row indexes where the selected UN region can be found
   countries_in_region = [] # List of countries in the selected UN region
   for index in row_indexes:
       get_country = country_data[index, 0] # Finds the country in the UN region using the row index and the first column in the country data (the names of all the countries)
       countries_in_region.append(get_country) # Adds the country name to the list of countries in the selected UN region
   return countries_in_region
def list_of_subs_in_region(region, country_data):
   ''' Function Summary:
       A function that creates a list of the subregions within the selected region.
     
       Parameters:
       Region -- The UN region name selected by the user
       Country Data -- The country data that was converted from an array of tuples to an array of lists in the make_data_array_of_lists function.
     
       Return Values:
       This function returns a list of the sub-regions within the region'''
   # Gives a tuple of lists - First list : Indexes of rows where the selected UN region can be found. Second list: Indexes of columns where the selected UN region can be found
   row_column_indexes = np.where(country_data == region)
   row_indexes = row_column_indexes[0] # Gets the list of row indexes where the UN region can be found
   sub_regions_in_region = [] # List of sub-regions within the selected UN region
   for index in row_indexes:
       get_sub = country_data[index, 2] # Finds the sub-region in the region by using the row index and the second column in country_data.
       sub_regions_in_region.append(get_sub) # Adds name of sub-regions in the selected region to the list of sub regions
   return sub_regions_in_region
def get_avg_pop_or_threatened(countries, data):
   ''' Function Summary:
       This function finds the average population or average threatened species for each country in the selected UN region, depending on the arguments that are passed in.
     
       Parameters:
       Countries -- The list of countries in the selected UN region.
       Data -- Either the population or threatened species data that was converted from an array of tuples to an array of lists in the make_data_array_of_lists function.
     
       Return Values:
       This function returns a list of the average populations or average threatened species for each country in the selected UN region.'''
   row_index_list = [] # A list of all the row indexes where each country in the selected UN region can be found in the data that is passed through
   mean_pop_or_threatened = [] # A list of the average populations or average threatened species for each country in the selected UN region
   for country in countries:
       # Gives a tuple of lists - First list : The row index where the country name can be found. Second list: The column index where the country name can be found
       row_column_index = np.where(data == country)
       row_index = int(row_column_index[0]) # Gets the row index
       row_index_list.append(row_index) # Adds the row index into a list
 
   updated_data = np.delete(data, 0, 1) # Deletes the column of country names to only have the integer values
   for index in row_index_list:
       values_in_row = [int(num) for num in updated_data[index]] # Makes a list of all the integer values in the given row
       mean_calculation = int(np.mean((values_in_row))) # Gets the average of the values_in_row list without decimals
       mean_pop_or_threatened.append(mean_calculation) # Adds the average to the list
   return mean_pop_or_threatened
#Main Function:
def main():
   #Importing csv files
   country_data = np.genfromtxt('Country_Data.csv', delimiter = ',', dtype = None, encoding = 'UTF-8', skip_header = True)
   population_data = np.genfromtxt('Population_Data.csv', delimiter = ',', dtype = None, encoding = 'UTF-8', skip_header = True)
   threatened_species_data = np.genfromtxt('Threatened_Species.csv', delimiter = ',', dtype = None,  encoding = 'UTF-8', skip_header= True)
 
   ''' The imported data was an array of tuples. However, we could not access certain coloumns and rows using indexes. Therefore, we made a function to change
   each tuple into a list. Each data set was passed through the specific function. '''
   country_data = make_data_array_of_lists(country_data)
   population_data = make_data_array_of_lists(population_data)
   threatened_species_data = make_data_array_of_lists(threatened_species_data)
 
   ''' The data was imported a second time with the headers included in the numpy arrays to avoid hard coding in the plotting process.'''
   population_data_header = np.genfromtxt('Population_Data.csv', delimiter = ',', dtype = None, encoding = 'UTF-8', skip_header = False)
   threatened_species__data_header = np.genfromtxt('Threatened_Species.csv', delimiter = ',', dtype = None,  encoding = 'UTF-8', skip_header= False)
   population_data_header = make_data_array_of_lists(population_data_header)
   threatened_species_data_header = make_data_array_of_lists(threatened_species__data_header)
   un_regions_list = []
   un_regions_list = sorted({row for row in country_data[1:,1]}) # Made a list of all the UN Regions from the Country Data. Sorted it to get rid of the duplicates and make it in alphabetical order.
   keys_for_region_dict = range(1, 1 + len(un_regions_list)) # Made a list of numbers starting from 1 to the number of UN regions there are plus 1.
   region_dict = dict(zip(keys_for_region_dict, un_regions_list)) # Made a dictionary by zipping the two lists, keys_for_region_dict and un_regions_list, to be used for the menu.
 
   stats_options_dict= {
       '1': 'Human Population Statistics',
       '2': 'Threatened Species Statistics'}
 
   while True: # While True loop (1) that will always execute unti it is broken from somewhere inside the loop. In this case, it will execute until the user chooses to quit the program.
       print('\nUN Regions:')
       for key, value in region_dict.items():
           print(f'{key}. {value}') # Prints the menu for the user.
       while True: # While True loop (2) that will always execute unti it is broken from somewhere inside the loop.
           print('\nPlease enter a region number that you would like statistics on or enter 0 to quit: ', end = '')
           region_selection = int(input())
           if region_selection in region_dict:  #Checks if input is valid region selection number by checking if it is in the region_dict.
               break # User input is valid so can break out of while True loop (2).
           elif region_selection == 0: # User can choose to quit program. Thank you statement is printed and exit() is used to quit the program.
               print('\nThank you for using our statistics program!\n')
               exit()
           else:
               print('You must enter a valid region number from the menu provided.') # User input is not valid so continue is used to go to the top of loop 2 and prompt for input again.
               continue
       print('\nStatistics Options: ')
       for key, value in stats_options_dict.items():
           print(f'{key}. {value}') # Prints the menu for the user
       while True: # While true loop (3) that will always execute until it is broken from somewhere inside the loop. In this case, it will execute until user provides correct input.
           print('\nPlease enter your requested selection number or enter 0 to quit: ', end = '')
           statistics_selection = input()
           if statistics_selection in stats_options_dict: # Checks if input is valid statistic selection number by checking if it is in the stats_option_dict
               break # Breaks out the the loop when the user choose the a valid selection number
           elif statistics_selection == '0': # User can choose to quit program. Thank you statement is printed and exit() is used to quit the program.
               print('Thank you for using our statistics program!')
               exit()
           else:
               print('You must enter a valid selection number from the menu provided.') # User input is not valid so continue is used to go to the top of loop 3 and prompt for input again.
               continue
         
       print(f'\n***{region_dict[region_selection]} {stats_options_dict[statistics_selection]}***\n')
       '''The next two lines of code pass in the following arguements - The UN region name (accessed using its key value in region_dict) and the country data '''
       countries_in_region = list_of_countries_in_region((region_dict[region_selection]), country_data) # List of countries in the selected UN region
       sub_regions_in_region = list_of_subs_in_region((region_dict[region_selection]), country_data) # List of sub-regions in the selected UN region
       # Region name and amount of sub-regions and countries printed using the class named Region
       region_instance = Region(region_dict[region_selection], len(set(sub_regions_in_region)), len(countries_in_region))
       region_instance.print_stats()
       # If statistics_selection is 1 (Human Population Statistics):
       if statistics_selection == '1':
           avg_pop_list = get_avg_pop_or_threatened(countries_in_region, population_data) # List of the average populations for each country in the selected UN region (2000-2020)
           format_string = '{country:40}{meanpop:<10}' # Formatting spacing for each country and population at a fixed width. Population is left alligned.
           print(format_string.format(country = f'Countries in the {region_dict[region_selection]} Region:', meanpop = 'Average Population 2000-2020:'))
           print('-' * 70)
           for index in range(len(countries_in_region)): # For loop that executes for the number of countries in the selected region.
               print(format_string.format(country = countries_in_region[index], meanpop = avg_pop_list[index])) # Format average population in each country into a table using format_string field width.
         
           max_pop = np.max(avg_pop_list) # Finds which number in the average population list is the greatest.
           country_with_max_pop = countries_in_region[avg_pop_list.index(max_pop)] # Finds which country belongs to that number using the index.
           min_pop = np.min(avg_pop_list) # Finds which number in the average population list is the lowest.
           country_with_min_pop = countries_in_region[avg_pop_list.index(min_pop)] # Finds which country belongs to that number using the index.
           print(f'\nThe country in the {region_dict[region_selection]} region with the maximum average population from 2000-2020 is {country_with_max_pop} with a population of {max_pop}.')
           print(f'The country in the {region_dict[region_selection]} region with the minimum average population from 2000-2020 is {country_with_min_pop} with a population of {min_pop}.\n')     
       # If statistics_selection is 2 (Threatened Species Statistics):
       else:
           avg_threaten_spe_list = get_avg_pop_or_threatened(countries_in_region, threatened_species_data) # List of the average threatened species for each country in the selected UN region
           format_string = '{country:40}{threaten_spe:<30}' # Formatting spacing for each country and threatened species at a fixed width. Threatened species are left alligned.
           print(format_string.format(country = f'Countries in the {region_dict[region_selection]} Region:', threaten_spe = 'Average Threatened Species:'))
           print('-' * 70)
           for index in range(len(countries_in_region)): # For loop that executes for the number of countries in the selected region.
               print(format_string.format(country = countries_in_region[index], threaten_spe = avg_threaten_spe_list[index]))  # Format average population in each country into a table using format_string field width.
         
           row_index_list = [] # List containing each country's row index in the Threatened Species Data
           for country in countries_in_region:
               row_column_index = np.where(threatened_species_data == country) # The country's row and column index in the Threatened Species Data
               row_index = row_column_index[0] # The country's row index
               row_index_list.append(row_index) # Appended the country's row index to the row_index_list
     
           ''' For each column that related to a specific threatened species and for each row index that related to the countries in the selected UN region,
           calculated the sum of each threatened species using the Threatened Species Data.'''
           sum_threatened_spec_list = [] # List of values equal to the sum of each threatened species in all of the countries in the selected UN Regions
           for column_index in range(1,5): # Column index 0 is not included as it is the country names
               sum_of_threatened_species = 0
               for row_index in row_index_list:
                   sum_of_threatened_species += int(threatened_species_data[row_index, column_index])
               sum_threatened_spec_list.append(sum_of_threatened_species) # Appended the total value of the specific species threatened into a list
           max_threatened_spec_num = np.max(sum_threatened_spec_list) # Found the maximum value in the list
           min_threatened_spec_num = np.min(sum_threatened_spec_list) # Found the minimum value in the list
           threatened_species = list(threatened_species_data_header[0, 1:5]) # List of the threatened species categories
           max_threatened_spec = threatened_species[sum_threatened_spec_list.index(max_threatened_spec_num)] # Found the index of the maximum value and used it to find the corresponding type of threatened species it's for
           min_threatened_spec = threatened_species[sum_threatened_spec_list.index(min_threatened_spec_num)] # Found the index of the minimum value and used it to find the corresponding type of threatened species it's for
           print(f'\nThe greatest threatened species in the {region_dict[region_selection]} region are {max_threatened_spec.lower()}.')
           print(f'The least threatened species in the {region_dict[region_selection]} region are {min_threatened_spec.lower()}.')
         
       # Plots for statistic_selection 1
 
       if statistics_selection == '1':
           '''
           First plot:
               x-cordinates: The list of the countries within the selected region
               y-cordinates: The list containing the average populations in each country
           Second plot:
               x-cordinates: The country with the greatest average population name
               y-cordinates: The country with the greatest average population value
           Third plot:
               x-cordinates: The country with the lowest average population name
               y-cordinates: The country with the lowest average population value'''
 
           plt.figure(1)
           plt.plot(countries_in_region, avg_pop_list, 'yo', label= '_nolegend_')
           plt.plot(country_with_max_pop, max_pop, 'ro') # Country with max population is plotted over top of first plot in a different colour so that the maximum population is highlighted.
           plt.plot(country_with_min_pop, min_pop, 'bo') # Country with min population is plotted over top of first plot in a different colour so that the minimum population is highlighted.
           plt.title(f'Average Population of Each Country in the {region_dict[region_selection]} Region from 2000-2020:')
           plt.xlabel(f'Countries in the {region_dict[region_selection]} Region')
           plt.xticks(rotation = 90, fontsize = 6)
           plt.ylabel('Average Population 2000-2020')
           plt.legend(('Maximum Population', 'Minimum Population'))
 
           '''
           x-cordinates: The years from 2000-2020
           y-coridnates: The list of population in the country with the greatest average population in the selected UN region'''
 
           plt.figure(2)
           plt.plot(population_data_header[0,1:22], population_data[list(country_data[:,0]).index(country_with_max_pop), range(1,22)], 'c--', label = 'Population Trend Line from 2000 - 2020')
           plt.title(f'Population From 2000-2020 in {country_with_max_pop} (The Most Populated Country in the {region_dict[region_selection]} Region)')
           plt.ylabel('Human Population')
           plt.xlabel('Years')
           plt.xticks(rotation = 90, fontsize = 6)
           plt.legend(loc='lower right')
           plt.show()
 
       # Plots for statistic_selection 2
       else:
           '''
           First plot:
               x-cordinates: The list containing the names of each threatened species
               y-cordinates: The list containing the total value of each threatened species in the selected UN region
           Second plot:
               x-cordinates: The greatest threatened species name
               y-cordinates: The greatest threatened species value
           Third plot:
               x-cordinates: The least threatened species name
               y-cordinates: The least threatened species value'''
         
           plt.figure(1)
           plt.plot(threatened_species, sum_threatened_spec_list, 'yo', label = '_nolegend_')
           plt.plot([max_threatened_spec], max_threatened_spec_num, 'ro')
           plt.plot([min_threatened_spec], min_threatened_spec_num, 'bo')
           plt.title(f'Threatened Species in the {region_dict[region_selection]} Region:')
           plt.xlabel('Threatened Species')
           plt.ylabel(f'Total Number of Threatened Species in the {region_dict[region_selection]} Region')
           plt.legend(('Greatest Threatened Species', 'Least Threatened Species'))
           '''
           x-cordinates: The list of all the countries in the selected UN region
           y-coridnates: The list of each countries average threatened species values in the selected UN region'''
         
           plt.figure(2)
           plt.plot(countries_in_region, avg_threaten_spe_list, 'yo', label = 'Average Value of Threatened Species in Country')
           plt.title(f'Average Threatened Species of Each Country in the {region_dict[region_selection]} Region:')
           plt.xlabel(f'Countries in the {region_dict[region_selection]} Region')
           plt.ylabel('Average Threatned Species')
           plt.legend(loc = 'upper right')
           plt.xticks(rotation = 90, fontsize = 6)
           plt.show()
# Do not modify the code below
if __name__ == '__main__':
   main()
