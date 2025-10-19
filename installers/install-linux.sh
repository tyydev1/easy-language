#!/bin/bash
# EASY Language Installer for Linux
# Installs the EASY interpreter and makes it available system-wide

set -e  # Exit on any error

# Colors for pretty output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  EASY Language Installer v1.0      ║${NC}"
echo -e "${BLUE}╔════════════════════════════════════╗${NC}"
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is required but not installed.${NC}"
    echo "Please install Python 3.6 or higher and try again."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo -e "${GREEN}✓${NC} Found Python ${PYTHON_VERSION}"

# Installation directories
INSTALL_DIR="$HOME/.easy-lang"
BIN_DIR="$HOME/.local/bin"

# Create directories
echo ""
echo "Creating installation directories..."
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

# Copy interpreter files
echo "Installing EASY interpreter..."
cp -r easy/* "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/easy.py"

# Create the main executable wrapper
echo "Creating easy command wrapper..."
cat > "$BIN_DIR/easy" << 'WRAPPER_EOF'
#!/usr/bin/env python3
import sys
import os

# Add EASY installation directory to Python path
easy_dir = os.path.expanduser("~/.easy-lang")
sys.path.insert(0, easy_dir)

# Import and run
import easy

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("EASY Language Interpreter v1.0")
        print("Usage: easy <filename.esy>")
        print("\nExamples:")
        print("  easy script.esy")
        print("  easy program.ez")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    # Add .esy extension if no extension provided
    if not ('.' in filename):
        filename += '.esy'
    
    try:
        with open(filename, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    result, error = easy.run(filename, code)
    
    if error:
        print(error.as_string())
        sys.exit(1)
    elif result and not isinstance(result, type(easy.Number.null)):
        print(result)
WRAPPER_EOF

chmod +x "$BIN_DIR/easy"

# Install the shell
echo "Installing EASY shell..."
cp misc/shell.py "$INSTALL_DIR/shell.py"

cat > "$BIN_DIR/easy-shell" << 'SHELL_EOF'
#!/usr/bin/env python3
import sys
import os

easy_dir = os.path.expanduser("~/.easy-lang")
sys.path.insert(0, easy_dir)

import shell
SHELL_EOF

chmod +x "$BIN_DIR/easy-shell"

# Setup PATH
echo ""
echo "Setting up PATH..."

SHELL_RC=""
if [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
else
    SHELL_RC="$HOME/.profile"
fi

# Check if PATH already includes .local/bin
if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$SHELL_RC" 2>/dev/null; then
    echo "" >> "$SHELL_RC"
    echo "# Added by EASY Language installer" >> "$SHELL_RC"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
    echo -e "${GREEN}✓${NC} Added ~/.local/bin to PATH in $SHELL_RC"
else
    echo -e "${GREEN}✓${NC} PATH already configured"
fi

# Verify installation
echo ""
echo -e "${GREEN}╔════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  Installation Complete!            ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════╝${NC}"
echo ""
echo "EASY has been installed to: $INSTALL_DIR"
echo "Commands available:"
echo "  ${BLUE}easy${NC}       - Run EASY programs"
echo "  ${BLUE}easy-shell${NC} - Interactive EASY shell"
echo ""
echo -e "${YELLOW}Important:${NC} Restart your terminal or run:"
echo "  source $SHELL_RC"
echo ""
echo "Try it out:"
echo "  echo 'say(\"Hello, EASY!\")' > test.esy"
echo "  easy test.esy"
echo ""
