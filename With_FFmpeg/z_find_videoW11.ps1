# # Define the root directory to start the search (set to 'C:\' to search the entire system)
# $searchRoot = "C:\"  # Change this if you want to search a specific directory

# # Find all output_video.mp4 files and return their paths
# Get-ChildItem -Path $searchRoot -Recurse -Filter "output_video.mp4" -ErrorAction SilentlyContinue | Select-Object FullName


# Define the root directory to start the search (set to 'C:\' to search the entire system)
$searchRoot = "C:\"  # Change this if you want to search a specific directory

# Find all files and sort them by size, then display the top 20 largest files
Get-ChildItem -Path $searchRoot -Recurse -File -ErrorAction SilentlyContinue |
    Sort-Object Length -Descending |
    Select-Object FullName, @{Name="Size(MB)"; Expression={"{0:N2}" -f ($_.Length / 1MB)}} |
    Select-Object -First 20
