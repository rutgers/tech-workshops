#!/bin/bash

# Rutgers IEEE Student Branch - Linux Workshop

# Module1-Test.sh

#echo statements are used to print directly to the terminal
#   eg. echo "Hello world!" will print "Hello world!" to the terminal

echo "Let us get started with the Module 1 Test!"
read -p "We are going to build a small test playground! Are you ready? " -n 1 -r
echo

if [[ !  $REPLY =~ ^[Yy]$ ]]; then
    echo "Ok. Let's exit then."
    exit 1
fi

echo
echo "Making a playground!"
mkdir Playground
ls

sleep 1

echo
echo "Entering the playground!"
cd Playground

echo
echo "Let's add some attractions!"

echo
for rides in `cat ../rides.txt`; do
    echo $rides
    mkdir $rides
done

echo
echo "Here is what's in the playground!"

ls -lta

sleep 2

echo
echo "Lets make sure we are still in the playground ..."

sleep 1
pwd

echo
echo "Deleting playground..."

sleep 1

cd ..
rm -r Playground
 
echo "All done!"
