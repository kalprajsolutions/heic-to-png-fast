[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/kalprajsolutions/heic-to-png-fast) [![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php) ![Python](https://img.shields.io/badge/python-3.6-blue.svg) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/kalprajsolutions/heic-to-png-fast/pulls) [![Downloads](https://pepy.tech/badge/global-chem)](https://github.com/kalprajsolutions/heic-to-png-fast)

# 🖼️ HEIC to PNG Batch Converter (Fast & Parallel)

A Python script that converts all `.HEIC` images in the current folder to `.PNG` format using parallel processing. Built with `Pillow`, `pyheif`, and `concurrent.futures` for speed.

![heic to png](heic-to-png.png)

## 🚀 Features

* ✅ Batch converts all `.HEIC` files in the folder
* ⚡ Parallel processing for fast execution (uses all CPU cores by default)
* 📂 Simple command-line usage
* 🛠️ Error-handling for bad/corrupt files

## 📦 Requirements

Install the required Python packages:

```bash
pip install pillow pyheif
```

> **Note**: You may need to install the `libheif` system library as well:

**Ubuntu/Debian:**

```bash
sudo apt-get install libheif1 libheif-dev
```

**macOS (Homebrew):**

```bash
brew install libheif
```

## 🐍 Usage

1. Place the script in the folder with your `.HEIC` files.
2. Run the script:

```bash
python main.py
```

It will automatically find and convert all `.HEIC` files in the current directory.

## 🧠 How It Works

* Uses `pyheif` to read `.HEIC` files.
* Converts images using `Pillow`.
* Processes multiple files in parallel using `concurrent.futures.ProcessPoolExecutor`.

## 📁 Example Output

```
Found 27 HEIC files. Starting conversion...
✔ Converted: IMG_1001.HEIC -> IMG_1001.png
✔ Converted: IMG_1002.HEIC -> IMG_1002.png
...
```

## 🛡️ License

MIT License
