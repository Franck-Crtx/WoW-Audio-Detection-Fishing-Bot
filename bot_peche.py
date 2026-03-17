import pyaudio
import numpy as np
import pyautogui
import time
import random

THRESHOLD = 300       
INPUT_ID = 3          
KEY_FISHING = '<'
KEY_SIT = 'x'         

stats = {
    "tentatives": 0,
    "reussites": 0,
    "fails_volontaires": 0,
    "temps_reactions": [],
    "start_time": time.time()
}

p = pyaudio.PyAudio()

def human_behavior():
    rand = random.random() * 100 
    if rand < 10:
        print("🎒 Tiens, j'ai quoi dans mes sacs ?")
        pyautogui.keyDown('shift'); pyautogui.press('b'); pyautogui.keyUp('shift')
        time.sleep(random.uniform(8.0, 15.0))
        pyautogui.keyDown('shift'); pyautogui.press('b'); pyautogui.keyUp('shift')
        time.sleep(1.5)

    if 10 <= rand < 14: 
        print("🦵 On se dégourdit les jambes...")
        touche_mvt = random.choice(['z', 's', 'q', 'd'])
        pyautogui.keyDown(touche_mvt); time.sleep(random.uniform(0.1, 0.2)); pyautogui.keyUp(touche_mvt)
        time.sleep(1.5)
        pyautogui.press(KEY_SIT)
        time.sleep(2)

def pecher():
    stats["tentatives"] += 1
    time.sleep(random.uniform(0.8, 1.8))
    human_behavior()

    print(f"\n🎣 Lancement n°{stats['tentatives']}...")
    pyautogui.press(KEY_FISHING)
    time.sleep(2.2)
    
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, 
                    input=True, input_device_index=INPUT_ID, 
                    frames_per_buffer=512)
    
    listen_start = time.time()
    try:
        while (time.time() - listen_start) < 21:
            data = stream.read(512, exception_on_overflow=False)
            vol = np.max(np.abs(np.frombuffer(data, dtype=np.int16)))

            if vol > THRESHOLD:
                if random.random() < 0.10:
                    print("🤡 Oups, j'ai raté le poisson (Missclick simulé) !")
                    stats["fails_volontaires"] += 1
                    time.sleep(random.uniform(3, 6))
                    return False

                reaction = random.uniform(0.18, 0.45)
                stats["temps_reactions"].append(reaction)
                stats["reussites"] += 1
                
                print(f"🐟 FERRÉ ! ({int(reaction*1000)}ms)")
                time.sleep(reaction)
                pyautogui.press(KEY_FISHING)
                time.sleep(random.uniform(1.2, 2.5)) 
                return True
    except Exception as e:
        print(f"Erreur flux : {e}")
    finally:
        stream.stop_stream()
        stream.close()
    return False

def afficher_stats():
    duree_totale = time.time() - stats["start_time"]
    minutes = int(duree_totale // 60)
    secondes = int(duree_totale % 60)
    
    avg_reaction = (sum(stats["temps_reactions"]) / len(stats["temps_reactions"]) * 1000) if stats["temps_reactions"] else 0
    taux_reussite = (stats["reussites"] / stats["tentatives"] * 100) if stats["tentatives"] > 0 else 0

    print("\n" + "="*40)
    print(f"     📊 RÉCAPITULATIF DE LA SESSION")
    print("="*40)
    print(f"⏱️  Durée : {minutes}min {secondes}s")
    print(f"🎣 Lancers totaux : {stats['tentatives']}")
    print(f"✅ Poissons ferrés : {stats['reussites']}")
    print(f"🤡 Fails simulés : {stats['fails_volontaires']}")
    print(f"📊 Taux de réussite : {taux_reussite:.1f}%")
    print(f"⚡ Réaction moyenne : {int(avg_reaction)}ms")
    print("="*40)

if __name__ == "__main__":
    try:
        print("===== BOT PÊCHE 'HUMAN-MIMIC' V1.1 =====")
        while True:
            pecher()
    except KeyboardInterrupt:
        afficher_stats()
        print("\nArrêt propre. À bientôt !")
        print(f"©️  Franck-Crtx 2026")
        p.terminate()
