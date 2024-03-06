import os

# Define the banner
def display_banner():
    banner = """
 oooooo     oooo ooooo   .oooooo.    ooooo ooooo            ooooooo  ooooo 
 `888.     .8'  `888'  d8P'  `Y8b   `888' `888'             `8888    d8'  
  `888.   .8'    888  888            888   888                Y888..8P    
   `888. .8'     888  888            888   888                 `8888'     
    `888.8'      888  888     ooooo  888   888                .8PY888.    
     `888'       888  `88.    .88'   888   888       o .o.   d8'  `888b   
      `8'       o888o  `Y8bood8P'   o888o o888ooooood8 Y8P o888o  o88888o 
                                                                                 
TOOL BY Yogendra SINGH & SAI PRAKASH & LAV SHARMA
DESIGNED BY YOGENDRA FAUJDAR
  """  
    print(banner)

# Define the repositories and their respective URLs
repositories = {
    'domain-lookup': 'https://github.com/yogi612/domain-lookup.git',
    'Port-Scanning ': 'https://github.com/yogi612/Port-Scanning.git',
    'VIGIL.X' :'https://github.com/yogi612/VIGIL.X.git',
}

# Function to clone and install a repository
def clone_and_install(repo_name, repo_url):
    print(f"Cloning {repo_name} repository from {repo_url}")
    os.system(f'git clone {repo_url}')

    # Check if an 'install.sh' script exists
    if os.path.exists(f"{repo_name}/install.sh"):
        print(f"Running 'install.sh' for {repo_name}")
        os.system(f'cd {repo_name} && chmod +x install.sh && ./install.sh')
    else:
        # Check if a .py file exists
        py_file = [file for file in os.listdir(repo_name) if file.endswith(".py")]
        if py_file:
            print(f"Running {py_file[0]} for {repo_name}")
            os.system(f'python {repo_name}/{py_file[0]}')

if __name__ == "__main__":
    display_banner()  # Add this line to display the banner

    print("Choose a Tool to install:")
    for i, repo_name in enumerate(repositories.keys(), start=1):
        print(f"{i}. {repo_name}")

    choice = input("Enter the number of the Tool: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(repositories):
            repo_name = list(repositories.keys())[choice - 1]
            repo_url = list(repositories.values())[choice - 1]
            clone_and_install(repo_name, repo_url)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")
