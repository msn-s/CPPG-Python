#----------------------------------------------------------
# Author: Mason Hilder
# Date: August 4th, 2025
# Description: Create a Character customization application
# that follows DnD rules, that you can save and load
# characters that have the user has previously saved
#-----------------------------------------------------------

#-----------------------------------------------------------
# I chose a very simple UI design, as it does not have to be
# very complicated. Straight to the point, easy to navigate
# if grandma wanted to use this program, she would, and would
# be able to understand it fully. I changed background and font
# color to try and add more life to it. Truthfully tkinter bugs 
# me, and i did not want to over complicate things for a very
# simple program. Thankfully i have experience iterating through
# things, and working with arrays within arrays so the Save,Load
# and delete functions were not as bad as i thought. However, it 
# was the most time consuming thing i tested the entire project.
# even took a couple day break from it.
#-------------------------------------------------------------

#region Imports
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from idlelib.tooltip import Hovertip
#endregion

#region Declarations

DND_SPECIES = ["Aasima","Dragonborn","Dwarf","Elf","Gnome","Goliath","Halfling","Human","Orc","Tiefling"]
DND_CLASSES = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock'","Wizard"]
NAME            = 0
CHARACTER_NAME  = 1
SPECIES         = 2
CLASS           = 3
STRENGTH        = 4
DEXTERITY       = 5
CONSTITUTION    = 6
INTELLIGENCE    = 7
WISDOM          = 8
CHARISMA        = 9
POINTS_LEFT     = 10
# Constants

available_points     = 27
ability_strength     = 8
ability_dexterity    = 8
ability_constitution = 8
ability_intelligence = 8
ability_wisdom       = 8
ability_charisma     = 8

saved_characters = []
stats = []

# Variables
#endregion

#region Functions
def characterComfirmation(state):
    '''A function that takes a state parameter (save, load, delete) and processes data accordingly.'''
    global saved_characters
    global stats
    global available_points
    global ability_strength
    global ability_intelligence
    global ability_dexterity
    global ability_constitution
    global ability_wisdom
    global ability_charisma

    if messagebox.askyesno(title="%s Character Preset" % (state), message="Would you like to %s your character preset?" % (state)):

        if state == "Save":
            name = entryName.get().strip()
            characterName = entryCharacterName.get().strip()
            species = cboSpecies.get().strip()
            classes = cboClass.get().strip()

            if not name or not characterName or not species or not classes:
                messagebox.showwarning("Missing Info", "Please fill in all fields before saving.")
                return

            strength = ability_strength
            dexterity = ability_dexterity
            constitution = ability_constitution
            intelligence = ability_intelligence
            wisdom = ability_wisdom
            charisma = ability_charisma
            pointsRemaining = available_points
            tempStats = [
                name, characterName, species, classes,  
                strength, dexterity, constitution, intelligence,
                wisdom, charisma, pointsRemaining   
            ]
                # Storing saved stats into a temporary variable to append later on 
            index = -1
            for i in range(len(saved_characters)):
                if saved_characters[i][0] == name:
                    index = i
            if index != -1:
                saved_characters[index] = tempStats
            else:
                saved_characters.append(tempStats)
                # Loop through saved characters, if index remains -1, add the character stats to the list
                # if it is not -1 replacing the existing data at that index with new stats
                # this ensures the data is updated if the name already exists, or added if its new

            cboLoad.config(values=[char[NAME] for char in saved_characters])
            cboDelete.config(values=[char[NAME] for char in saved_characters])
            messagebox.showinfo("Saved", "Character saved successfully.")

        elif state == "Load":
            selected_name = cboLoad.get().strip()
            if not selected_name:
                messagebox.showwarning("No Selection", "Please select a character to load.")
                return

            found = False
            for i in range(len(saved_characters)):
                if saved_characters[i][0] == selected_name:
                    char = saved_characters[i]

                    entryName.delete(0, tk.END)
                    entryName.insert(0, char[NAME])

                    entryCharacterName.delete(0, tk.END)
                    entryCharacterName.insert(0, char[CHARACTER_NAME])

                    cboSpecies.set(char[SPECIES])
                    cboClass.set(char[CLASS])

                    ability_strength = char[STRENGTH]
                    ability_dexterity = char[DEXTERITY]
                    ability_constitution = char[CONSTITUTION]
                    ability_intelligence = char[INTELLIGENCE]
                    ability_wisdom = char[WISDOM]
                    ability_charisma = char[CHARISMA]
                    available_points = char[POINTS_LEFT]

                    lblStrength.config(text="Strength: %s" % (ability_strength))
                    lblDexterity.config(text="Dexterity: %s" % (ability_dexterity))
                    lblConstitution.config(text="Constitution: %s" % (ability_constitution))
                    lblIntelligence.config(text="Intelligence: %s" % (ability_intelligence))
                    lblWisdom.config(text="Wisdom: %s" % (ability_wisdom))
                    lblCharisma.config(text="Charisma: %s" % (ability_charisma))
                    lblPoints.config(text="Points Left: %s" % (available_points))

                    found = True

            if found:
                messagebox.showinfo("Loaded", "Character loaded successfully.")

        elif state == "Delete":
            selected_name = cboDelete.get().strip()
            if not selected_name:
                messagebox.showwarning("No Selection", "Please select a character to delete.")
                return

            if messagebox.askyesno("Delete Character", "Are you sure you want to delete %s?" % (selected_name)):
                found = False
                new_list = []
                for char in saved_characters:
                    if char[NAME] != selected_name:
                        new_list.append(char)
                    else:
                        found = True
                saved_characters[:] = new_list  # If we have two users with same name, it will replace it, not needed but thought it would be nice

                cboLoad.config(values=[char[NAME] for char in saved_characters])
                cboDelete.config(values=[char[NAME] for char in saved_characters])
                if found:
                    messagebox.showinfo("Deleted", "Character deleted successfully.")



