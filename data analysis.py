import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                  Results of Lok Sabha Elections                   ") 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

url = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Find tables with election results
tables = soup.find_all('table')

#Extract headers
headers = soup.find_all('th')[0:4]
headers = [ele.text.strip() for ele in headers]


# Extract data into a DataFrame
data = []
for table in tables:
    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)
df = pd.DataFrame(data, columns=headers)
df.to_csv('/Users/manojkumar/Documents/data_analysis/lok_sabha_results.csv', index=False)

df = pd.read_csv('/Users/manojkumar/Documents/data_analysis/lok_sabha_results.csv')
df.dropna(inplace=True)
df.columns = df.columns.str.strip()

# Plot pie chart of party-wise vote share
plt.figure(figsize=(10, 8))
plt.pie(df['Won'], startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Party-wise Vote Share')
plt.show()


# Define a color palette
colors = plt.cm.tab20.colors
# Plot pie chart of party-wise vote share
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(df['Won'], autopct='%1.1f%%', startangle=140, colors=colors)

# Add a legend with party names and corresponding colors
plt.legend(wedges, df['Party'], title="Parties", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Party-wise Vote Share')
plt.savefig('party_wise_vote_share.png')
plt.show()




while True:
    print()
    print("10 Key Insights:-")
    print()
    print("1. Total Seats in Lok Sabha")
    print("2. Party with Most Seats Won")
    print("3. Top 5 States by Number of Seats Won")
    print("4. Party with Highest Vote Share Percentage")
    print("5. Closest Contested Seat")
    print("6. State with Highest Voter Turnout")
    print("7. Top 5 Parties by Vote Share Percentage")
    print("8. Number of Parties with More than 10 Seats")
    print("9. Number of First-Time MPs")
    print("10. Percentage of Women MPs")
    print("Enter 0 for exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        total_seats = df['Total'].astype(int).sum()
        print(total_seats)
        
    elif choice == 2:
        most_seats_won_party = df.loc[df['Won'].astype(int).idxmax()]['Party']
        print(most_seats_won_party)
        
    elif choice == 3:
        top_5_states_seats = df.groupby('State')['Won'].sum().sort_values(ascending=False).head(5)
        print(top_5_states_seats)
        
    elif choice == 4:
        highest_vote_share_party = vote_share_df.loc[vote_share_df['Vote Share'].idxmax()]['Party']
        print(highest_vote_share_party)
        
    elif choice == 5:
        closest_contest = df.loc[(df['Winning Margin'].astype(int)).idxmin()]
        print(closest_contest)
        
    elif choice == 6:
        highest_turnout_state = turnout_df.loc[turnout_df['Turnout'].idxmax()]['State']
        print(highest_turnout_state)
        
    elif choice == 7:
        top_5_parties_vote_share = vote_share_df[['Party', 'Vote Share']].sort_values(by='Vote Share', ascending=False).head(5)
        print(top_5_parties_vote_share)
        
    elif choice == 8:
        parties_more_than_10_seats = df[df['Won'].astype(int) > 10]['Party'].nunique()
        print(parties_more_than_10_seats)
        
    elif choice == 9:
        first_time_mps = df[df['First Time MP'] == True].shape[0]
        print(first_time_mps)
        
    elif choice == 10:
        total_mps = df.shape[0]
        women_mps = df[df['Gender'] == 'F'].shape[0]
        percentage_women_mps = (women_mps / total_mps) * 100
        print(percentage_women_mps)
        
    elif choice == 0:
        print()
        print()
        print("***************THANK YOU***************")
        break

    else:
        print("ENTER A VALID NUMBER!!!")
        print()
        print()
        print()
