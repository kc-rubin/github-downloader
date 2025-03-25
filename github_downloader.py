import subprocess
import os

def github_downloader(repo_url, destination_path, folders):
    try:
        # Step 1: Initialize a new Git repository
        subprocess.run(["git", "init", destination_path], check=True)
        os.chdir(destination_path)

        # Step 2: Set the remote origin
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)

        # Step 3: Enable sparse-checkout
        subprocess.run(["git", "sparse-checkout", "init", "--cone"], check=True)

        # Step 4: Specify the folders to include
        subprocess.run(["git", "sparse-checkout", "set"] + folders, check=True)

        # Step 5: Pull the repository
        subprocess.run(["git", "pull", "origin", "main"], check=True)

        print(f"Cloned specific folders {folders} to {destination_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during cloning: {e}")



# Example usage
repo_url = "https://github.com/SkyentificGit/Moteus.git"
destination_path = "github_downloader/git/"
folders = ["MJBotsPythonLibrary"]  # Specify the folders you want to clone
github_downloader(repo_url, destination_path, folders)
