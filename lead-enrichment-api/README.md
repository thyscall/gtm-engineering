# Macro-Trend Signal Engine

This is a routing tool that pulls raw lead data from a marketing enrichment API. 
The SDRs need a quick way to pull leads by department, 
see the average age of the leads, and get a clean list of contacts.


This Python CLI tool that does the following:

1. Accepts arguments: Accepts a --department argument from the command line (e.g., "Engineering", "Marketing", "Sales").

2. Retrieves information: Fetches the user database from this public mock API: https://dummyjson.com/users?limit=100

3. Processes data: Filters the API response to only include users where their company.department matches the user's CLI argument (ensure this is case-insensitive).

4. Calculates the Average Age of the matched leads.

5. Prints a summary: Prints a clear, formatted summary to the terminal that includes:
The requested department name.
The total number of leads found.
The average age of those leads (rounded to 1 decimal place).
A table displaying the First/Last Name, Email, and Job Title of the matched leads.

EXAMPLE RUN
python3 lead-enrichment-api.py --department sales
Marketing Leads for: SALES
-----------------------------------------------------------------------------------------------------------------------------
Total Number of Leads Found: 5
Average Age: 32.8
-----------------------------------------------------------------------------------------------------------------------------
Name                      | Email                                    | Title                          | Department
-----------------------------------------------------------------------------------------------------------------------------
Chloe Morales             | chloe.morales@x.dummyjson.com            | Database Administrator         | Sales                    
Nathan Dixon              | nathan.dixon@x.dummyjson.com             | Engineer                       | Sales                    
Austin Hudson             | austin.hudson@x.dummyjson.com            | Legal Counsel                  | Sales                    
Aubrey Wagner             | aubrey.wagner@x.dummyjson.com            | Engineer                       | Sales                    
Scarlett Bowman           | scarlett.bowman@x.dummyjson.com          | Software Engineer              | Sales                    
-----------------------------------------------------------------------------------------------------------------------------
