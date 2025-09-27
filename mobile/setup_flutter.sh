#!/bin/bash
# Flutter Setup Script for macOS/Linux - Modern Todo List Mobile App

echo "========================================"
echo "  Flutter Mobile App Setup"
echo "========================================"
echo

# Check if Flutter is installed
if ! command -v flutter &> /dev/null; then
    echo "❌ Flutter is not installed or not in PATH"
    echo
    echo "Please install Flutter:"
    echo "macOS: https://flutter.dev/docs/get-started/install/macos"
    echo "Linux: https://flutter.dev/docs/get-started/install/linux"
    echo
    echo "After installation, add Flutter to your PATH and run this script again"
    exit 1
fi

echo "✅ Flutter is installed"
flutter --version

echo
echo "[1/5] Running Flutter Doctor..."
flutter doctor

echo
echo "[2/5] Creating Flutter project..."
if [ ! -d "flutter_todo" ]; then
    flutter create flutter_todo --org com.todolist.modernapp
    echo "✅ Flutter project created"
else
    echo "ℹ️  Flutter project already exists"
fi

echo
echo "[3/5] Setting up project dependencies..."
cd flutter_todo

# Create pubspec.yaml with dependencies
cat > pubspec.yaml << EOF
name: modern_todo_list
description: A modern, beautiful todo list app
version: 1.0.0+1

environment:
  sdk: '>=2.19.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2
  shared_preferences: ^2.0.15
  provider: ^6.0.3
  intl: ^0.18.0
  flutter_local_notifications: ^15.0.0
  path_provider: ^2.0.11

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^2.0.0

flutter:
  uses-material-design: true
EOF

flutter pub get

echo "[4/5] Setting up project structure..."
# Create directories
mkdir -p lib/{models,screens,services,widgets,theme}
mkdir -p assets/{icons,images}

echo "[5/5] Setup complete!"
echo
echo "========================================"
echo "  Setup Successful! 🎉"
echo "========================================"
echo
echo "Next steps:"
echo "1. Open project: code flutter_todo"
echo "2. Start development: flutter run"
echo "3. Connect a device or start an emulator"
echo
echo "Available commands:"
echo "  flutter run          - Run app in debug mode"
echo "  flutter hot-reload   - Press 'r' during development"
echo "  flutter build apk    - Build for Android"
echo "  flutter build ios    - Build for iOS (macOS only)"
echo

cd ..
echo "Press Enter to continue..."
read