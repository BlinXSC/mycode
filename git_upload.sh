#!/bin/bash

echo "Please provide a comment for this upload GitHub"
read comment

git add *
git commit -m "$comment"
git push origin HEAD