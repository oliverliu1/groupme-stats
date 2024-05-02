import pandas as pd

NUMBER_OF_LEADERS = 10

# Load the CSV file into a DataFrame
csv_file_path = 'analysis.csv'
data = pd.read_csv(csv_file_path)

# Define the categories
categories = ['Number of Messages', 'Number of Words', 'Number of Likes',
              'Average Likes per Message', 'Self Likes', 'Total Likes Given']

# Open a text file to write the results
with open('category_leaders.txt', 'w') as file:
    for category in categories:
        # Sort data by the current category in descending order
        sorted_data = data.sort_values(by=category, ascending=False).head(NUMBER_OF_LEADERS)
        
        # Write the category header and the top 10 results to the file
        file.write(f"Top {NUMBER_OF_LEADERS} for {category}:\n")
        file.write("-" * 30 + "\n")
        
        # Extract the formatted header and data
        formatted_data = sorted_data[['Author', category]].to_string(index=False, header=True)
        formatted_data = formatted_data.split('\n')
        
        # Headers and rows
        headers = formatted_data[0].split(maxsplit=1)  # Split only once
        rows = [line.strip() for line in formatted_data[1:]]
        
        # Determine the maximum lengths for author names and values
        max_value_len = max(len(line.split()[-1]) for line in rows)
        max_name_len = max(len(" ".join(line.split()[:-1])) for line in rows)
        
        # Format and write the headers
        file.write(f"{headers[1].rjust(max_value_len)} {headers[0].ljust(max_name_len)}\n")
        file.write("-" * 30 + "\n")
        
        # Format and write each row
        for row in rows:
            parts = row.split()
            value = parts[-1]  # Last part is the number
            author = " ".join(parts[:-1])  # Rest is the author name
            file.write(f"{value.rjust(max_value_len)} {author.ljust(max_name_len)}\n")
        
        file.write("-" * 30 + "\n\n\n\n")  # Add space between categories

print(f"Top {NUMBER_OF_LEADERS} results have been written to 'category_leaders.txt'")
