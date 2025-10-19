# Installing EASY Language

EASY is a beginner-friendly programming language that's easy to install on any platform.

## Linux Installation

### Quick Install (Recommended)

1. Download the latest release:
```
wget https://github.com/tyydev1/easy-language/releases/latest/download/easy-lang-linux.tar.gz
```

2. Extract and run the installer:
```bash
   tar -xzf easy-lang-linux.tar.gz
   cd easy-lang-*-linux
   ./install.sh
```

3. Restart your terminal or run:
```bash
   source ~/.bashrc  # or ~/.zshrc if you use zsh
```

4. Test your installation:
```bash
   echo 'say("Hello, EASY!")' > test.esy
   easy test.esy
```

### Manual Installation

If you prefer to install manually:

1. Clone the repository or download the source
2. Copy the `easy/` directory to `~/.easy-lang/`
3. Add `~/.local/bin` to your PATH
4. Create wrapper scripts in `~/.local/bin/`

## Windows Installation

### Quick Install (Recommended)

1. Download the latest release: `easy-lang-windows.zip`

2. Extract the ZIP file to a folder

3. Right-click on `install.ps1` and select "Run with PowerShell"
   - If you see a security warning, type `Y` and press Enter

4. Open a new Command Prompt or PowerShell window

5. Test your installation:
```cmd
   echo say("Hello, EASY!") > test.esy
   easy test.esy
```

### Requirements

- Python 3.6 or higher
- Windows 10 or later (for best compatibility)

If Python is not installed:
1. Download from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation

## Verifying Installation

After installation, you should be able to run:
```bash
easy --help
```

Or start the interactive shell:
```bash
easy-shell
```

## Troubleshooting

### Command not found

**Linux**: Make sure `~/.local/bin` is in your PATH:
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Windows**: Restart your command prompt or PowerShell window after installation.

### Python not found

Install Python 3.6+ from [python.org](https://www.python.org/downloads/)

### Permission denied (Linux)

Make the installer executable:
```bash
chmod +x install.sh
```

## Uninstallation

**Linux**:
```bash
rm -rf ~/.easy-lang
rm ~/.local/bin/easy
rm ~/.local/bin/easy-shell
```

**Windows**:
```powershell
Remove-Item -Recurse "$env:LOCALAPPDATA\EasyLang"
Remove-Item "$env:LOCALAPPDATA\Microsoft\WindowsApps\easy.cmd"
Remove-Item "$env:LOCALAPPDATA\Microsoft\WindowsApps\easy-shell.cmd"
```

## Getting Help

- [GitHub Issues](https://github.com/tyydev1/easy-language/issues)
- [Documentation](https://github.com/tyydev1/easy-language)
- [Examples](https://github.com/tyydev1/easy-language/tree/main/misc)
