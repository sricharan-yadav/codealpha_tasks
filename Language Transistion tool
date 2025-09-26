import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from deep_translator import GoogleTranslator
from gtts import gTTS
import speech_recognition as sr
import os
import playsound

# Function: Translate text
def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    src_lang = source_lang.get()
    tgt_lang = target_lang.get()

    if not text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    try:
        translated = GoogleTranslator(source=src_lang, target=tgt_lang).translate(text)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
        output_text.config(state=tk.DISABLED)

        # Save translation to file
        save_translation(text, translated, src_lang, tgt_lang)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

# Save translations in history file
def save_translation(original, translated, src, tgt):
    with open("translation_history.txt", "a", encoding="utf-8") as f:
        f.write(f"From ({src}) -> ({tgt})\n")
        f.write(f"Input: {original}\n")
        f.write(f"Output: {translated}\n")
        f.write("-" * 40 + "\n")

# Function: Copy translated text
def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END).strip())
    messagebox.showinfo("Copied", "Translated text copied to clipboard!")

# Function: Speak translated text (TTS)
def speak_text():
    text = output_text.get("1.0", tk.END).strip()
    lang = target_lang.get()
    if not text:
        messagebox.showwarning("Warning", "No text to speak!")
        return
    try:
        tts = gTTS(text=text, lang=lang)
        filename = "tts_output.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        messagebox.showerror("Error", f"Text-to-Speech failed: {e}")

# Function: Speech-to-Text input
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Listening", "Speak now...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, text)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand audio")
        except sr.RequestError:
            messagebox.showerror("Error", "Speech recognition service unavailable")
        except Exception as e:
            messagebox.showerror("Error", f"Speech-to-Text failed: {e}")

# GUI Setup
root = tk.Tk()
root.title("Language Translator Tool")
root.geometry("600x500")

# Language dropdowns (use ISO codes)
langs = ["en", "hi", "te", "fr", "es", "de", "ta", "ja", "ko", "zh-cn"]  # you can add more
lang_names = {
    "en": "English", "hi": "Hindi", "te": "Telugu", "fr": "French",
    "es": "Spanish", "de": "German", "ta": "Tamil", "ja": "Japanese",
    "ko": "Korean", "zh-cn": "Chinese"
}

source_lang = tk.StringVar(value="en")
target_lang = tk.StringVar(value="te")

ttk.Label(root, text="Source Language:").pack(pady=5)
src_menu = ttk.Combobox(root, textvariable=source_lang, values=langs, width=15)
src_menu.pack()

ttk.Label(root, text="Target Language:").pack(pady=5)
tgt_menu = ttk.Combobox(root, textvariable=target_lang, values=langs, width=15)
tgt_menu.pack()

# Input text area
ttk.Label(root, text="Enter Text:").pack(pady=5)
input_text = scrolledtext.ScrolledText(root, height=5, wrap=tk.WORD)
input_text.pack(padx=10, pady=5, fill=tk.BOTH)

# Translate button
ttk.Button(root, text="Translate", command=translate_text).pack(pady=5)

# Output text area
ttk.Label(root, text="Translated Text:").pack(pady=5)
output_text = scrolledtext.ScrolledText(root, height=5, wrap=tk.WORD, state=tk.DISABLED)
output_text.pack(padx=10, pady=5, fill=tk.BOTH)

# Buttons frame
frame = tk.Frame(root)
frame.pack(pady=10)

ttk.Button(frame, text="Copy", command=copy_text).grid(row=0, column=0, padx=5)
ttk.Button(frame, text="Speak", command=speak_text).grid(row=0, column=1, padx=5)
ttk.Button(frame, text="🎤 Speak Input", command=speech_to_text).grid(row=0, column=2, padx=5)

root.mainloop()
