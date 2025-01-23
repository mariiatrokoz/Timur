#!/bin/bash
echo "do you miss me?"
echo "enter 'y' for yes and 'n' for no"
read response
if [ "$response" = "y" ]; then
echo "I miss u 2!:***"
elif [ "$response" = "n" ]; then
echo "Oh,okay. That's fine"
else
    echo "What? Bye!"

fi
