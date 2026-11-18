import os
import shutil
public_path = '/home/danielsm/Projects/GitProjects/StaticSiteGenerator/static_site_generator/public'
static_path = '/home/danielsm/Projects/GitProjects/StaticSiteGenerator/static_site_generator/static'

def main():
    just_created = False
    # Check if the public path exists
    if not os.path.exists(public_path):
        os.makedirs(public_path)
        print(f"Created directory: {public_path}")
        just_created = True

    # List all files in the public path
    files = os.listdir(public_path)
    print(f"Files in {public_path}:")
    for file in files:
        print(f"- {file}")

    #Deleting all files in directoy if necessary
    if not just_created:
        for file in files:
            file_path = os.path.join(public_path, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # This will remove the directory and all its contents
                    print(f"Deleted directory and its contents: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    #Recursively copy files from static directory to public path
    copy_directory(static_path, public_path)

    

def copy_directory(src, dest):
    #Copying files from static directory to public path
    for file in os.listdir(src):
        file_path = os.path.join(src, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest)
            print(f"Copied file: {file} to {dest}")
        else:
            new_dest = os.path.join(dest, file)
            if not os.path.exists(new_dest):
                os.makedirs(new_dest)
                print(f"Created directory: {new_dest}")
            copy_directory(file_path, new_dest)
    print(f"Finished copying files from {src} to {dest}")
        

if __name__ == "__main__":
    main()