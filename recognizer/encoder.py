from pydub import AudioSegment
import os

# 압축된 WAV 파일 경로
compressed_wav_path = 'compressed_audio.wav'

# 무손실 WAV 파일 경로
lossless_wav_path = 'lossless_audio.wav'

def covert_loseless(audio_file_path):
    audio = AudioSegment.from_file(audio_file_path)
    lossless_audio = audio.set_sample_width(sample_width=2)
    lossless_wav_path = os.path.join("uploads", 'lossless_audio.wav')
    lossless_audio.export(lossless_wav_path, format="wav")
    return lossless_wav_path

if __name__ == "__main__":
    print(covert_loseless("test.wav"))