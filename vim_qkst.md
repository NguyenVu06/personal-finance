

## Summary of Commands
```bash
# Clone the repository
git clone https://gitlab.com/yourusername/yourrepository.git
cd yourrepository

# Create a new branch
git checkout -b feature/your-feature-name

# Make changes, add, and commit
git add .
git commit -m "Describe the changes you made"

# Push changes to GitLab
git push origin feature/your-feature-name

# After MR approval, merge and push
git checkout main
git pull origin main
git merge feature/your-feature-name
git push origin main

# Delete the feature branch
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

This workflow ensures that each team member can work on their own tasks without interfering with others, and changes are only merged into the main branch after review and approval.

