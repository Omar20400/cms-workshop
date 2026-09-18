# حاسبة الكتلة المولية
masses = {
    "H": 1.008,
    "O": 15.999,
    "C": 12.011,
    "N": 14.007,
    "Na": 22.990,
    "Cl": 35.45,
}

formula = input("اكتب الصيغة الكيميائية (مثال: H2O): ")

total = 0
i = 0
while i < len(formula):
    element = formula[i]
    i = i + 1
    number = ""
    while i < len(formula) and formula[i].isdigit():
        number = number + formula[i]
        i = i + 1
    if number == "":
        number = "1"
    total = total + masses[element] * int(number)

print("الكتلة المولية =", total)