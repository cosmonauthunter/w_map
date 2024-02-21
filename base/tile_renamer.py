import os

# Directory where your tiles are stored (change this to your actual directory)
directory = "./"

# Assuming all tiles are at zoom level 0
zoom_level = 0

# Grid dimensions
grid_width = 7
grid_height = 8

# Function to rename files
def rename_files():
    for y in range(grid_height):
        for x in range(grid_width):
            # Calculate the original tile number based on x and y
            original_tile_number = y * grid_width + x + 1
            # Format it to match your original naming scheme (e.g., 01, 02, ...)
            original_filename = f"Witcher_timeline_onmap_tiles-{original_tile_number:02}.jpg"
            # New filename in the format of "z_x_y.png"
            new_filename = f"{zoom_level}_{x}_{y}.jpg"
            
            # Full path for original and new filenames
            original_filepath = os.path.join(directory, original_filename)
            new_filepath = os.path.join(directory, new_filename)
            
            # Check if the original file exists to avoid errors
            if os.path.exists(original_filepath):
                # Rename the file
                os.rename(original_filepath, new_filepath)
                print(f"Renamed '{original_filename}' to '{new_filename}'")
            else:
                print(f"File '{original_filename}' not found.")

# Call the function to start renaming
rename_files()
