import numpy as np
from tabulate import tabulate  # Install via: pip install tabulate

def input_matrix(name):
    print(f"\n Enter values for Matrix {name}")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print(f"Enter the values row-wise (space separated):")

    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").strip().split()))
        if len(row) != cols:
            print("Column count doesn't match. Try again.")
            return input_matrix(name)
        matrix.append(row)

    return np.array(matrix)

def display_matrix(matrix, label="Result"):
    print(f"\n {label} ({matrix.shape[0]}x{matrix.shape[1]}):")
    print(tabulate(matrix, tablefmt="fancy_grid"))

def menu():
    print("\n Matrix Operations Tool")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix")
    print("5. Determinant of Matrix")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = input("\n Enter your choice (1-6): ")

        if choice in ['1', '2', '3']:
            A = input_matrix("A")
            B = input_matrix("B")

            try:
                if choice == '1':
                    if A.shape != B.shape:
                        print(" Matrices must have the same dimensions for addition.")
                    else:
                        result = A + B
                        display_matrix(A, "Matrix A")
                        display_matrix(B, "Matrix B")
                        display_matrix(result, "A + B")

                elif choice == '2':
                    if A.shape != B.shape:
                        print(" Matrices must have the same dimensions for subtraction.")
                    else:
                        result = A - B
                        display_matrix(A, "Matrix A")
                        display_matrix(B, "Matrix B")
                        display_matrix(result, "A - B")

                elif choice == '3':
                    if A.shape[1] != B.shape[0]:
                        print(" Columns of A must equal rows of B for multiplication.")
                    else:
                        result = np.dot(A, B)
                        display_matrix(A, "Matrix A")
                        display_matrix(B, "Matrix B")
                        display_matrix(result, "A × B")
            except ValueError as e:
                print(" Error:", e)

        elif choice == '4':
            A = input_matrix("A")
            result = A.T
            display_matrix(A, "Matrix A")
            display_matrix(result, "Transpose of A")

        elif choice == '5':
            A = input_matrix("A")
            if A.shape[0] != A.shape[1]:
                print(" Determinant can only be calculated for square matrices.")
            else:
                det = np.linalg.det(A)
                display_matrix(A, "Matrix A")
                print(f"\n Determinant: {det:.4f}")

        elif choice == '6':
            print(" Exiting. Thank you!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
