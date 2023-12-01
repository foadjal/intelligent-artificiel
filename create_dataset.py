

def arabic_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def create_dataset(start_number, end_number):
    dataset = []
    for num in range(start_number, end_number + 1):
        roman_numeral = arabic_to_roman(num)
        dataset.append((roman_numeral, num))
    return dataset

def save_to_csv(dataset, filename='dataset.csv'):
    with open(filename, 'w') as file:
        file.write("Chiffre_Romain,Nombre_Arabe\n")
        for roman_numeral, arabic_numeral in dataset:
            file.write(f"{roman_numeral},{arabic_numeral}\n")

if __name__ == "__main__":
    start_number = 1  # Vous pouvez ajuster le début selon vos besoins
    end_number = 10000000000  # 100 milliards

    generated_dataset = create_dataset(start_number, end_number)
    save_to_csv(generated_dataset)
