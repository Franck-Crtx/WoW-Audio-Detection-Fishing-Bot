# 🎣 WoW Audio Fishing Bot
Un bot de pêche intelligent pour World of Warcraft, basé sur la détection du flux audio. Ce script permet d'automatiser la pêche de manière sécurisée en isolant le son du jeu.

## ✨ Points forts
- Human-Mimic Engine :
  - Délais de réaction aléatoires (180ms - 450ms).
  - Taux d'échec simulé (10%) pour éviter les patterns mathématiques parfaits.
  - Actions humaines : Ouverture aléatoire des sacs (`Maj+B`) et micro-mouvements anti-AFK.
- Statistiques de Session : Récapitulatif complet à l'arrêt du script (Taux de réussite, temps de réaction moyen).

## 🛠️ Installation
1 - Python : Assurez-vous d'avoir Python 3.8+ installé.
2 - Dépendances : Installez les bibliothèques nécessaires via votre terminal :

```
$> pip install pyaudio numpy pyautogui
```

3 - Configuration WoW :

- Activez la Fouille Automatique dans les options du jeu.
- (Optionnel) Utilisez l'addon Better Fishing pour lier la pêche à une seule touche (par défaut `<` dans le script).

## 🎧 Configuration Audio (Crucial)
Pour que le bot soit fiable et ne réagisse pas aux sons parasites (vidéos, musique, chat vocal) :

1 - Dans les paramètres Windows, isolez le son de WoW sur un canal spécifique ou utilisez un mixeur virtuel.
2 - Assurez-vous que le périphérique écouté par le script ne reçoit que les sons provenant du jeu.

## 🚀 Utilisation
### Étape 1 : Trouver votre ID Audio
Lancez le script de diagnostic pour identifier l'ID du périphérique audio que vous souhaitez écouter :

```
$> python canal.py
```
Notez l'ID correspondant à votre sortie audio de jeu.

### Étape 2 : Lancer le Bot
1 - Modifiez la variable `INPUT_ID` dans `bot_peche.py` avec l'ID trouvé précédemment.
2 - Lancez le bot :

```
$> python bot_peche.py
```
3 - Basculez sur WoW et placez votre personnage devant un point d'eau.

## 📊 Statistiques
À l'arrêt du script (Ctrl+C), un rapport détaillé s'affiche :

- Durée de la session.
- Nombre de lancers réussis vs Fails simulés.
- Temps de réaction moyen (permet d'ajuster les délais pour plus de réalisme).

## ⚖️ Licence & Copyright
Ce projet est sous licence MIT.

© 2026 Franck-Crtx.

Avertissement : L'utilisation de scripts d'automatisation peut être soumise à des sanctions de la part de l'éditeur du jeu. Utilisez ce bot de manière responsable et modérée.
