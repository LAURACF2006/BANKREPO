class Cuenta: 
    def __init__(self, bank_account, balance=100):
        """
        Inicializa la cuenta bancaria con un número de cuenta y un saldo inicial.
        """
        self.bank_account = bank_account  
        self.balance = balance  

    def operaciones(self):
        """
        Muestra el menú de operaciones al usuario y llama a los métodos según su elección.
        """
        while True:
            try:
                opcion = int(input('''
        ------------------------------------------
        POR FAVOR INDIQUE QUE OPERACIÓN DESEA REALIZAR..
        1. CONSULTAR BALANCE
        2. DEPÓSITO A CUENTA
        3. RETIRO DE EFECTIVO
        4. SALIR
        Opción: '''))
                
                if opcion == 1:
                    print(f"Su balance actual es de: {self.get_balance()}€")
                elif opcion == 2:
                    cantidad = int(input("Introduzca la cantidad a depositar: "))
                    self.deposito(cantidad)
                elif opcion == 3:
                    cantidad = int(input("Introduzca la cantidad a retirar: "))
                    self.retirar(cantidad)
                elif opcion == 4:
                    self.salir()
                    break
                else:
                    print("Lo sentimos, opción no válida. Intente de nuevo.")
            except ValueError:
                print("Por favor, introduzca un número válido para la opción.")
    
    def deposito(self, cantidad):
        """
        Realiza un depósito si la cantidad es positiva.
        """
        if cantidad > 0:
            self.balance += cantidad
            print(f"Se han depositado {cantidad}€. Su balance actual es de: {self.balance}€")
        else:
            print("Por favor, introduzca una cantidad positiva para depositar.")
    
    def retirar(self, cantidad):
        """
        Realiza un retiro si la cantidad es positiva y hay suficiente saldo.
        """
        if cantidad > 0:
            if self.balance >= cantidad:
                self.balance -= cantidad  
                print(f"Se han retirado {cantidad}€. Su balance actual es de: {self.balance}€")
            else:
                print(f"Fondos insuficientes. Su balance actual es de: {self.balance}€")
        else:
            print("Por favor, introduzca una cantidad positiva para retirar.")

    def get_balance(self): 
        """
        Devuelve el balance actual de la cuenta.
        """
        return self.balance

    def salir(self):
        """
        Muestra un mensaje de despedida al usuario.
        """
        print("Gracias por su visita.")


