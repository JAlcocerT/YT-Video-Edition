import os
import torch
import numpy as np
from pydub import AudioSegment
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

def extract_audio(video_file):
    """Extracts audio from a video file and saves it as a WAV file."""
    audio = AudioSegment.from_file(video_file)
    audio_file = "extracted_audio.wav"
    audio.export(audio_file, format="wav")
    return audio_file

def load_model():
    """Loads the Wav2Vec2 model and processor from Hugging Face."""
    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
    return processor, model

def detect_speech_intervals(audio_file, processor, model):
    """Detects intervals in the audio file where speech is present."""
    audio = AudioSegment.from_wav(audio_file)

    # Resample to 16 kHz if necessary
    if audio.frame_rate != 16000:
        audio = audio.set_frame_rate(16000)

    audio_array = np.array(audio.get_array_of_samples()).astype(np.float32)
    
    # Normalize audio array
    audio_array = audio_array / np.max(np.abs(audio_array))

    # Tokenize audio
    inputs = processor(audio_array, sampling_rate=16000, return_tensors="pt", padding=True)

    # Get logits from the model
    with torch.no_grad():
        logits = model(**inputs).logits

    # Get predicted IDs
    predicted_ids = torch.argmax(logits, dim=-1)

    # Decode the IDs to text
    transcription = processor.batch_decode(predicted_ids)[0]
    
    # Here, we assume speech is detected if there is a non-empty transcription
    speaking_intervals = []
    if transcription.strip():
        speaking_intervals.append((0, len(audio) / 1000))  # From start to end (in seconds)

    return speaking_intervals

def main(video_file):
    # Extract audio from video
    audio_file = extract_audio(video_file)
    
    # Load model
    processor, model = load_model()
    
    # Detect speaking intervals
    speaking_intervals = detect_speech_intervals(audio_file, processor, model)

    # Display the intervals
    if speaking_intervals:
        print("Detected speaking intervals:")
        for start, end in speaking_intervals:
            print(f"Start: {start} s, End: {end} s")
    else:
        print("No speaking detected.")

    # Clean up the extracted audio file
    if os.path.exists(audio_file):
        os.remove(audio_file)

if __name__ == "__main__":
    video_path = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/DJI_20241030132520_0026_D.MP4"  # Example video path
    video_path = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/TrastevereVaticanWalk/DJI_20241029115014_0001_D.MP4"
    main(video_path)


# import os
# import torch
# import numpy as np
# from pydub import AudioSegment
# from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# def extract_audio(video_file):
#     """Extracts audio from a video file and saves it as a WAV file."""
#     audio = AudioSegment.from_file(video_file)
#     audio_file = "extracted_audio.wav"
#     audio.export(audio_file, format="wav")
#     return audio_file

# def load_model():
#     """Loads the Wav2Vec2 model and processor from Hugging Face."""
#     processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
#     model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
#     return processor, model

# def detect_speech_intervals(audio_file, processor, model):
#     """Detects intervals in the audio file where speech is present."""
#     audio = AudioSegment.from_wav(audio_file)
#     audio_array = np.array(audio.get_array_of_samples()).astype(np.float32)
    
#     # Normalize audio array
#     audio_array = audio_array / np.max(np.abs(audio_array))

#     # Tokenize audio
#     inputs = processor(audio_array, sampling_rate=audio.frame_rate, return_tensors="pt", padding=True)

#     # Get logits from the model
#     with torch.no_grad():
#         logits = model(**inputs).logits

#     # Get predicted IDs
#     predicted_ids = torch.argmax(logits, dim=-1)

#     # Decode the IDs to text
#     transcription = processor.batch_decode(predicted_ids)[0]
    
#     # Here, we assume speech is detected if there is a non-empty transcription
#     speaking_intervals = []
#     if transcription.strip():
#         speaking_intervals.append((0, len(audio) / 1000))  # From start to end (in seconds)

#     return speaking_intervals

# def main(video_file):
#     # Extract audio from video
#     audio_file = extract_audio(video_file)
    
#     # Load model
#     processor, model = load_model()
    
#     # Detect speaking intervals
#     speaking_intervals = detect_speech_intervals(audio_file, processor, model)

#     # Display the intervals
#     if speaking_intervals:
#         print("Detected speaking intervals:")
#         for start, end in speaking_intervals:
#             print(f"Start: {start} s, End: {end} s")
#     else:
#         print("No speaking detected.")

#     # Clean up the extracted audio file
#     if os.path.exists(audio_file):
#         os.remove(audio_file)

# if __name__ == "__main__":
#     video_path = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/DJI_20241030132520_0026_D.MP4"  # Example video path
#     main(video_path)
