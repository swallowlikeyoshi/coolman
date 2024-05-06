import ffmpeg
import os

def convert_aac_to_wav(input_file, output_file, ffmpeg_path):
    (
        ffmpeg
        .input(input_file)
        .output(output_file, acodec='pcm_s16le', format='wav')
        .run(cmd=ffmpeg_path, overwrite_output=True)
    )
    return output_file

if __name__ == "__main__":
    input_file_path = "input.aac"
    output_file_path = "output.wav"
    convert_aac_to_wav(input_file_path, output_file_path)
    print("Conversion complete!")
