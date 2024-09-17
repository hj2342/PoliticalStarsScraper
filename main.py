import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/india/from-kangana-to-kirron-kher-actors-who-joined-politics-lok-sabha-elections-2024-amitabh-bachchan-jaya-sunny-deol-hema-malini/photostory/108789366.cms?picid=108789426"

try:

    response = requests.get(url)
    response.raise_for_status()  
    
    # Parsing the page content 
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Lists to hold actor names and their descriptions
    actor_list = []
    descriptions = []

    # Find all 'h2' tags, they contain actor names
    headings = soup.find_all('h2')
    for heading in headings:
        # removing the unwanted content
        actor_name = heading.get_text().strip()
        if actor_name and actor_name != 'TOI':
            actor_list.append(actor_name)
        # Limiting the number of actors to 10
            if len(actor_list) >= 10:
                break

    # Find all 'p' tags, they contain actor descriptions
    descriptions_tags = soup.find_all('p')
    for desc_tag in descriptions_tags:
      # removing the unwanted content
        desc = desc_tag.get_text().strip()
        if desc:
            descriptions.append(desc)
    
  # Limiting the number of descriptions to the number of actors
    descriptions = descriptions[:len(actor_list)]

# Displaying actors
    print("\nActor Politicians in India:")
    for i, actor in enumerate(actor_list, 1):
        print(f"{i}. {actor}")

   # User input for actor number
    actor_num = int(input("\nEnter the number of the actor you want to know more about: "))
    
    # Checking if the input is valid
    if 1 <= actor_num <= len(actor_list):
      # printing the selected actor name
        selected_actor = actor_list[actor_num - 1]
        print(f"\nSelected Actor: {selected_actor}")
        
      # printing the corresponding description
        if actor_num <= len(descriptions):
            print(f"Description: {descriptions[actor_num - 1]}\n")
        else:
            print("No description available for this actor.")
    else:
        print("Invalid actor number.")

except requests.RequestException as e:
    print(f"An error occurred while fetching the webpage: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")