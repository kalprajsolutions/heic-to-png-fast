import os
import pyheif
from PIL import Image
from concurrent.futures import ProcessPoolExecutor, as_completed

def convert_heic_to_png(input_path):
    try:
        output_path = os.path.splitext(input_path)[0] + ".png"

        heif_file = pyheif.read(input_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        image.save(output_path, "PNG")
        return f"✔ Converted: {input_path} -> {output_path}"
    except Exception as e:
        return f"✘ Failed: {input_path} ({e})"

def batch_convert_parallel(folder='.', max_workers=None):
    heic_files = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.lower().endswith(".heic")
    ]

    if not heic_files:
        print("No HEIC files found.")
        return

    print(f"Found {len(heic_files)} HEIC files. Starting conversion...")

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(convert_heic_to_png, file) for file in heic_files]
        for future in as_completed(futures):
            print(future.result())

# Run conversion in current directory using all available cores
if __name__ == "__main__":
    batch_convert_parallel()
