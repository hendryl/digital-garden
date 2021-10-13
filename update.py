import shutil
import os

def copy_and_overwrite(from_path, to_path):
  if os.path.exists(to_path):
    shutil.rmtree(to_path)
  shutil.copytree(from_path, to_path)

def main():

  copy_and_overwrite("/mnt/g/My Drive/obsidian-hendry/taman", "./_notes")

if __name__ == '__main__':
  main()
