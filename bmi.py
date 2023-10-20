import tkinter as tk

window = tk.Tk()
window.minsize(width=350, height=270)
window.title("BMI Calculator")

def formula():

    weight = weight_input.get()
    height = height_input.get()
    if len(weight) < 1:
        bmi_sonuc.config(text="Why you dont write any number??\nNeden herhangi bir numaraya yazmıyorsun??")
    else:
        if len(height) < 1:
            bmi_sonuc.config(text="Why you dont write any number??\nNeden herhangi bir numaraya yazmıyorsun??")
        else:
            try:
                #weight
                weight = int(weight)
                height = int(height)

                height /= 100
                formul_sonuc = weight / (height * height)  # or weight / (height ** 2)
                noktaSonrasi = str(formul_sonuc).split(".")[1][:2]
                bmi = float(str(int(formul_sonuc)) + "." + noktaSonrasi)
                if bmi < 18.5:
                    bmi_sonuc.config(text=f"Your BMI is: {bmi} and you are: underweight\n\nBMI sonucun: {bmi} ve senin kilo alman gerek kanka")
                elif bmi >= 18.5 and bmi <= 24.9:
                    bmi_sonuc.config(text=f"Your BMI is: {bmi} and you are: normal weight\n\nBMI sonucun: {bmi} ve sen normalsin")
                elif bmi >= 25.0 and bmi <= 29.9:
                    bmi_sonuc.config(text=f"Your BMI is: {bmi} and you are: owerweight\n\nBMI sonucun: {bmi} ve sen biraz kilolusun")
                elif bmi >= 30.0 and bmi <= 34.9:
                    bmi_sonuc.config(text=f"Your BMI is: {bmi} and you are: Obesity class 1\n\nBMI sonucun: {bmi} geçmiş oılsun kral obezlik başlamış")
                elif bmi >= 35.0 and bmi <= 39.9:
                    bmi_sonuc.config(text=f"Your BMI is: {bmi} and you are: Obesity class 2\n\nBMI sonucun: {bmi} hobaa obezite sınıf 2'ye gelmişin be olum")
                else:
                    bmi_sonuc.config(text=f"Your BMI is: {bmi} and you are: Obesity class 3\n\nBMI sonucun: {bmi} yuh devenin nalı")
            except:
                bmi_sonuc.config(text="Just enter number, not text\nSadece numara gir, yazı değil")


#bosluk
bosluk = tk.Label(height=2)
bosluk.pack()

#weight text
weight_text = tk.Label(text="Enter your weight (kg)", font=("Arial", 10, "bold"))
weight_text.pack()

#weight input
weight_input = tk.Entry(width=13)
weight_input.pack()

#height text
height_text = tk.Label(text="Enter your height (cm)", font=("Arial", 10, "bold"))
height_text.pack()

#height input
height_input = tk.Entry(width=13)
height_input.pack()

#bosluk2
bosluk2 = tk.Label(height=1)
bosluk2.pack()

#calculator button
calculator = tk.Button(text="Calculate!", command=formula)
calculator.pack()

#bmi_sonuc
bmi_sonuc = tk.Label(text="")
bmi_sonuc.pack()

window.mainloop()