def get_cost(score):
    '''A function that returns the cost of total points needed depedning on the score of the ability'''

    if score == 8: return 0
    elif score == 9: return 1
    elif score == 10: return 2
    elif score == 11: return 3
    elif score == 12: return 4
    elif score == 13: return 5
    elif score == 14: return 7
    elif score == 15: return 9

def increasePoints(ability):
    '''A function that increases skill points, taking the ability as a parameter when clicking on the button'''

    global available_points
    global ability_strength
    global ability_intelligence
    global ability_dexterity
    global ability_constitution
    global ability_wisdom
    global ability_charisma

    if ability == "Strength":
        old_score = ability_strength
        if old_score < 15:
            new_score = old_score + 1
            cost_change = get_cost(new_score) - get_cost(old_score)
            if available_points >= cost_change:
                ability_strength = new_score
                available_points -= cost_change
                lblStrength.config(text="Strength: %s" % (ability_strength))

    elif ability == "Dexterity":
        old_score = ability_dexterity
        if old_score < 15:
            new_score = old_score + 1
            cost_change = get_cost(new_score) - get_cost(old_score)
            if available_points >= cost_change:
                ability_dexterity = new_score
                available_points -= cost_change
                lblDexterity.config(text="Dexterity: %s" % (ability_dexterity))

    elif ability == "Constitution":
        old_score = ability_constitution
        if old_score < 15:
            new_score = old_score + 1
            cost_change = get_cost(new_score) - get_cost(old_score)
            if available_points >= cost_change:
                ability_constitution = new_score
                available_points -= cost_change
                lblConstitution.config(text="Constitution: %s" % (ability_constitution))

    elif ability == "Intelligence":
        old_score = ability_intelligence
        if old_score < 15:
            new_score = old_score + 1
            cost_change = get_cost(new_score) - get_cost(old_score)
            if available_points >= cost_change:
                ability_intelligence = new_score
                available_points -= cost_change
                lblIntelligence.config(text="Intelligence: %s" % (ability_intelligence))

    elif ability == "Wisdom":
        old_score = ability_wisdom
        if old_score < 15:
            new_score = old_score + 1
            cost_change = get_cost(new_score) - get_cost(old_score)
            if available_points >= cost_change:
                ability_wisdom = new_score
                available_points -= cost_change
                lblWisdom.config(text="Wisdom: %s" % (ability_wisdom))

    elif ability == "Charisma":
        old_score = ability_charisma
        if old_score < 15:
            new_score = old_score + 1
            cost_change = get_cost(new_score) - get_cost(old_score)
            if available_points >= cost_change:
                ability_charisma = new_score
                available_points -= cost_change
                lblCharisma.config(text="Charisma: %s" % (ability_charisma))

    lblPoints.config(text="Points Left: %s" % (available_points), font=("Arial", 11))
    Hovertip(lblPoints,"Available Points left: %s" % (available_points))

