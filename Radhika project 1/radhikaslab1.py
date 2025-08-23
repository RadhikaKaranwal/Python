from gc import get_count
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # For heatmap
print(" Employee Data Analysis Report\n")

# 1. Load the CSV file
df = pd.read_csv('employee_data.csv', sep='\t')  # Replace with the actual file path
print(" First 5 rows of the dataset:")
print(df.head())

# 2. Basic Data Summary
print("\n Summary Statistics:")
print(df.describe())

# 3. Calculate average of a selected column
selected_column = 'Salary'  # Change this to your column name
if selected_column in df.columns:
    average_value = df[selected_column].mean()
    print(f"\n Average {selected_column}: {average_value:.2f}")
else:
    print(f"\n Column '{selected_column}' not found.")

# 4. Bar Chart: Count of categories (e.g., Department-wise)
if 'Department' in df.columns:
    dept_counts = df['Department'].value_counts()
    plt.figure(figsize=(8, 5))
    dept_counts.plot(kind='bar', color='skyblue')
    plt.title('Employee Count per Department')
    plt.xlabel('Department')
    plt.ylabel('Count')
    plt.tight_layout()  
    plt.savefig('department_count.png')
    plt.show()

# 5. Scatter Plot: Salary vs Experience
if {'Experience', 'Salary'}.issubset(df.columns):
    plt.figure(figsize=(8, 5))
    plt.scatter(df['Experience'], df['Salary'], alpha=0.6, c='green')
    plt.title('Salary vs Experience')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('salary_vs_experience.png')
    plt.show()

# 6. Heatmap: Correlation matrix
plt.figure(figsize=(10, 7))
corr = df.corr(numeric_only=True)  # Only numeric columns
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.show()

# 7. Insights and Observations
print("\n Insights and Observations:")

# Insight 1: Average Salary
if selected_column in df.columns:
    print(f"• The average salary of employees is ₹{average_value:.2f}.")

# Insight 2: Largest Department
if 'Department' in df.columns:
    largest_dept = df['Department'].value_counts().idxmax()
    count = df['Department'].value_counts().max()
    print(f"• The largest department is '{largest_dept}' with {count} employees.")

# Insight 3: Salary vs Experience Trend
if {'Experience', 'Salary'}.issubset(df.columns):
    print("• Scatter plot shows that salary tends to increase with experience, indicating a possible positive correlation.")

# Insight 4: Features Most Correlated with Salary
corr = df.corr(numeric_only=True)
if 'Salary' in corr.columns:
    salary_corr = corr['Salary'].drop('Salary').sort_values(ascending=False)
    print("• Features most positively correlated with Salary:")
    for feature, value in salary_corr.head(3).items():

        print(f"   - {feature}: Correlation = {value:.2f}")
