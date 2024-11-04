# ls *.MP4 | sed "s/^/file '/; s/$/'/" > file_list.txt #add .mp4 of current folder to a list

# #du -sh ./* #check their size

# #generate a video with them
# #ffmpeg -f concat -safe 0 -i file_list.txt -c copy output_video.mp4
# #ffmpeg -f concat -safe 0 -i file_list.txt -c:v copy -an output_video.mp4 #silenced video
# #ffmpeg -i output_video.mp4 -filter:v "setpts=PTS/4" -an fast_output_video.mp4 #

# ##### flip just one file #####
# ffmpeg -i DJI_20241030170740_0050_D.MP4 -vf "transpose=2,transpose=2" -c:a copy flipped_DJI_20241030170740_0050_D.MP4 -y

# ###### Every Video Needs Re-Encoding so that they are compatible when Pasted Together

# # Create a temporary file list for concatenation
# ls *.MP4 | sed 's/^/file /' > file_list.txt

# # Concatenate videos and re-encode
# ffmpeg -f concat -safe 0 -i file_list.txt -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 192k output_merged.mp4

# # Clean up
# #rm file_list.txt


# ####

# # Step 1: Clear the new file list for concatenation
# echo "" > final_file_list.txt

# # Step 2: Process each video file
# for video in *.MP4; do
#     # Get the codec info for the input video
#     codec_info=$(mediainfo --Inform="Video;%Codec%" "$video")
    
#     # Check for rotation metadata
#     if mediainfo "$video" | grep -q 'Rotation'; then
#         # If rotation is found, check if it's specifically 180 degrees
#         if mediainfo "$video" | grep 'Rotation.*180'; then
#             # Rotate the video and maintain the same codec
#             flipped_video="flipped_$video"
#             ffmpeg -i "$video" -vf "transpose=2,transpose=2" -c:v "$codec_info" -c:a copy "$flipped_video" -y
#             echo "file '$flipped_video'" >> final_file_list.txt
#         else
#             # No flip needed
#             echo "file '$video'" >> final_file_list.txt
#         fi
#     else
#         # No rotation metadata; use the original video
#         echo "file '$video'" >> final_file_list.txt
#     fi
# done

# # Step 3: Concatenate all videos into a single file
# ffmpeg -f concat -safe 0 -i final_file_list.txt -c copy output_video_flip.MP4


# #####

# # Step 1: Clear the new file list for concatenation
# # echo "" > final_file_list.txt

# # # Step 2: Process each video file
# # for video in *.MP4; do
# #     # Check if rotation metadata exists
# #     if mediainfo "$video" | grep -q 'Rotation'; then
# #         # No flip needed; re-encode for consistency
# #         reencoded_video="reencoded_$video"
# #         ffmpeg -i "$video" -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k "$reencoded_video" -y
# #         echo "file '$reencoded_video'" >> final_file_list.txt
# #     else
# #         # Flip the video if rotation metadata is missing, then re-encode
# #         flipped_video="flipped_$video"
# #         ffmpeg -i "$video" -vf "transpose=2,transpose=2" -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k "$flipped_video" -y
# #         echo "file '$flipped_video'" >> final_file_list.txt
# #     fi
# # done

# # # Step 3: Concatenate all processed videos into a single output file
# # ffmpeg -f concat -safe 0 -i final_file_list.txt -c copy output_video_final.MP4

# # Step 4: Clean up temporary re-encoded and flipped files if desired
# #rm reencoded_*.MP4 flipped_*.MP4



# # ## Step 1: Clear the new file list for concatenation
# # echo "" > final_file_list.txt

# # # Step 2: Process each video file
# # for video in *.MP4; do
# #     if mediainfo "$video" | grep -q 'Rotation'; then
# #         # No flip needed
# #         echo "file '$video'" >> final_file_list.txt
# #     else
# #         # Flip only if rotation metadata is missing
# #         flipped_video="flipped_$video"
# #         ffmpeg -i "$video" -vf "transpose=2,transpose=2" -c:a copy "$flipped_video" -y
# #         echo "file '$flipped_video'" >> final_file_list.txt
# #     fi
# # done

# # # Step 3: Concatenate all videos into a single file
# # ffmpeg -f concat -safe 0 -i final_file_list.txt -c copy output_video_flip.MP4