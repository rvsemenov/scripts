#!/usr/bin/python

import os, sys

def main():
  currentDir = sys.argv[1]

  folders = []
  folders.append(currentDir)
  # r=root, d=directories, f = files
  for r, d, f in os.walk(currentDir):
    for folder in d:
      folders.append(os.path.join(r, folder))

  for f in folders:
    for filename in os.listdir(f):
      fname, fext = os.path.splitext(filename)
      directory = currentDir + fext[1:]
      if not os.path.exists(directory):
        os.makedirs(directory) 
      os.rename(f + "/" + filename, directory + "/" + filename)

if __name__ == '__main__':
  main()
