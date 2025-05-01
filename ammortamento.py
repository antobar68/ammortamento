
import matplotlib.pyplot as plt

def calcola_ammortamento(capitale, tasso_annuo, anni, frequenza=12):
    n = anni * frequenza
    i = (tasso_annuo / 100) / frequenza
    rata = capitale * (i * (1 + i) ** n) / ((1 + i) ** n - 1)

    residuo = capitale
    tabella = []

    for k in range(1, n + 1):
        interesse = residuo * i
        quota_capitale = rata - interesse
        residuo -= quota_capitale
        tabella.append({
            'Rata': k,
            'Quota Capitale': round(quota_capitale, 2),
            'Quota Interessi': round(interesse, 2),
            'Rata Totale': round(rata, 2),
            'Residuo': round(max(residuo, 0), 2)
        })

    return tabella

def stampa_tabella(tabella):
    print(f"{'Rata':<5} {'Quota Capitale':<15} {'Quota Interessi':<15} {'Rata Totale':<12} {'Residuo':<10}")
    for r in tabella:
        print(f"{r['Rata']:<5} {r['Quota Capitale']:<15} {r['Quota Interessi']:<15} {r['Rata Totale']:<12} {r['Residuo']:<10}")

def plot_residuo(tabella):
    x = [r['Rata'] for r in tabella]
    y = [r['Residuo'] for r in tabella]
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o')
    plt.title('Capitale Residuo nel Tempo')
    plt.xlabel('Numero Rata')
    plt.ylabel('Residuo (€)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Esempio d'uso
if __name__ == '__main__':
    capitale = float(input("Inserisci il capitale (€): "))
    tasso = float(input("Inserisci il tasso di interesse annuo (%): "))
    anni = int(input("Inserisci la durata del prestito (anni): "))
    freq = int(input("Inserisci la frequenza delle rate (12 = mensile, 4 = trimestrale): "))

    tabella = calcola_ammortamento(capitale, tasso, anni, freq)
    stampa_tabella(tabella)
    plot_residuo(tabella)
