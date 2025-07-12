#!/bin/bash

echo "Creating repository structure for AudioToGerman..."

# Create directories
mkdir -p src input output logs scripts

# Create files
touch src/__init__.py
touch src/audio_processor.py
touch src/transcriber.py
touch src/translator.py
touch src/text_to_speech.py
touch src/main.py
touch src/app.py
touch scripts/setup_repo.sh
touch requirements.txt
touch README.md
touch .gitignore

# Populate files (simplified; actual content will be copied from below)
echo "Writing placeholder content to files..."

# .gitignore
cat > .gitignore << EOL
# .gitignore
__pycache__/
*.pyc
input/*
output/*
logs/*
*.mp3
*.wav
*.mp4
*.pt
*.bin
*.h5
.env
EOL

# requirements.txt
cat > requirements.txt << EOL
ffmpeg-python==0.2.0
transformers==4.44.2
datasets==2.21.0
soundfile==0.12.1
scipy==1.13.1
torch==2.4.1
streamlit==1.39.0
EOL

echo "Repository structure created successfully!"
echo "Next steps:"
echo "1. Copy source code into src/ files (or update setup_repo.sh with full content)."
echo "2. Install FFmpeg: sudo apt-get install ffmpeg"
echo "3. Install dependencies: pip install -r requirements.txt"
echo "4. Run Streamlit: streamlit run src/app.py"
