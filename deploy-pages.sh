#!/data/data/com.termux/files/usr/bin/bash
set -e
REPO_DIR="$PWD"
LANDING_DIR="$REPO_DIR/landing"
echo "🚀 Kessel_Run Pages Deploy..."
touch "$LANDING_DIR/.nojekyll"
cat > README.md << 'RMD'
# Kessel_Run AI | rayrock92610
**Live:** https://rayrock92610.github.io/Kessel_Run/landing/index.html
Termux-native AI runtime. GP-API intel, London Bridge Sentinel.
RMD
git add "$LANDING_DIR/.nojekyll" README.md
git commit -m "deploy(pages): .nojekyll + README" || echo "No changes"
git push origin main
echo "✅ Pushed. Configure: https://github.com/RayRock92610/Kessel_Run/settings/pages"
echo "Branch: main → /root → Save → Live @ https://rayrock92610.github.io/Kessel_Run/landing/index.html"
curl -s raw.githubusercontent.com/RayRock92610/Kessel_Run/main/landing/index.html | grep title
