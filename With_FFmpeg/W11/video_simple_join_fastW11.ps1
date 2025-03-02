
# Function to join videos without reencoding using FFmpeg
function Join-Videos {
    param (
        [string]$videoDirectory,   # Path to the directory with video files
        [string]$outputDirectory,  # Path to the directory where the output will be saved
        [string]$outputFilename = "output_video2.mp4"  # Name of the output video
    )

    # Create the file_list.txt in the video directory
    $fileListPath = Join-Path $videoDirectory "file_list.txt"
    
    # Open the file for writing
    $fileListContent = @()
    
    # Get all MP4 files and add them to the list
    Get-ChildItem -Path $videoDirectory -Filter *.MP4 | Sort-Object Name | ForEach-Object {
        $fileListContent += "file '$($_.FullName)'"
    }
    
    # Write the content to file_list.txt
    $fileListContent | Out-File -FilePath $fileListPath -Encoding UTF8

    # Construct the full output path
    $outputPath = Join-Path $outputDirectory $outputFilename

    # Concatenate the videos using FFmpeg (no reencoding)
    $ffmpegCommand = "ffmpeg -f concat -safe 0 -i '$fileListPath' -c copy '$outputPath'"

    # Execute the FFmpeg command
    Write-Host "Running FFmpeg to concatenate videos..."
    Invoke-Expression $ffmpegCommand

    # Check if the output video was created
    if (Test-Path $outputPath) {
        Write-Host "Videos successfully concatenated and saved as: $outputPath"
    } else {
        Write-Host "Error: Output video not created."
    }

    # Clean up the temporary file_list.txt
    Remove-Item -Path $fileListPath -Force
}

# Example usage
$videoDirectory = "C:\Users\j--e-\Desktop\DJiOA5Pro-NL\NL-17nov"  # Path to the folder containing videos
$outputDirectory = "C:\Users\j--e-\Desktop\DJiOA5Pro-NL\NL-17nov"  # Path to the folder where the output will be saved

Join-Videos -videoDirectory $videoDirectory -outputDirectory $outputDirectory



# # Define the path to the folder containing the videos
# $videoFolder = "C:\Users\j--e-\Desktop\DJiOA5Pro-NL\NL-17nov"

# # Change directory to the video folder
# Set-Location $videoFolder


# # Create file_list.txt in the video folder
# dir *.MP4 | ForEach-Object { "file '$($_.Name)'" } > file_list.txt

# # Concatenate videos and save output in the same folder
# ffmpeg -f concat -safe 0 -i file_list.txt -c copy "$videoFolder\output_video.mp4"

# # (Optional) Check file sizes
# Get-ChildItem *.MP4 | Select-Object Name, @{Name="Size(MB)"; Expression={ "{0:N2}" -f ($_.Length / 1MB) }}


# # Change directory to where your videos are located
# # Set-Location "C:\Users\j--e-\Desktop\DJiOA5Pro-NL\NL-17nov"

# # # Create file_list.txt
# # dir *.MP4 | ForEach-Object { "file '$($_.Name)'" } > file_list.txt

# # # Concatenate videos
# # ffmpeg -f concat -safe 0 -i file_list.txt -c copy output_video.mp4

# # # (Optional) Check file sizes
# # Get-ChildItem *.MP4 | Select-Object Name, @{Name="Size(MB)"; Expression={ "{0:N2}" -f ($_.Length / 1MB) }}


# # Ensure Compatibility If your videos differ in codec, resolution, or frame rate, -c copy may fail. In that case, re-encode the videos:

# # ffmpeg -f concat -safe 0 -i file_list.txt -c:v libx264 -crf 23 -preset fast output_video.mp4

# #     This ensures compatibility by re-encoding the videos into a standard format.

# #### LINUX ####

# # ls *.MP4 | sed "s/^/file '/; s/$/'/" > file_list.txt #add .mp4 of current folder to a list

# # #du -sh ./* #check their size

# # ###generate a video with them
# # #ffmpeg -f concat -safe 0 -i file_list.txt -c copy output_video.mp4
# # #ffmpeg -f concat -safe 0 -i file_list.txt -c:v copy -an output_video.mp4 #silenced video
# # ffmpeg -i output_video.mp4 -filter:v "setpts=PTS/4" -an fast_output_video.mp4 #