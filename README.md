# Chechen TTS

An open-source text-to-speech project for the Chechen language (нохчийн мотт).

## About

Chechen is a Nakh-Dagestanian language spoken by around 1.5 million people. Despite its size, it is not supported by major TTS providers such as Google, Amazon, ElevenLabs, Yandex, or Sber SaluteSpeech.

This repository provides a working baseline for Chechen text-to-speech based on Meta's [MMS-TTS-che](https://huggingface.co/facebook/mms-tts-che) model. The current version is functional but far from perfect — pronunciation and intonation are limited.

A dedicated, fine-tuned model with significantly better quality is currently in development and will be released here as soon as it is ready.

## Requirements

- Python 3.9 or newer
- ~2 GB of free disk space (for dependencies and the model)
- Internet connection on first run (to download the model)
- Works on CPU; a GPU makes it faster but is not required

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/chechen-tts.git
cd chechen-tts
```

Create a virtual environment (recommended):

```
python -m venv .venv
```

Activate it:

- **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
- **macOS / Linux:** `source .venv/bin/activate`

Install dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the script with the default example:

```
python main.py
```

Or pass your own Chechen text:

```
python main.py "Ассаламу алайкум, муха ду хьан гӀуллакхаш?"
```

On first run, the model (~150 MB) will be downloaded from Hugging Face and cached locally. Subsequent runs will start instantly.

The generated audio will be saved as `output.wav` in the project folder.

## Known limitations

- Pronunciation of Chechen-specific sounds (кӀ, пӀ, тӀ, цӀ, чӀ, Ӏ, хь, гӀ, къ) is inconsistent
- Intonation can sound flat or unnatural
- Long sentences may lose rhythm — splitting text into shorter sentences helps
- Different orthography variants (Ӏ vs I vs 1) may produce different results

These issues are inherent to the baseline model and are the main motivation for the ongoing improved version.

## Roadmap

- [x] Working baseline (MMS-TTS-che)
- [ ] Collect and curate a Chechen speech dataset
- [ ] Fine-tune the model for improved naturalness
- [ ] Publish improved model weights
- [ ] Simple web demo

## How to help

- **Native Chechen speakers** — feedback on pronunciation and naturalness
- **Chechen texts** — clean written material with clear licensing
- **Chechen audio with transcripts** — audiobooks, lectures, interviews with matching text
- **ML engineers** — training pipelines, evaluation, G2P
- **Anyone** — share the project in Chechen-speaking communities

Open an issue or reach out if you'd like to contribute.

## License

MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements

- Meta AI for the [MMS project](https://ai.meta.com/blog/multilingual-model-speech-recognition/)
- The Chechen-speaking community
