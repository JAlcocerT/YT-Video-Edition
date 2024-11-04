// package main

// import (
// 	"fmt"
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

// 	// Build the FFmpeg command to concatenate the first video and the flipped second video
// 	cmd := exec.Command("ffmpeg",
// 		"-i", video1,
// 		"-i", video2,
// 		"-filter_complex", "[1:v]hflip,vflip[v2];[0:v][v2]concat=n=2:v=1:a=0[out]",
// 		"-map", "[out]",
// 		outputVideo)

// 	// Run the command
// 	if err := cmd.Run(); err != nil {
// 		fmt.Println("Error running FFmpeg command:", err)
// 		return
// 	}

// 	fmt.Println("Videos concatenated successfully! Output file:", outputVideo)
// }
