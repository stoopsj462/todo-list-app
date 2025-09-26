# PowerShell script to create shortcuts for Todo List App

# Create desktop shortcut
$DesktopPath = [Environment]::GetFolderPath("Desktop")
$WshShell = New-Object -comObject WScript.Shell

# Shortcut for GUI version
$Shortcut = $WshShell.CreateShortcut("$DesktopPath\Todo List App.lnk")
$Shortcut.TargetPath = "C:\Users\stoop\OneDrive\Desktop\Todo List App (GUI).bat"
$Shortcut.WorkingDirectory = "C:\Users\stoop\OneDrive\Desktop\code\ToDo list app"
$Shortcut.Description = "Todo List App - Graphical Interface"
$Shortcut.Save()

Write-Host "Desktop shortcut created: Todo List App.lnk"

# Instructions for taskbar
Write-Host ""
Write-Host "To add to taskbar:"
Write-Host "1. Right-click the new desktop shortcut 'Todo List App'"
Write-Host "2. Select 'Pin to taskbar'"
Write-Host ""
Write-Host "Or drag the shortcut to your taskbar!"
Write-Host ""
Write-Host "Press any key to exit..."
Read-Host