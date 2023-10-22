import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
slang = {
    "USA": {
        "Awesome": "Extremely good or excellent",
        "Y'all": "You all (used in the Southern dialect)",
        "Dude": "A slang term for a man",
        "Fixin' to": "Getting ready to",
        "Buck": "A dollar",
        "Chill": "Relax or hang out",
        "Crash":"Go To sleep quickly and suddenly",
        "411":"What's the gossip",
        "Score":"Achieve something you want"
    },
    "United Kingdom": {
        "Bloke": "A man",
        "Cheers": "Thanks or goodbye",
        "Knackered": "Tired or exhausted",
        "Chuffed": "Pleased or happy",
        "Gutted": "Extremely disappointed",
        "Bloody":"Dammed",
        "Trolled":"Drunk"
    },

    "Australia": {
        "Mate": "Friend",
        "Barbie": "Barbecue",
        "Arvo": "Afternoon",
        "Brekkie": "Breakfast",
        "Sickie": "A day off sick",
        "Woop Woop":"Middle of nowhere",
        "Fag":"Cigarette"
    },

    "Canada": {
        "Toque": "A winter hat",
        "Eh": "Used at the end of a sentence to seek agreement or confirmation",
        "Double-double": "A coffee with two creams and two sugars",
        "Poutine": "A dish of French fries topped with cheese curds and gravy",
        "Loonie": "A one-dollar coin",
        "Parkade":"A multi-level parking structure",
        "Sophonsified":"Sufficiently full and satisfied"
    },

    "France": {
        "C’est la galère": "It's a real pain",
        "Bouffer": "To eat",
        "Génial": "Great or fantastic",
        "Bouquin": "Book",
        "Mec": "Guy or dude"
    },

    "Germany": {
        "Fingerspitzengefühl": "Fingertip feeling; intuitive flair",
        "Klugscheißer": "Know-it-all",
        "Eier haben": "To have balls (courage)",
        "Feierabend": "End of the workday",
        "Schnapsidee": "Crazy idea or nonsense"
    },

   "Italy": {
        "Figo": "Cool or awesome",
        "Magari": "Maybe or I wish",
        "Ciao": "Hello or goodbye",
        "Pasta al dente": "Pasta cooked firm to the bite",
        "Tranquillo": "Relax or calm down"
    },

    "Spain": {
        "Vale": "Okay or all right",
        "Guay": "Cool or great",
        "Tío/Tía": "Dude/girl",
        "Empalagar": "To be too sweet or sickly",
        "Marcha": "Nightlife or party scene"
    },

    "Japan": {
        "Kawaii": "Cute",
        "Otaku": "A person with obsessive interests, particularly in anime and manga",
        "Ganbatte": "Good luck or do your best",
        "Itadakimasu": "A phrase said before eating, similar to 'bon appétit'",
        "Baka": "Fool or idiot"
    },

    "China": {
        "Guanxi": "Relationships or connections",
        "Chabuduo": "Close enough or almost there",
        "Baizuo": "A derogatory term for a naive, Western liberal",
        "Ganbei": "Cheers or bottoms up",
        "Dabao": "Takeout or to-go"
    },


    "India": {
         "Bakwas": "Nonsense or rubbish",
         "Chai": "Tea, typically spiced and sweetened",
         "cheddar": "Money",
         "GOAT": "Greatest of all time",
         "Gucci": "Good or cool",
         "LOL": "laugh out loud",
         "Lit": "Amazing",
         "Sic": "Something that is cool",
         "Snatched": "Looks good",
         "TBH": "To Be Honest",
         "YOLO": "You Only Live Once",
         "BTW": "By The Way",
         "Jugaad": "A clever, improvised solution",
         "Sasta": "Cheap or inexpensive"
    },

    "South Africa": {
         "Braai": "Barbecue",
         "Lekker": "Nice or great",
         "Yebo": "Yes",
         "Eina": "Ouch or pain",
         "Robot": "Traffic light"
    },


  
}
MEANING_NOT_FOUND = "Meaning not found for the selected slang."
NO_SLANG_FOUND = "No slang found for the selected country."
WINDOW_SIZE = "500x600"
WINDOW_BG_COLOR = '#E6E6FA'
BUTTON_BG_COLOR = '#8B008B' 
BUTTON_HOVER_COLOR = '#800080' 
BUTTON_TEXT_COLOR = '#FFFFFF'
HEADER_FONT = ("Arial", 24, "bold")
SUBHEADER_FONT = ("Arial", 14)
SLANG_TEXT_SIZE =22

