import whisper
import os

def transcribe_directory(audio_directory):
    # Load the model
    model = whisper.load_model("base")

    # Path to save the output text file
    output_file = "output.txt"

    # Transcribe all MP3 files in the directory
    for filename in os.listdir(audio_directory):
        if filename.endswith(".mp3"):
            audio_path = os.path.join(audio_directory, filename)
            print(f"Transcribing {filename}...")

            # Transcribe the audio
            result = model.transcribe(audio_path)
            transcription = result["text"]

            # Append the transcription to the output file
            with open(output_file, "a") as f:
                f.write(f"Transcription for {filename}:\n{transcription}\n\n")
                print(f"Completed transcription for {filename}")

    print("All transcriptions completed and saved to output.txt.")

if __name__ == "__main__":
    # Directory containing MP3 files
    audio_directory = "/mnt/c/ITOpsTalk/Recordings"  # Update this path to your directory
    transcribe_directory(audio_directory)

