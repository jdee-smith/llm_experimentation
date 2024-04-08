#!/bin/bash
set -e


Help()
{
   # Display Help
   echo "Usage"
   echo
   echo "Syntax: build.sh [-n|h]"
   echo "Options:"
   echo "n     Name to be given to the image."
   echo "h     Print the help manual."
   echo
}

while getopts ":hn:" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      n) # Enter a name
         Name=$OPTARG;;
     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
   esac
done


isort .
black .
mypy .
docker build -t $Name image/.