#!/bin/bash
# Build release packages for EASY Language

VERSION="$1"
if [ -z "$VERSION" ]; then
    echo "Usage: ./build-releases.sh <version>"
    echo "Example: ./build-releases.sh 1.0.0"
    exit 1
fi

echo "Building EASY Language v$VERSION releases..."

# Create releases directory
mkdir -p releases

# Build Linux package
echo "Building Linux package..."
mkdir -p "easy-lang-$VERSION-linux"
cp -r easy "easy-lang-$VERSION-linux/"
cp -r misc "easy-lang-$VERSION-linux/"
cp installers/install-linux.sh "easy-lang-$VERSION-linux/install.sh"
cp README.md "easy-lang-$VERSION-linux/"
cp LICENSE "easy-lang-$VERSION-linux/" 2>/dev/null || echo "Note: No LICENSE file found"

tar -czf "releases/easy-lang-$VERSION-linux.tar.gz" "easy-lang-$VERSION-linux"
rm -rf "easy-lang-$VERSION-linux"
echo "✓ Created releases/easy-lang-$VERSION-linux.tar.gz"

# Build Windows package
echo "Building Windows package..."
mkdir -p "easy-lang-$VERSION-windows"
cp -r easy "easy-lang-$VERSION-windows/"
cp -r misc "easy-lang-$VERSION-windows/"
cp installers/install-windows.ps1 "easy-lang-$VERSION-windows/install.ps1"
cp README.md "easy-lang-$VERSION-windows/"
cp LICENSE "easy-lang-$VERSION-windows/" 2>/dev/null || echo "Note: No LICENSE file found"

zip -r "releases/easy-lang-$VERSION-windows.zip" "easy-lang-$VERSION-windows"
rm -rf "easy-lang-$VERSION-windows"
echo "✓ Created releases/easy-lang-$VERSION-windows.zip"

echo ""
echo "Release packages created in ./releases/"
ls -lh releases/