def decreasePoints(ability):
    '''A function that decreases skill points, taking the ability as a parameter when clicking on the button'''
    global available_points
    global ability_strength
    global ability_intelligence
    global ability_dexterity
    global ability_constitution
    global ability_wisdom
    global ability_charisma

    if ability == "Strength" and ability_strength > 8:
        old_score = ability_strength
        new_score = old_score - 1
        refund = get_cost(old_score) - get_cost(new_score)
        ability_strength = new_score
        available_points += refund
        lblStrength.config(text="Strength: %s" % (ability_strength))

    elif ability == "Dexterity" and ability_dexterity > 8:
        old_score = ability_dexterity
        new_score = old_score - 1
        refund = get_cost(old_score) - get_cost(new_score)
        ability_dexterity = new_score
        available_points += refund
        lblDexterity.config(text="Dexterity: %s" % (ability_dexterity))

    elif ability == "Constitution" and ability_constitution > 8:
        old_score = ability_constitution
        new_score = old_score - 1
        refund = get_cost(old_score) - get_cost(new_score)
        ability_constitution = new_score
        available_points += refund
        lblConstitution.config(text="Constitution: %s" % (ability_constitution))

    elif ability == "Intelligence" and ability_intelligence > 8:
        old_score = ability_intelligence
        new_score = old_score - 1
        refund = get_cost(old_score) - get_cost(new_score)
        ability_intelligence = new_score
        available_points += refund
        lblIntelligence.config(text="Intelligence: %s" % (ability_intelligence))

    elif ability == "Wisdom" and ability_wisdom > 8:
        old_score = ability_wisdom
        new_score = old_score - 1
        refund = get_cost(old_score) - get_cost(new_score)
        ability_wisdom = new_score
        available_points += refund
        lblWisdom.config(text="Wisdom: %s" % (ability_wisdom))

    elif ability == "Charisma" and ability_charisma > 8:
        old_score = ability_charisma
        new_score = old_score - 1
        refund = get_cost(old_score) - get_cost(new_score)
        ability_charisma = new_score
        available_points += refund
        lblCharisma.config(text="Charisma: %s" % (ability_charisma))

    lblPoints.config(text="Points Left: %s" % (available_points), font=("Arial", 11))
    Hovertip(lblPoints,"Available Points left: %s" % (available_points))
#endregion

#region Initialize UI
window = tk.Tk()
window.geometry("600x400")
window.title("DnD Character Creator")
window.config(bg="#553F43")
window.resizable(False,False)

# Row 0 
lblPlayerName = tk.Label(window, text="Name:", font=("Arial", 11), bg="#553F43",fg="#FFFFFF")
lblPlayerName.grid(row=0, column=0,pady=5,padx=0,sticky="E")

entryName = tk.Entry(window, width=19, bg="#FFFFFF")
entryName.grid(row=0, column=1, sticky="W",padx=0,pady=5)

#lblSpacer = tk.Label(window, text="Spacer", fg="#553F43",bg="#553F43")
#lblSpacer.grid(row=0,column=2)

btnSave = tk.Button(window,text="Save",width=6,command=lambda: characterComfirmation("Save"))
btnSave.grid(row=0,column=3,padx=20,pady=0)