def display_meaning(slang_word, country):
    if country in slang and slang_word in slang[country]:
        meaning = slang[country][slang_word]
        messagebox.showinfo("Meaning", f"Meaning of {slang_word}: {meaning}")
    else:
        messagebox.showinfo("Meaning", "Meaning not found for the selected slang.")

def display_slang():
    country = country_var.get()
    if country in slang:
        slang_words = list(slang[country].keys())
        slang_listbox.delete(0, tk.END)
        for slang_word in slang_words:
            slang_listbox.insert(tk.END, slang_word)
    else:
        slang_listbox.delete(0, tk.END)
        slang_listbox.insert(tk.END, "No slang found for the selected country.")


def clear_list():
    slang_listbox.delete(0, tk.END)
root = tk.Tk()
root.title("Country Slang Display")
root.geometry(WINDOW_SIZE)
root.configure(bg=WINDOW_BG_COLOR)

root.minsize(600, 800)
root.maxsize(600, 1000)

style = ttk.Style()
style.map('C.TButton',
          foreground=[('active', 'black'), ('!active', BUTTON_TEXT_COLOR)],
          background=[('active', BUTTON_HOVER_COLOR), ('!active', BUTTON_BG_COLOR)])

header_label = ttk.Label(root, text="Explore Slangs Across Countries", font=HEADER_FONT, background='#FFA500', 
                         borderwidth=2, relief="solid", foreground='#FFFFFF')
header_label.pack(pady=20)

subheading_label = ttk.Label(root, text="English Assignment", font=SUBHEADER_FONT, background=WINDOW_BG_COLOR)
subheading_label.pack()


subheading2_label = ttk.Label(root, text="~ SRMIST", font=SUBHEADER_FONT, background=WINDOW_BG_COLOR)
subheading2_label.pack()

country_var = tk.StringVar()
country_dropdown = ttk.Combobox(root, textvariable=country_var, font=('Arial', 16))
country_dropdown['values'] = list(slang.keys())
country_dropdown.pack(pady=20)

slang_list_label = tk.Label(root, text="Slangs list here", font=('Arial', SLANG_TEXT_SIZE), background=WINDOW_BG_COLOR)
slang_list_label.pack(pady=20)

display_label = ttk.Label(root, text="1. Display Slang", font=('Arial', 12, 'bold'), background=WINDOW_BG_COLOR)
display_label.pack(anchor='center', pady=5)

display_button = ttk.Button(root, text="Display Slang", command=display_slang, style='C.TButton')
display_button.pack(anchor='center', pady=5)

clear_label = ttk.Label(root, text="2. Clear", font=('Arial', 12, 'bold'), background=WINDOW_BG_COLOR)
clear_label.pack(anchor='center', pady=5)

clear_button = ttk.Button(root, text="Clear", command=clear_list, style='C.TButton')
clear_button.pack(anchor='center', pady=5)

meaning_label = ttk.Label(root, text="3. Slang Meaning", font=('Arial', 12, 'bold'), background=WINDOW_BG_COLOR)
meaning_label.pack(anchor='center', pady=5)

meaning_button = ttk.Button(root, text="Slang Meaning", command=lambda: display_meaning(slang_listbox.get(tk.ACTIVE), country_var.get()), style='C.TButton')
meaning_button.pack(anchor='center', pady=5)


group_members_label = ttk.Label(root, text="Group Members:\n1.AMAN \n2. xyz\n3. xyz", anchor='se')
group_members_label.pack(side='bottom', anchor='se', padx=10, pady=10)

slang_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
slang_listbox.pack(pady=20)


root.mainloop()