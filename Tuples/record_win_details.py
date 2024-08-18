group_details = []
for group in range(2):
    print(f'Enter Group {group+1} Details:')
    g_name = input("What is the name of your group?: ")
    g_size = input("How many people are in your group: ")
    comp_date = input("When was the competition held?: ")
    comp_venue = input("What venue was the competition held at?: ")
    type_medal = input("What type of medal did you recieve (Gold, Silver, Bronze)?: ")
    Var_Details = (g_name, g_size, comp_date, comp_venue, type_medal)
    group_details.append(Var_Details)
print("All group details Recorded")
for items in group_details:
    print(items)