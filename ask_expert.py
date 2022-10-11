from tkinter import Tk, simpledialog, messagebox
print('Ask the Expert - Capital Cities of the World')
root = Tk()
root.withdraw()

the_world = {}

def read_from_file():
    with open('capitals_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city

def write_to_file(country_name, city_name):
    with open('capitals_data.txt', 'a') as file:
        file.write('\n', country_name + '/' + city_name)

read_from_file()

while True:
    query_country = simpledialog.askstring('Country', 'Type the name of a country:')
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
    else:
        new_city = simpledialog.askstring('Teach me', 'I don\' know!' + 'What is the capital city of ' + query_country + '?')
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)
root.mainloop()