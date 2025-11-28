import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import os
import datetime
import time
import re
import matplotlib.pyplot as plt
import numpy as np
import random
import json
import psutil
import subprocess
from pathlib import Path

REMINDERS_FILE = "reminders.txt"

contacts = {
    "mom": "+91XXXXXXXXXX",
    "dad": "+91XXXXXXXXXX",
    "rahul": "+91XXXXXXXXXX",
    "brother": "+91XXXXXXXXXX"
}

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

USE_MIC = True
try:
    if not sr.Microphone.list_microphone_names():
        USE_MIC = False
except:
    USE_MIC = False


def speak(text):
    print(f"Wednesday: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        pass


def listen(timeout=5, phrase_time_limit=6):
    if not USE_MIC:
        try:
            return input("You: ").strip().lower()
        except:
            return None
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.6)
            print("Listening…")
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            print("Recognizing…")
            return r.recognize_google(audio, language="en-IN").lower()
    except:
        return None


def normalize(t):
    return t.lower().strip() if t else ""


def extract_intent_and_target(text):
    INTENTS = [
        "send scheduled message", "list reminders", "clear reminders",
        "how are you", "set reminder", "remind", "open", "search",
        "play", "plot", "message", "close", "shutdown", "restart",
        "lock", "sleep", "exit", "stop", "goodnight"
    ]

    text = normalize(text)
    if not text:
        return None, None

    for intent in sorted(INTENTS, key=lambda x: -len(x)):
        if intent in text:
            parts = text.split(intent, 1)
            return intent, parts[1].strip() if len(parts) > 1 else ""

    for intent in ["open", "search", "play", "message", "close", "plot"]:
        m = re.search(rf"\b{intent}\b(?:\s+(.+))?", text)
        if m:
            return intent, (m.group(1) or "").strip()

    return None, text


def extract_numbers(text):
    try:
        return list(map(int, re.findall(r'\d+', text)))
    except:
        return []


def plot_bar_chart(vals):
    plt.figure()
    plt.bar(range(len(vals)), vals)
    plt.show()


def plot_line_graph(vals):
    plt.figure()
    plt.plot(vals, marker='o')
    plt.show()


def plot_sine():
    x = np.linspace(0, 10, 500)
    y = np.sin(x)
    plt.figure()
    plt.plot(x, y)
    plt.show()


def handle_plotting(target):
    vals = extract_numbers(target)
    if "bar" in target:
        if vals:
            plot_bar_chart(vals)
        else:
            speak("Provide numbers.")
    elif "line" in target:
        if vals:
            plot_line_graph(vals)
        else:
            speak("Provide numbers.")
    elif "sin" in target:
        plot_sine()
    else:
        speak("I can plot bar, line, or sine graphs.")


def send_instant_message(target):
    if not target:
        speak("Who should I message?")
        return

    name = next((c for c in contacts if c in target), None)
    if not name:
        speak("Contact not found.")
        return

    number = contacts[name]

    if "saying" in target:
        msg = target.split("saying", 1)[1].strip()
    else:
        msg = re.sub(name, "", target).replace("message", "").replace("to", "").strip()

    if not msg:
        speak("Message content required.")
        return

    try:
        pywhatkit.sendwhatmsg_instantly(number, msg, wait_time=10)
        speak(f"Message sent to {name}.")
    except:
        speak("WhatsApp failed.")


def send_scheduled_message(target):
    nums = extract_numbers(target)
    if len(nums) < 2:
        speak("Give hour and minute.")
        return

    hour, minute = nums[0], nums[1]

    name = next((c for c in contacts if c in target), None)
    if not name:
        speak("Contact not found.")
        return

    number = contacts[name]

    msg = re.sub(r'\d+|send|scheduled|message|to|at|' + name, '', target).replace("saying", "").strip()
    if not msg:
        speak("Message text missing.")
        return

    try:
        pywhatkit.sendwhatmsg(number, msg, hour, minute)
        speak(f"Scheduled message set for {name}.")
    except:
        speak("Schedule failed.")


def open_website(target):
    if not target:
        speak("What should I open?")
        return

    if "." in target:
        url = "https://" + target
    else:
        sites = {
            "youtube": "https://youtube.com",
            "google": "https://google.com",
            "github": "https://github.com"
        }
        url = sites.get(target, "https://www.google.com/search?q=" + target)

    speak(f"Opening {target}")
    try:
        webbrowser.open(url)
    except:
        speak("Couldn't open website.")


def close_browser():
    browsers = ["chrome.exe", "msedge.exe", "firefox.exe", "brave.exe", "opera.exe"]

    for proc in psutil.process_iter(['pid', 'name']):
        name = proc.info['name'].lower() if proc.info['name'] else ""
        if any(b in name for b in browsers):
            try:
                proc.kill()
            except:
                pass

    speak("Browser closed.")


APPS = {
    "notepad": r"notepad.exe",
    "calculator": r"calc.exe",
    "paint": r"mspaint.exe",
    "cmd": r"cmd.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
}

FOLDERS = {
    "downloads": os.path.expandvars(r"C:\Users\%USERNAME%\Downloads"),
    "documents": os.path.expandvars(r"C:\Users\%USERNAME%\Documents"),
    "desktop": os.path.expandvars(r"C:\Users\%USERNAME%\Desktop"),
    "pictures": os.path.expandvars(r"C:\Users\%USERNAME%\Pictures")
}


