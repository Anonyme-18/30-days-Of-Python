# Statistics Class
class Statistics:
    def __init__(self, data_list):
        self.data = sorted(data_list)  # Sorting helps with median and other operations

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def data_range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        number_of_values = self.count()
        middle_index = number_of_values // 2
        if number_of_values % 2 == 0:
            return (self.data[middle_index - 1] + self.data[middle_index]) / 2
        else:
            return self.data[middle_index]

    def mode(self):
        frequency_map = {}
        for value in self.data:
            frequency_map[value] = frequency_map.get(value, 0) + 1
        mode_value = max(frequency_map, key=frequency_map.get)
        return mode_value, frequency_map[mode_value]

    def variance(self):
        mean_value = self.mean()
        return round(sum((x - mean_value) ** 2 for x in self.data) / self.count(), 1)

    def std_dev(self):
        return round(self.variance() ** 0.5, 1)

    def freq_dist(self):
        frequency_map = {}
        for value in self.data:
            frequency_map[value] = frequency_map.get(value, 0) + 1
        # Sort by frequency descending
        return sorted([(freq / self.count() * 100, value) for value, freq in frequency_map.items()], reverse=True)

    def describe(self):
        print("Count:", self.count())
        print("Sum:", self.sum())
        print("Min:", self.min())
        print("Max:", self.max())
        print("Range:", self.data_range())
        print("Mean:", self.mean())
        print("Median:", self.median())
        print("Mode:", self.mode())
        print("Variance:", self.variance())
        print("Standard Deviation:", self.std_dev())
        print("Frequency Distribution:", self.freq_dist())


# Example usage
ages_list = [
    31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
    33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26
]

statistics_instance = Statistics(ages_list)
print("Statistics Summary:")
statistics_instance.describe()

# PersonAccount Class
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []  # list of tuples (description, amount)
        self.expenses = []  # list of tuples (description, amount)

    def add_income(self, description, amount):
        self.incomes.append((description, amount))

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))

    def total_income(self):
        return sum(amount for _, amount in self.incomes)

    def total_expense(self):
        return sum(amount for _, amount in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print(f"\nAccount Info for {self.firstname} {self.lastname}")
        print("Incomes:")
        for income_description, income_amount in self.incomes:
            print(f"  + {income_description}: {income_amount}")
        print("Expenses:")
        for expense_description, expense_amount in self.expenses:
            print(f"  - {expense_description}: {expense_amount}")
        print(f"Total Income: {self.total_income()}")
        print(f"Total Expense: {self.total_expense()}")
        print(f"Account Balance: {self.account_balance()}")


# Example usage
account_holder = PersonAccount("John", "Doe")
account_holder.add_income("Salary", 3000)
account_holder.add_income("Freelance", 800)
account_holder.add_expense("Rent", 1200)
account_holder.add_expense("Groceries", 400)

account_holder.account_info()
