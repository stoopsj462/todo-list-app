; Modern Todo List App - Inno Setup Installer Script
; This creates a professional Windows installer for the application

[Setup]
AppName=Modern Todo List
AppVersion=1.0.0
AppPublisher=Todo List Developer
AppPublisherURL=https://github.com/yourusername/modern-todo-list
AppSupportURL=https://github.com/yourusername/modern-todo-list/issues
AppUpdatesURL=https://github.com/yourusername/modern-todo-list/releases
DefaultDirName={autopf}\Modern Todo List
DefaultGroupName=Modern Todo List
AllowNoIcons=yes
LicenseFile=LICENSE.txt
InfoBeforeFile=README.md
OutputDir=installer_output
OutputBaseFilename=ModernTodoList-Setup-v1.0.0
SetupIconFile=icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
Source: "dist\ModernTodoList.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion
; Add any additional files your app needs
; Source: "assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Modern Todo List"; Filename: "{app}\ModernTodoList.exe"
Name: "{group}\{cm:UninstallProgram,Modern Todo List}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Modern Todo List"; Filename: "{app}\ModernTodoList.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Modern Todo List"; Filename: "{app}\ModernTodoList.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\ModernTodoList.exe"; Description: "{cm:LaunchProgram,Modern Todo List}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

[Code]
procedure InitializeWizard();
begin
  // Custom initialization code if needed
end;

function InitializeSetup(): Boolean;
begin
  Result := True;
  // Add any pre-installation checks here
end;