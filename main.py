import tkinter as tk
from tkinter import messagebox

# Funksioni per ndertimin e inverted index
def build_inverted_index():
    inverted_index = {}
    # Hap skedarin "index.txt" për lexim
    with open("index.txt", 'r') as file:
        for line_num, line in enumerate(file, start=1):
            words = line.strip().split()
            for word in words:
                # Normalizimi i fjaleve ne lowercase per te bere kerkimin case-insensitive
                word = word.lower()
                if word not in inverted_index:
                    inverted_index[word] = [line_num]
                else:
                    inverted_index[word].append(line_num)
    return inverted_index

# Funksioni per kerkimin e nje fjale ne inverted index
def search_word(inverted_index, word):
    # Normalizimi i fjales ne lowercase per te bere kerkimin case-insensitive
    word = word.lower()
    if word in inverted_index:
        return inverted_index[word]
    else:
        return None

# Funksioni qe ekzekutohet kur shtypet butoni "Search"
def search():
    search_word_result = entry.get()
    search_result = search_word(inverted_index, search_word_result)

    if search_result:
        # Hap fajllin "search_result.txt" per te shkruar rezultatet e kerkimit
        with open("search_result.txt", 'w') as output_file:
            output_file.write(f"Search results for '{search_word_result}':\n")
            positions = {}  # Dictionary per te ruajtur pozitat e fjales ne cdo rresht
            with open("index.txt", 'r') as index_file:
                lines = index_file.readlines()
                for line_num in search_result:
                    line = lines[line_num - 1].strip()
                    output_file.write(f"Line {line_num}: {line}\n")
                    # Gjej pozitat e fjales ne kete rresht dhe ruaj ato
                    line_positions = [i+1 for i in range(len(line.split())) if line.split()[i].lower() == search_word_result.lower()]
                    positions[line_num] = line_positions
            # Shkruaj pozitat ne fajllin e output
            for line_num, pos_list in positions.items():
                output_file.write(f"Positions of '{search_word_result}' in Line {line_num}: {pos_list}\n")
    else:
        # Shtoni fjalen ne index.txt nese nuk gjendet
        with open("index.txt", 'a') as index:
            index.write(search_word_result + "\n")
        messagebox.showinfo("Search Result", f"The word '{search_word_result}' doesn't exist in the file.")

# Funksioni qe ekzekutohet kur mbyllet aplikacioni
def on_closing():
    if messagebox.askokcancel("Close", "Do you want to close the app?"):
        root.destroy()

# Krijimi i GUI
root = tk.Tk()
root.title("Search Box")

# Percaktimi i madhesise se dritares dhe qendrimi i saj ne ekran
window_width = 400
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

frame = tk.Frame(root, width=300, height=200)  # Rritja e madhesise se frame
frame.pack_propagate(False)  # Parandalon ndryshimin e madhesise se frame per te pershtatur permbajtjen e saj
frame.pack()

label = tk.Label(frame, text="Enter the word to search:")
label.pack()

entry = tk.Entry(frame)
entry.pack()

search_button = tk.Button(frame, text="Search", command=search)
search_button.pack()

# Nderto inverted index
inverted_index = build_inverted_index()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
