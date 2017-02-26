rust for visual studio:
https://marketplace.visualstudio.com/items?itemName=vosen.VisualRust


PROBLEM: No Rust installation detected (rustup-init.exe, VisualRust 0.1.2, VS 2015)
solution: (execute as an admin on cmd)
REG ADD "HKLM\SOFTWARE\Mozilla Foundation\Rust\current" /v InstallDir /t REG_SZ /d "%USERPROFILE%\.cargo"

