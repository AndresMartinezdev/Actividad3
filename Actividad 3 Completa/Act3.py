import tkinter as tk
from tkinter import messagebox
import math

#CON ESTO MANEJO Y CREO EL MENU PRINCIPAL DE LA INTERFAZ

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú Principal")
        self.geometry("400x300")

        # Título
        tk.Label(self, text="Menú Principal", font=("Arial", 16)).pack(pady=10)

        # Botones para las secciones
        tk.Button(self, text="Capítulo 3", command=self.abrir_capitulo3).pack(pady=5)
        tk.Button(self, text="Capítulo 4", command=self.abrir_capitulo4).pack(pady=5)
        tk.Button(self, text="Figuras Geométricas", command=self.abrir_figuras_geometricas).pack(pady=5)

    def abrir_capitulo3(self):
        Capitulo3(self)

    def abrir_capitulo4(self):
        Capitulo4(self)

    def abrir_figuras_geometricas(self):
        FigurasGeometricas(self)

#AQUI CREO LA INTERFAZ PARA EL CAPITULO 3


class Capitulo3(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Capítulo 3")
        self.geometry("400x300")

        tk.Label(self, text="Capítulo 3 - Ejercicios Propuestos", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Ejercicio 18", command=self.abrir_ejercicio18).pack(pady=5)
        tk.Button(self, text="Ejercicio 19", command=self.abrir_ejercicio19).pack(pady=5)

    def abrir_ejercicio18(self):
        Ejercicio18GUI(self)

    def abrir_ejercicio19(self):
        Ejercicio19GUI(self)

# Ejercicio 18
class Ejercicio18GUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicio 18 - Empleado")
        self.geometry("400x400")

        tk.Label(self, text="Empleado - Cálculo de Salarios", font=("Arial", 14)).pack(pady=10)

        self.campos = {}
        for campo in ["Código", "Nombre", "Horas Trabajadas", "Valor Hora", "Retención Fuente (%)"]:
            tk.Label(self, text=campo + ":").pack()
            entrada = tk.Entry(self)
            entrada.pack()
            self.campos[campo] = entrada

        tk.Button(self, text="Calcular", command=self.calcular_salarios).pack(pady=10)
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular_salarios(self):
        try:
            codigo = self.campos["Código"].get()
            nombre = self.campos["Nombre"].get()
            horas = float(self.campos["Horas Trabajadas"].get())
            valor_hora = float(self.campos["Valor Hora"].get())
            retencion = float(self.campos["Retención Fuente (%)"].get()) / 100

            salario_bruto = horas * valor_hora
            retencion_total = salario_bruto * retencion
            salario_neto = salario_bruto - retencion_total

            self.resultado.config(
                text=f"Empleado: {nombre} (Código: {codigo})\nSalario Bruto: ${salario_bruto:.2f}\nRetención: ${retencion_total:.2f}\nSalario Neto: ${salario_neto:.2f}"
            )
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Ejercicio 19
class Ejercicio19GUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicio 19 - Triángulo Equilátero")
        self.geometry("400x400")

        tk.Label(self, text="Triángulo Equilátero", font=("Arial", 14)).pack(pady=10)

        tk.Label(self, text="Lado del Triángulo:").pack()
        self.lado = tk.Entry(self)
        self.lado.pack()

        tk.Button(self, text="Calcular Perímetro", command=self.calcular_perimetro).pack(pady=5)
        tk.Button(self, text="Calcular Altura", command=self.calcular_altura).pack(pady=5)
        tk.Button(self, text="Calcular Área", command=self.calcular_area).pack(pady=5)

        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular_perimetro(self):
        try:
            lado = float(self.lado.get())
            perimetro = lado * 3
            self.resultado.config(text=f"Perímetro: {perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido.")

    def calcular_altura(self):
        try:
            lado = float(self.lado.get())
            altura = math.sqrt(lado**2 - (lado / 2)**2)
            self.resultado.config(text=f"Altura: {altura:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido.")

    def calcular_area(self):
        try:
            lado = float(self.lado.get())
            altura = math.sqrt(lado**2 - (lado / 2)**2)
            area = (lado * altura) / 2
            self.resultado.config(text=f"Área: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido.")

#AQUI CREO EL CAPITULO 4


class Capitulo4(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Capítulo 4")
        self.geometry("400x300")

        tk.Label(self, text="Capítulo 4", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Ejercicios Resueltos", command=self.abrir_resueltos).pack(pady=5)
        tk.Button(self, text="Ejercicios Propuestos", command=self.abrir_propuestos).pack(pady=5)

    def abrir_resueltos(self):
        Resueltos(self)

    def abrir_propuestos(self):
        Propuestos(self)


#AQUI CREE LAS VENATNAS DEL CAPITULO 4 PARA LOS EJERCICIOS PROPUESTOS Y RESUELTOS                           
class EjerciciosResueltos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicios Resueltos")
        self.geometry("400x300")
        tk.Label(self, text="Ejercicios Resueltos", font=("Arial", 14)).pack(pady=10)

class EjerciciosPropuestos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicios Propuestos")
        self.geometry("400x300")
        tk.Label(self, text="Ejercicios Propuestos", font=("Arial", 14)).pack(pady=10)

# Ventana de Ejercicios Resueltos
class Resueltos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicios Resueltos")
        self.geometry("400x300")

        tk.Label(self, text="Ejercicios Resueltos", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Ejercicio 7", command=self.ejercicio_7).pack(pady=5)
        tk.Button(self, text="Ejercicio 10", command=self.ejercicio_10).pack(pady=5)

    def ejercicio_7(self):
        Ejercicio7(self)

    def ejercicio_10(self):
        Ejercicio10(self)

# Ventana de Ejercicios Propuestos
class Propuestos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicios Propuestos")
        self.geometry("400x300")

        tk.Label(self, text="Ejercicios Propuestos", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Ejercicio 22", command=self.ejercicio_22).pack(pady=5)
        tk.Button(self, text="Ejercicio 23", command=self.ejercicio_23).pack(pady=5)

    def ejercicio_22(self):
        Ejercicio22(self)

    def ejercicio_23(self):
        Ejercicio23(self)

# Implementación del Ejercicio 7
class Ejercicio7(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicio 7")
        self.geometry("400x300")

        tk.Label(self, text="Comparar dos números", font=("Arial", 14)).pack(pady=10)

        tk.Label(self, text="Número A:").pack()
        self.entry_a = tk.Entry(self)
        self.entry_a.pack()

        tk.Label(self, text="Número B:").pack()
        self.entry_b = tk.Entry(self)
        self.entry_b.pack()

        tk.Button(self, text="Comparar", command=self.comparar).pack(pady=10)

    def comparar(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            mayor = b if a < b else a
            messagebox.showinfo("Resultado", f"El número mayor es: {mayor}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")

# Implementación del Ejercicio 10
class Ejercicio10(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicio 10")
        self.geometry("400x400")

        tk.Label(self, text="Calcular valor de matrícula", font=("Arial", 14)).pack(pady=10)

        tk.Label(self, text="Número de Inscripción:").pack()
        self.entry_ni = tk.Entry(self)
        self.entry_ni.pack()

        tk.Label(self, text="Nombre:").pack()
        self.entry_nom = tk.Entry(self)
        self.entry_nom.pack()

        tk.Label(self, text="Patrimonio:").pack()
        self.entry_pat = tk.Entry(self)
        self.entry_pat.pack()

        tk.Label(self, text="Estrato:").pack()
        self.entry_es = tk.Entry(self)
        self.entry_es.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack(pady=10)

    def calcular(self):
        try:
            ni = self.entry_ni.get()
            nom = self.entry_nom.get()
            pat = float(self.entry_pat.get())
            es = int(self.entry_es.get())
            pagmat = 50000
            if pat > 2000000 and es > 3:
                pagmat += pat * 0.03
            messagebox.showinfo("Resultado", f"Estudiante: {nom} (NI: {ni})\nEl valor de la matrícula es: {pagmat}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Implementación del Ejercicio 22
class Ejercicio22(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicio 22")
        self.geometry("400x400")

        tk.Label(self, text="Calcular salario de trabajador", font=("Arial", 14)).pack(pady=10)

        tk.Label(self, text="Nombre del Trabajador:").pack()
        self.entry_nom = tk.Entry(self)
        self.entry_nom.pack()

        tk.Label(self, text="Salario por hora:").pack()
        self.entry_salh = tk.Entry(self)
        self.entry_salh.pack()

        tk.Label(self, text="Horas trabajadas:").pack()
        self.entry_ht = tk.Entry(self)
        self.entry_ht.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack(pady=10)

    def calcular(self):
        try:
            nom = self.entry_nom.get()
            salh = float(self.entry_salh.get())
            ht = float(self.entry_ht.get())
            salario = salh * ht
            messagebox.showinfo("Resultado", f"Trabajador: {nom}\nEl salario es: {salario}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Implementación del Ejercicio 23
class Ejercicio23(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicio 23")
        self.geometry("400x300")

        tk.Label(self, text="Resolver ecuación cuadrática", font=("Arial", 14)).pack(pady=10)

        tk.Label(self, text="Coeficiente a:").pack()
        self.entry_a = tk.Entry(self)
        self.entry_a.pack()

        tk.Label(self, text="Coeficiente b:").pack()
        self.entry_b = tk.Entry(self)
        self.entry_b.pack()

        tk.Label(self, text="Coeficiente c:").pack()
        self.entry_c = tk.Entry(self)
        self.entry_c.pack()

        tk.Button(self, text="Resolver", command=self.resolver).pack(pady=10)

    def resolver(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())
            discriminante = (b ** 2) - (4 * a * c)

            if discriminante < 0:
                resultado = "No tiene soluciones reales"
            elif discriminante > 0:
                raiz = math.sqrt(discriminante)
                x1 = (-b + raiz) / (2 * a)
                x2 = (-b - raiz) / (2 * a)
                resultado = f"La ecuación tiene 2 soluciones: X1 = {x1} y X2 = {x2}"
            else:
                x = -b / (2 * a)
                resultado = f"La ecuación tiene una única solución: X = {x}"

            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "El coeficiente 'a' no puede ser cero.")

#AQUI ESTA LA PARTE DE LA ACTIVIDAD DE LAS FIGURAS


class FigurasGeometricas(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Figuras Geométricas")
        self.geometry("400x300")
        tk.Label(self, text="Figuras Geométricas", font=("Arial", 14)).pack(pady=10)

        tk.Button(self, text="Círculo", command=self.abrir_circulo).pack(pady=5)
        tk.Button(self, text="Rectángulo", command=self.abrir_rectangulo).pack(pady=5)
        tk.Button(self, text="Cuadrado", command=self.abrir_cuadrado).pack(pady=5)
        tk.Button(self,text="Rombo", command=self.abrir_rombo).pack(pady=5)
        tk.Button(self,text="Trapecio",command=self.abrir_trapecio).pack(pady=5)

    def abrir_circulo(self):
        CirculoGUI(self)

    def abrir_rectangulo(self):
        RectanguloGUI(self)
    
    def abrir_cuadrado(self):
        CuadradoGUI(self)
    
    def abrir_rombo(self):
        RomboGUI(self)
    
    def abrir_trapecio(self):
        TrapecioGUI(self)


class CirculoGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Círculo")
        self.geometry("400x300")
        tk.Label(self, text="Cálculo del Círculo", font=("Arial", 14)).pack(pady=10)

        tk.Label(self, text="Radio:").pack()
        self.radio = tk.Entry(self)
        self.radio.pack()

        tk.Button(self, text="Calcular Área", command=self.calcular_area).pack(pady=5)
        tk.Button(self, text="Calcular Perímetro", command=self.calcular_perimetro).pack(pady=5)

        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular_area(self):
        try:
            radio = float(self.radio.get())
            area = math.pi * radio**2
            self.resultado.config(text=f"Área: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido.")

    def calcular_perimetro(self):
        try:
            radio = float(self.radio.get())
            perimetro = 2 * math.pi * radio
            self.resultado.config(text=f"Perímetro: {perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido.")

# Clase para manejar cálculos del rectángulo
class RectanguloGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Rectángulo")
        self.geometry("400x300")
        tk.Label(self, text="Cálculo del Rectángulo", font=("Arial", 14)).pack(pady=10)

        tk.Label(self, text="Base:").pack()
        self.base = tk.Entry(self)
        self.base.pack()

        tk.Label(self, text="Altura:").pack()
        self.altura = tk.Entry(self)
        self.altura.pack()

        tk.Button(self, text="Calcular Área", command=self.calcular_area).pack(pady=5)
        tk.Button(self, text="Calcular Perímetro", command=self.calcular_perimetro).pack(pady=5)

        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular_area(self):
        try:
            base = float(self.base.get())
            altura = float(self.altura.get())
            area = base * altura
            self.resultado.config(text=f"Área: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

    def calcular_perimetro(self):
        try:
            base = float(self.base.get())
            altura = float(self.altura.get())
            perimetro = 2 * (base + altura)
            self.resultado.config(text=f"Perímetro: {perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
            
class CuadradoGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cuadrado")
        self.geometry("400x300")
        tk.Label(self, text="Cálculo del Cuadrado", font=("Arial", 14)).pack(pady=10)

        tk.Label(self, text="Lado:").pack()
        self.lado = tk.Entry(self)
        self.lado.pack()
        
        tk.Button(self, text="Calcular Área", command=self.calcular_area).pack(pady=5)
        tk.Button(self, text="Calcular Perímetro", command=self.calcular_perimetro).pack(pady=5)

        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular_area(self):
        try:
            lado = float(self.lado.get())
            area = lado ** 2
            self.resultado.config(text=f"Área: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

    def calcular_perimetro(self):
        try:
            lado = float(self.lado.get())
            perimetro = 4 * lado
            self.resultado.config(text=f"Perímetro: {perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

class RomboGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Rombo")
        self.geometry("400x300")
        tk.Label(self, text="Cálculo del Rombo", font=("Arial", 14)).pack(pady=10)

        tk.Label(self, text="Lado:").pack()
        self.lado = tk.Entry(self)
        self.lado.pack()
        
        tk.Label(self, text="Diagonal mayor").pack()
        self.Diagonal_mayor = tk.Entry(self)
        self.Diagonal_mayor.pack()
        
        tk.Label(self, text="Diagonal menor").pack()
        self.Diagonal_menor = tk.Entry(self)
        self.Diagonal_menor.pack()

        tk.Button(self, text="Calcular Área", command=self.calcular_area).pack(pady=5)
        tk.Button(self, text="Calcular Perímetro", command=self.calcular_perimetro).pack(pady=5)
        
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()
    
    def calcular_area(self):
        try:
            DiagM = float(self.Diagonal_mayor.get())
            Diagm = float(self.Diagonal_menor.get())
            area = (DiagM * Diagm) / 2
            self.resultado.config(text=f"Área: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
        
    def calcular_perimetro(self):
        try:
            Lado = float(self.lado.get())
            Perimetro = Lado * 4
            self.resultado.config(text=f"Perímetro: {Perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")


class TrapecioGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Trapecio")
        self.geometry("400x300")
        tk.Label(self, text="Cálculo del Trapecio", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self,text="Base mayor").pack()
        self.Base_mayor = tk.Entry(self)
        self.Base_mayor.pack()
        
        tk.Label(self,text="Base menor").pack()
        self.Base_menor = tk.Entry(self)
        self.Base_menor.pack()
        
        tk.Label(self,text="Lado").pack()
        self.lado = tk.Entry(self)
        self.lado.pack()
        
        tk.Label(self,text="Altura").pack()
        self.altura = tk.Entry(self)
        self.altura.pack()
        
        tk.Button(self, text="Calcular Área", command=self.calcular_area).pack(pady=5)
        tk.Button(self, text="Calcular Perímetro", command=self.calcular_perimetro).pack(pady=5)
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()
    
    
    def calcular_area(self):
        try:
            BaM = float(self.Base_mayor.get())
            Bam = float(self.Base_menor.get())
            altura = float(self.altura.get())
            area = ((BaM + Bam) * altura) / 2
            self.resultado.config(text=f"Área: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
    
    
    def calcular_perimetro(self):
        try:
            BaM = float(self.Base_mayor.get())
            Bam = float(self.Base_menor.get())
            Lado = float(self.lado.get())
            perimetro = (BaM + Bam) * (2 * Lado)
            self.resultado.config(text=f"Perímetro: {perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
        
        
# ============================================
# Iniciar la aplicación
# ============================================
if __name__ == "__main__":
    app = MenuPrincipal()
    app.mainloop()