def open_app(command):
    for app in APPS:
        if app in command:
            speak(f"Opening {app}")
            try:
                subprocess.Popen(APPS[app])
            except:
                speak("Can't open app.")
            return

    for folder in FOLDERS:
        if folder in command:
            speak(f"Opening {folder}")
            try:
                os.startfile(FOLDERS[folder])
            except:
                speak("Can't open folder.")
            return

    speak("Not found.")


def close_app(command):
    for app in APPS:
        if app in command:
            speak(f"Closing {app}")
            for p in psutil.process_iter(['pid', 'name']):
                if app.lower() in p.info['name'].lower():
                    try:
                        p.kill()
                    except:
                        pass
            return

    for folder in FOLDERS:
        if folder in command:
            speak(f"Closing {folder}")
            os.system("taskkill /im explorer.exe /f")
            os.system("start explorer.exe")
            return

    if "browser" in command:
        close_browser()
        return

    speak("Nothing to close.")


def play_youtube(text):
    speak("Playing.")
    try:
        pywhatkit.playonyt(text)
    except:
        speak("Failed to play.")


def system_control(cmd):
    if "shutdown" in cmd:
        speak("Shutting down.")
        os.system("shutdown /s /t 3")
    elif "restart" in cmd:
        speak("Restarting.")
        os.system("shutdown /r /t 3")
    elif "lock" in cmd:
        speak("Locking system.")
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif "sleep" in cmd:
        speak("Sleeping.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


JOKES = [
    "Why did the programmer quit? Because he didn’t get arrays.",
    "My computer needed a break. So it went to sleep.",
    "I would tell you a UDP joke, but you might not get it."
]

FALLBACKS = ["Say that again.", "I didn't understand.", "Repeat please."]


def load_reminders():
    if not Path(REMINDERS_FILE).exists():
        return []
    try:
        with open(REMINDERS_FILE, "r") as f:
            return [json.loads(line) for line in f]
    except:
        return []


def save_reminders(data):
    with open(REMINDERS_FILE, "w") as f:
        for r in data:
            f.write(json.dumps(r) + "\n")


def add_reminder(text):
    now = datetime.datetime.now()
    nums = extract_numbers(text)

    if len(nums) >= 2:
        hour, minute = nums[0], nums[1]
    else:
        future = now + datetime.timedelta(minutes=5)
        hour, minute = future.hour, future.minute

    msg = re.sub(r'\d+|reminder|set|at|in|minutes', '', text).strip()
    if not msg:
        msg = "Reminder"

    t = datetime.datetime(now.year, now.month, now.day, hour % 24, minute % 60)
    if t <= now:
        t += datetime.timedelta(days=1)

    data = load_reminders()
    data.append({
        "time": t.strftime("%Y-%m-%d %H:%M"),
        "msg": msg,
        "done": False
    })
    save_reminders(data)
    speak("Reminder added.")


def check_reminders():
    now = datetime.datetime.now()
    data = load_reminders()
    changed = False

    for r in data:
        try:
            if not r["done"] and now >= datetime.datetime.strptime(r["time"], "%Y-%m-%d %H:%M"):
                speak("Reminder: " + r["msg"])
                r["done"] = True
                changed = True
        except:
            pass

    if changed:
        save_reminders(data)


def list_reminders():
    data = [r for r in load_reminders() if not r["done"]]
    if not data:
        speak("No pending reminders.")
        return

    for r in data:
        speak(r["time"] + " → " + r["msg"])


def greeting():
    h = datetime.datetime.now().hour
    if h < 12:
        speak("Good morning.")
    elif h < 17:
        speak("Good afternoon.")
    else:
        speak("Good evening.")


def run_assistant():
    speak("Wednesday online.")
    greeting()
    check_reminders()

    while True:
        check_reminders()
        text = listen()

        if not text:
            speak(random.choice(FALLBACKS))
            continue

        if "hello wednesday" in text:
            speak("Hello. I'm listening.")
            continue

        if "how are you" in text:
            speak("Running smoothly.")
            continue

        if "joke" in text:
            speak(random.choice(JOKES))
            continue

        if "time" in text:
            speak(datetime.datetime.now().strftime("%I:%M %p"))
            continue

        if "date" in text:
            speak(datetime.datetime.now().strftime("%A, %d %B %Y"))
            continue

        if "remind" in text:
            add_reminder(text)
            continue

        if "list reminders" in text:
            list_reminders()
            continue

        if "clear reminders" in text:
            save_reminders([])
            speak("All reminders cleared.")
            continue

        if "send scheduled message" in text:
            send_scheduled_message(text)
            continue

        if "message" in text:
            send_instant_message(text)
            continue

        if "plot" in text:
            handle_plotting(text)
            continue

        if "open" in text:
            if any(a in text for a in APPS.keys() | FOLDERS.keys()):
                open_app(text)
            else:
                t = text.replace("open", "").strip()
                open_website(t)
            continue

        if "close" in text:
            close_app(text)
            continue

        if "search" in text:
            q = text.replace("search", "").strip()
            if q:
                speak("Searching.")
                pywhatkit.search(q)
            else:
                speak("What should I search?")
            continue

        if "play" in text:
            play_youtube(text.replace("play", "").strip())
            continue

        if any(x in text for x in ["shutdown", "restart", "lock", "sleep"]):
            system_control(text)
            continue

        if any(x in text for x in ["exit", "stop", "bye", "goodnight"]):
            speak("Goodnight. Wednesday powering off.")
            break

        speak(random.choice(FALLBACKS))


run_assistant()
