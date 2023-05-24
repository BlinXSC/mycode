#!/bin/bash

echo "Please provide a comment for this upload GitHub"
read $comment

git add *
git commit -m "Test"
git push origin HEAD