@echo off
REM Flutter Setup Script for Windows - Modern Todo List Mobile App
echo ========================================
echo   Flutter Mobile App Setup
echo ========================================
echo.

REM Check if Flutter is installed
flutter --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Flutter is not installed or not in PATH
    echo.
    echo Please install Flutter:
    echo 1. Download from: https://flutter.dev/docs/get-started/install/windows
    echo 2. Extract to C:\flutter
    echo 3. Add C:\flutter\bin to your PATH
    echo 4. Run this script again
    echo.
    pause
    exit /b 1
)

echo ✅ Flutter is installed
flutter --version

echo.
echo [1/5] Running Flutter Doctor...
flutter doctor

echo.
echo [2/5] Creating Flutter project...
if not exist "flutter_todo" (
    flutter create flutter_todo --org com.todolist.modernapp
    echo ✅ Flutter project created
) else (
    echo ℹ️  Flutter project already exists
)

echo.
echo [3/5] Setting up project dependencies...
cd flutter_todo

REM Create pubspec.yaml with dependencies
echo name: modern_todo_list > pubspec.yaml
echo description: A modern, beautiful todo list app >> pubspec.yaml
echo version: 1.0.0+1 >> pubspec.yaml
echo. >> pubspec.yaml
echo environment: >> pubspec.yaml
echo   sdk: '>=2.19.0 <4.0.0' >> pubspec.yaml
echo. >> pubspec.yaml
echo dependencies: >> pubspec.yaml
echo   flutter: >> pubspec.yaml
echo     sdk: flutter >> pubspec.yaml
echo   cupertino_icons: ^1.0.2 >> pubspec.yaml
echo   shared_preferences: ^2.0.15 >> pubspec.yaml
echo   provider: ^6.0.3 >> pubspec.yaml
echo   intl: ^0.18.0 >> pubspec.yaml
echo   flutter_local_notifications: ^15.0.0 >> pubspec.yaml
echo   path_provider: ^2.0.11 >> pubspec.yaml
echo. >> pubspec.yaml
echo dev_dependencies: >> pubspec.yaml
echo   flutter_test: >> pubspec.yaml
echo     sdk: flutter >> pubspec.yaml
echo   flutter_lints: ^2.0.0 >> pubspec.yaml
echo. >> pubspec.yaml
echo flutter: >> pubspec.yaml
echo   uses-material-design: true >> pubspec.yaml

flutter pub get

echo [4/5] Setting up project structure...
REM Create directories
mkdir lib\models 2>nul
mkdir lib\screens 2>nul
mkdir lib\services 2>nul
mkdir lib\widgets 2>nul
mkdir lib\theme 2>nul
mkdir assets\icons 2>nul
mkdir assets\images 2>nul

echo [5/5] Setup complete!
echo.
echo ========================================
echo   Setup Successful! 🎉
echo ========================================
echo.
echo Next steps:
echo 1. Open project: code flutter_todo
echo 2. Start development: flutter run
echo 3. Connect a device or start an emulator
echo.
echo Available commands:
echo   flutter run          - Run app in debug mode
echo   flutter hot-reload   - Press 'r' during development
echo   flutter build apk    - Build for Android
echo   flutter build ios    - Build for iOS
echo.

cd ..
pause