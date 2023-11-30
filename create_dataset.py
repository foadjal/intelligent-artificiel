import roman

def create_dataset(start, end):
    dataset = []

    for num in range(start, end + 1):
        roman_numeral = roman.fromRoman(roman.toRoman(num))
        dataset.append((roman_numeral, num))

    return dataset

def save_to_csv(dataset, filename='dataset.csv'):
    with open(filename, 'w') as file:
        file.write("Chiffre_Romain,Nombre_Arabe\n")
        for roman_numeral, arabic_numeral in dataset:
            file.write(f"{roman_numeral},{arabic_numeral}\n")

if __name__ == "__main__":
    start_number = 1  # Vous pouvez ajuster le début selon vos besoins
    end_number = 100000000000  # 100 milliards

    generated_dataset = create_dataset(start_number, end_number)
    save_to_csv(generated_dataset)