btnLoad = tk.Button(window,text="Load",width=6,command=lambda: characterComfirmation("Load"))
btnLoad.grid(row=0,column=4,padx=20,pady=0)

btnDelete = tk.Button(window,text="Delete",width=6,command=lambda: characterComfirmation("Delete"))
btnDelete.grid(row=0,column=5,padx=20,pady=0)

# Row 1 
lblCharacterName = tk.Label(window, text="Character Name:", font=("Arial", 11), bg="#553F43",fg="#FFFFFF")
lblCharacterName.grid(row=1, column=0,pady=5,padx=0,sticky="W")

entryCharacterName = tk.Entry(window, width=19, bg="#FFFFFF")
entryCharacterName.grid(row=1, column=1, sticky="W",padx=0,pady=5)

#lblSpacer = tk.Label(window, text="Spacer", fg="#553F43",bg="#553F43")
#lblSpacer.grid(row=1,column=2)

cboLoad = ttk.Combobox(window,values=[char[NAME] for char in saved_characters],width=16,state="readonly") # Figuring out how to display Name only in cbo box was annoying. 
cboLoad.grid(row=1,column=4,padx=5,pady=0)

cboDelete = ttk.Combobox(window,values=[char[NAME] for char in saved_characters],width=16,state="readonly")
cboDelete.grid(row=1,column=5,padx=5,pady=0)

# Row 2
lblSpecies = tk.Label(window,text="Species:",font=("Arial", 11), bg="#553F43",fg="#FFFFFF")
lblSpecies.grid(row=2,column=0,sticky="E",padx=0,pady=5)

cboSpecies = ttk.Combobox(window,values=DND_SPECIES,width=19,state="readonly")
cboSpecies.grid(row=2,column=1)

# Row 3
lblClass = tk.Label(window,text="Classes:",font=("Arial", 11), bg="#553F43",fg="#FFFFFF")
lblClass.grid(row=3,column=0,sticky="E",padx=0,pady=5)

cboClass = ttk.Combobox(window,values=DND_CLASSES,width=19,state="readonly")
cboClass.grid(row=3,column=1)

# Row 4 - 
lblPoints = tk.Label(window,text="Points Left: %s" % (available_points),font=("Arial", 11), bg="#553F43",fg="#FFFFFF")
lblPoints.grid(row=4,column=1,sticky="E",padx=0,pady=5)

# Row 5
lblStrength = tk.Label(window,text="Strength: %s" % (ability_strength),font=("Arial", 11), bg="#553F43",fg="#01befe")
lblStrength.grid(row=5,column=0,sticky="E",padx=0,pady=5)

btnUpStrength = tk.Button(window, text="↑", command=lambda: increasePoints("Strength"))
btnUpStrength.grid(row=5,column=1,padx=20,pady=5,sticky="W")

btnDownStrength = tk.Button(window, text="↓", command=lambda: decreasePoints("Strength"))
btnDownStrength.grid(row=5,column=1,padx=0,pady=5,sticky="W")

# Row 6
lblDexterity = tk.Label(window,text="Dexterity: %s" % (ability_dexterity),font=("Arial", 11), bg="#553F43",fg="#ffdd00")
lblDexterity.grid(row=6,column=0,sticky="E",padx=0,pady=5)

btnUpDexterity = tk.Button(window, text="↑", command=lambda: increasePoints("Dexterity"))
btnUpDexterity.grid(row=6,column=1,padx=20,pady=5,sticky="W")

btnDownDexterity = tk.Button(window, text="↓", command=lambda: decreasePoints("Dexterity"))
btnDownDexterity.grid(row=6,column=1,padx=0,pady=5,sticky="W")

# Row 7
lblConstitution = tk.Label(window,text="Constitution: %s" % (ability_constitution),font=("Arial", 11), bg="#553F43",fg="#ff7d00")
lblConstitution.grid(row=7,column=0,sticky="E",padx=0,pady=5)

