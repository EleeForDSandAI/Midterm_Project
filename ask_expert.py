from tkinter import Tk, simpledialog, messagebox
print('Ask the Expert - Capital Cities of the World')
root = Tk()
root.iconbitmap('globe.ico')
root.withdraw()

the_world = {}

def read_from_file():
    with open('capitals_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city

read_from_file()

def write_to_file(country_name, city_name):
    with open('capitals_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)

def capitalize(string):
    return string.capitalize()

def capitalizedstring(word):
    the_country = list(map(capitalize, word.split()))
    string = ''
    for i in range(len(the_country)):
        if i == len(the_country) - 1:
            string += the_country[i]
        else:
            string += the_country[i] + ' '
    return string

while True:
    try:            
        query_country = simpledialog.askstring('Country', 'Type the name of a country:')
        query_country = capitalizedstring(query_country)
        if query_country in the_world:
            result = the_world[query_country]
            messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
        elif query_country == 'Quit':
            break
        else:
            new_city = simpledialog.askstring('Teach me', 'I don\' know!' + 'What is the capital city of ' + query_country + '?')
            the_world[query_country] = capitalizedstring(new_city)
            write_to_file(query_country, capitalizedstring(new_city))
    except AttributeError:
        continue