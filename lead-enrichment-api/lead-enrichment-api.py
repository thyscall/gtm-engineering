import argparse
import requests

def mktg_enrich():


    # 1. Accepts arguments: Accepts a --department argument from the command line (e.g., "Engineering", "Marketing", "Sales").

    parser = argparse.ArgumentParser(description="Lead Enrichment API")
    parser.add_argument("--department", required=True, nargs='+')           # nargs='+ allows for 1+ arguments, CLI: --department sales accounting engineering
    args = parser.parse_args()

    # 2. Fetches the user database from this public mock API: https://dummyjson.com/users?limit=100
    api_url = "https://dummyjson.com/users?limit=100"
    target_depts = [d.lower() for d in args.department]

    # 3. Filters the API response to only include users where their company.department 
    # matches the user's CLI argument 
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        leads = data.get("users",[])
        qual_leads = []
        qual_leads_count = 0
        total_age = 0

        for lead in leads:

            company = lead.get("company",{})
            department = company.get("department",{}).lower()

            if department in target_depts:

                firstName = lead.get("firstName","Unknown")
                lastName = lead.get("lastName","Unknown")
                email = lead.get("email",{})
                age = lead.get("age", 0)
                title = company.get("title", "Unknown")
                department = company.get("department", "Unknown")

                qual_leads.append({
                    'name': f'{firstName} {lastName}', 
                    'email': email,
                    'age': age,
                    'title': title,
                    'department': department
                })

                total_age += age

                qual_leads_count += 1


        # 5. Prints a summary: Prints a clear, formatted summary to the terminal that includes:
        # The requested department name.
        # The total number of leads found.
        # The average age of those leads (rounded to 1 decimal place).
        # A table displaying the First/Last Name, Email, and Job Title of the matched leads.
        if not qual_leads:
                print(f'No matching leads found for {department}')
        else:
            formatted_depts = ", ".join(target_depts).upper()
            print(f'Marketing Leads for: {formatted_depts}')
            print('-' * 125)
            print(f'Total Number of Leads Found: {qual_leads_count}')
            print(f'Average Age: {total_age/qual_leads_count:.1f}')
            print('-' * 125)
            print(f"{'Name':<25} | {'Email':<40} | {'Title':<30} | Department")            
            print('-' * 125)

            qual_leads.sort(key=lambda x: x['department'])
            for lead in qual_leads:
                print(f"{lead['name']:<25} | {lead['email']:<40} | {lead['title']:<30} | {lead['department']:<25}")

            print('-' * 125)

        
    except requests.exceptions.RequestException as e:
        print(f'Not able to fetch API. Details: {e}')
    except Exception as e:
        print(f'System Error: {e}')


if __name__ == "__main__":
    mktg_enrich()

