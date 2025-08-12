class Statistics:
    def __init__(self, data):
        self.data = sorted(data)

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count(), 1)

    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]

    def mode(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1
        max_count = max(freq.values())
        mode_val = [k for k, v in freq.items() if v == max_count][0]
        return {"mode": mode_val, "count": max_count}

    def var(self):
        mean_val = self.mean()
        return round(sum((x - mean_val) ** 2 for x in self.data) / self.count(), 1)

    def std(self):
        return round(self.var() ** 0.5, 1)

    def freq_dist(self):
        return


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
        33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count()) 
print('Sum: ', data.sum()) 
print('Min: ', data.min()) 
print('Max: ', data.max()) 
print('Range: ', data.range()) 
print('Mean: ', data.mean()) 
print('Median: ', data.median()) 
print('Mode: ', data.mode()) 
print('Standard Deviation: ', data.std()) 
print('Variance: ', data.var()) 
print('Frequency Distribution: ', data.freq_dist())


# Exercises: Level 2
# 1. Create a class called PersonAccount. It has firstname, lastname, incomes,
# expenses properties and it has total_income, total_expense, account_info,
# add_income, add_expense and account_balance methods. Incomes is a set
# of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def total_income(self):
        return sum(sum(mont) for mont in self.incomes.values())

    def total_expense(self):
        return sum(sum(mont) for mont in self.expenses.values())
    
    def account_info(self):
        info = f"Cher client, {self.lastname} {self.firstname},\n"
        info += f"vous avez effectué au total {self.total_expense()} de depenses et {self.total_income()} d'entrées\n"
        info += f"votre solde actuel est de {self.account_balance()}"
        return info
    
    def add_income(self, desc, mont):
        if desc not in self.incomes:
            self.incomes[desc] = []
        self.incomes[desc].append(mont)

        return "depot effectué avec succès"
    
    def add_expense(self, desc, mont):
        if desc not in self.expenses:
            self.expenses[desc] = []
        self.expenses[desc].append(mont)

        return "retrait effectué avec succès"

    def account_balance(self):
        return self.total_income() - self.total_expense()
    
client = PersonAccount("John", "Doe")

client.add_income("Salaire", 200)
client.add_income("Service", 1000)
client.add_expense("Fee food", 1200)
client.add_expense("Dons", 100)
print(client.account_info())
