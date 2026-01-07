#!/usr/bin/env bash

# Stop if any command fails
set -e

echo "🚀 Bootstrapping new Python project..."

# Ask for project name
read -p "Enter project name (snake_case, e.g. payment_service): " PROJECT_NAME
read -p "Project description: " PROJECT_DESC

# Validate input
if [[ -z "$PROJECT_NAME" ]]; then
  echo "❌ Project name cannot be empty"
  exit 1
fi

# Replace placeholder text in all files
echo "🔄 Replacing project name placeholders..."
grep -rl "__PROJECT_NAME__" . | xargs sed -i "s/__PROJECT_NAME__/$PROJECT_NAME/g"
grep -rl "__PROJECT_DESCRIPTION__" . | xargs sed -i "s/__PROJECT_DESCRIPTION__/$PROJECT_DESC/g"

# Rename src/app → src/<project_name>
if [ -d "src/app" ]; then
  mv src/app src/$PROJECT_NAME
fi

echo "✅ Bootstrap completed successfully!"
echo "👉 Your package name is now: $PROJECT_NAME"
echo "👉 Start coding inside src/$PROJECT_NAME"
