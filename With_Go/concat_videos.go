// package main

// import (
// 	"fmt"
// 	"os"
// 	"os/exec"
// )

// func main() {
// 	// Define the directory where the videos are located
// 	videoDirectory := "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"

// 	// Define the input video file names
// 	video1 := videoDirectory + "DJI_20241030132520_0026_D.MP4"
// 	video2 := videoDirectory + "DJI_20241030145603_0036_D.MP4"

// 	// Define the output file name
// 	outputVideo := videoDirectory + "output.mp4"

// 	// Create a temporary text file listing the videos to concatenate
// 	tempFile, err := os.Create("video_list.txt")
// 	if err != nil {
// 		fmt.Println("Error creating file:", err)
// 		return
// 	}
// 	defer tempFile.Close()

// 	// Write the video file paths to the temporary file
// 	_, err = tempFile.WriteString(fmt.Sprintf("file '%s'\n", video1))
// 	if err != nil {
// 		fmt.Println("Error writing to file:", err)
// 		return
// 	}
// 	_, err = tempFile.WriteString(fmt.Sprintf("file '%s'\n", video2))
// 	if err != nil {
// 		fmt.Println("Error writing to file:", err)
// 		return
// 	}

// 	// Build the FFmpeg command to concatenate videos
// 	cmd := exec.Command("ffmpeg", "-f", "concat", "-safe", "0", "-i", "video_list.txt", "-c", "copy", outputVideo)

// 	// Run the command
// 	if err := cmd.Run(); err != nil {
// 		fmt.Println("Error running FFmpeg command:", err)
// 		return
// 	}

// 	fmt.Println("Videos concatenated successfully! Output file:", outputVideo)
// }