btnUpConstitution = tk.Button(window, text="↑", command=lambda: increasePoints("Constitution"))
btnUpConstitution.grid(row=7,column=1,padx=20,pady=5,sticky="W")

btnDownConstitution = tk.Button(window, text="↓", command=lambda: decreasePoints("Constitution"))
btnDownConstitution.grid(row=7,column=1,padx=0,pady=5,sticky="W")

# Row 8
lblIntelligence = tk.Label(window,text="Intelligence: %s" % (ability_intelligence),font=("Arial", 11), bg="#553F43",fg="#ff006d")
lblIntelligence.grid(row=8,column=0,sticky="E",padx=0,pady=5)

btnUpIntelligence = tk.Button(window, text="↑", command=lambda: increasePoints("Intelligence"))
btnUpIntelligence.grid(row=8,column=1,padx=20,pady=5,sticky="W")

btnDownIntelligence = tk.Button(window, text="↓", command=lambda: decreasePoints("Intelligence"))
btnDownIntelligence.grid(row=8,column=1,padx=0,pady=5,sticky="W")

# Row 9
lblWisdom = tk.Label(window,text="Wisdom: %s" % (ability_wisdom),font=("Arial", 11), bg="#553F43",fg="#adff02")
lblWisdom.grid(row=9,column=0,sticky="E",padx=0,pady=5)

btnUpWisdom = tk.Button(window, text="↑", command=lambda: increasePoints("Wisdom"))
btnUpWisdom.grid(row=9,column=1,padx=20,pady=5,sticky="W")

btnDownWisdom = tk.Button(window, text="↓", command=lambda: decreasePoints("Wisdom"))
btnDownWisdom.grid(row=9,column=1,padx=0,pady=5,sticky="W")

# Row 10
lblCharisma = tk.Label(window,text="Charisma: %s" % (ability_charisma),font=("Arial", 11), bg="#553F43",fg="#8f00ff")
lblCharisma.grid(row=10,column=0,sticky="E",padx=0,pady=5)

btnUpCharisma = tk.Button(window, text="↑", command=lambda: increasePoints("Charisma"))
btnUpCharisma.grid(row=10,column=1,padx=20,pady=5,sticky="W")

btnDownCharisma = tk.Button(window, text="↓", command=lambda: decreasePoints("Charisma"))
btnDownCharisma.grid(row=10,column=1,padx=0,pady=5,sticky="W")
#endregion

#region Hovertips
Hovertip(lblPoints,"Available Points left %s" % (available_points))
Hovertip(entryName,"Please enter your name!")
Hovertip(entryCharacterName,"Please enter your characters name!")
Hovertip(cboSpecies,"Please select your species!")
Hovertip(cboClass,"Please select your class!")
Hovertip(btnUpStrength,"Increase strength ability by 1 point")
Hovertip(btnDownStrength,"Decrease strength ability by 1 point")
Hovertip(btnUpDexterity,"Increase dexterity ability by 1 point")
Hovertip(btnDownDexterity,"Decrease dexterity ability by 1 point")
Hovertip(btnUpIntelligence,"Increase intelligence ability by 1 point")
Hovertip(btnDownIntelligence,"Decrease intelligence ability by 1 point")
Hovertip(btnUpCharisma,"Increase charisma ability by 1 point")
Hovertip(btnDownCharisma,"Decrease charisma ability by 1 point")
Hovertip(btnUpWisdom,"Increase wisdom ability by 1 point")
Hovertip(btnDownWisdom,"Decrease wisdom ability by 1 point")
Hovertip(btnUpConstitution,"Increase constitution ability by 1 point")
Hovertip(btnDownConstitution,"Decrease constitution ability by 1 point")
Hovertip(btnSave,"Would you like to save your character?")
Hovertip(btnLoad,"Would you like to load your character?")
Hovertip(btnDelete,"Would you like to delete your character?")
Hovertip(cboLoad,"Select a character from the dropdown menu to load")
Hovertip(cboDelete,"Select a character from the dropdown menu to delete")



#endregion

#region Main Loop
window.mainloop()
#endregion