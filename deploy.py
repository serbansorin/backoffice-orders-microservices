import os
import sys

# Define the root directory where the folders are located
root_directory = os.getcwd()
# Get a list of all subdirectories in the root directory
subdirectories = [os.path.join(root_directory, name) for name in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, name)) and name != '.git' and name != 'client']

def build_client():
    pass
 
def build():
    os.system('npm run build')

def git_status_check():
     # Change the current working directory to the subdirectory
    if os.system('git status') == 0:
        print("Everything is up to date")
        return 1
    else:
        print("Something is not up to date")
        return 0

def git_sync():
    os.system('git push && git pull')

def git_commit():
    if git_status_check() == 0:
        os.system('git add . && git commit -m "Auto commit"')

def npm_sync():
    pass


# TODO: need to work with docker
def deploy():
    Check command line arguments
    if len(sys.argv) < 2:
        print("Please provide a valid deploy option:")
        # deploy_option = input()
        return
    
    # Get the deploy option
    deploy_option = len(sys.argv) != 2 or sys.argv[1]

    print(deploy_option, '\n')
    # Deploy based on the option
    for subdirectory in subdirectories:
        os.chdir(subdirectory)  # Change the current working directory to the subdirectory
        print(os.getcwd())
        os.chdir(root_directory)
        print(os.getcwd())

        continue
        # deploy options
        if deploy_option == "--push":
            git_commit()
            git_sync()
            
        elif deploy_option == "--stash-change":
            os.system('git stash')
            git_sync()
            
        elif deploy_option == "--go-live":
            # git_sync()
            print('--go-live is not implemented yet, Thank you!! please try again')
            return
        # option only install
        elif deploy_option == "--npm-install" or deploy_option == "--npm-i":
            os.system('npm install')
            
        elif deploy_option == "--sync-start":
            os.system('npm install && npm start')
            os.system('npm start')
            
        elif deploy_option == "--all":
            git_commit()
            git_sync()
            os.system('npm install && npm start')

        elif deploy_option == 'start':
            os.system('npm start')

        else:
            print('No available option')
            return
        os.chdir(root_directory)


if __name__ == "__main__":
    deploy()

