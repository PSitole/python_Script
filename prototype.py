import os
import librosa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split


AUDIO_FOLDER = 'audio_files/'
RESULTS_FOLDER = 'results/'


def detect_emotion(audio_file):
    return "happy"

def detect_aggression(audio_file):
    return False

def create_line_chart(emotion, aggression, audio_file):
    # Get time data from the audio file
    time, audio_data = librosa.load(audio_file)

    # Create line chart for emotion and aggression over time
    plt.figure(figsize=(10, 4))
    plt.plot(time, emotion, label='Emotion', color='blue')
    plt.plot(time, aggression, label='Aggression', color='red')
    plt.xlabel('Time')
    plt.ylabel('Intensity')
    plt.title('Emotion and Aggression Detection Over Time')
    plt.legend()
    plt.grid()
    plt.savefig(os.path.join(RESULTS_FOLDER, audio_file.split('.')[0] + '_chart.png'))
    plt.close()


def main():
    # Create results folder if it doesn't exist
    if not os.path.exists(RESULTS_FOLDER):
        os.makedirs(RESULTS_FOLDER)

    for audio_file in os.listdir(AUDIO_FOLDER):
        if audio_file.endswith(".wav") or audio_file.endswith(".mp3"):
            audio_path = os.path.join(AUDIO_FOLDER, audio_file)

            emotion = detect_emotion(audio_path)

            aggression = detect_aggression(audio_path)

            # Print results as tables
            results_df = pd.DataFrame({'Audio File': [audio_file], 'Emotion': [emotion], 'Sad': [aggression]})
            results_df.to_csv(os.path.join(RESULTS_FOLDER, audio_file.split('.')[0] + '_results.csv'), index=False)

            # Create line charts for emotion and aggression
            if emotion is not None and aggression is not False:
                create_line_chart(emotion, aggression, audio_path)

if __name__ == "__main__":
    main()
