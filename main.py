"""
Chechen TTS — baseline using Meta MMS-TTS-che.
Generates speech from Chechen text and saves it as output.wav.
"""

import sys
import torch
import scipy.io.wavfile
from transformers import VitsModel, AutoTokenizer

DEFAULT_TEXT = "Ассаламу алайкум, муха ду хьан гӀуллакхаш?"
MODEL_NAME = "facebook/mms-tts-che"
OUTPUT_FILE = "output.wav"


def main():
    text = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TEXT

    print(f"Loading model ({MODEL_NAME})...")
    model = VitsModel.from_pretrained(MODEL_NAME)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    print(f"Synthesizing: {text}")
    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = model(**inputs).waveform

    audio = output.squeeze().numpy()
    scipy.io.wavfile.write(
        OUTPUT_FILE,
        rate=model.config.sampling_rate,
        data=audio,
    )

    print(f"Done. Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
