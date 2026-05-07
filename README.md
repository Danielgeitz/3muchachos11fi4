# 3muchachos11fi4

# Projekt Setup Anleitung

Dieses Projekt verwendet eine Python Virtual Environment (`venv`) zur Verwaltung der Abhängigkeiten (Dependencies).

## 1. Virtuelle Umgebung erstellen

```bash
python -m venv .venv
```

## 2. Virtuelle Umgebung aktivieren

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Nach der Aktivierung sollte `(.venv)` am Anfang der Terminalzeile angezeigt werden.

---

## 3. Installierte Abhängigkeiten speichern / aktualisieren

Um alle installierten Python-Pakete in einer `requirements.txt` Datei zu speichern / aktualisieren:

```bash
pip freeze > requirements.txt
```

---

## 4. Abhängigkeiten installieren

Um alle Abhängigkeiten aus der `requirements.txt` Datei zu installieren:

```bash
pip install -r requirements.txt
```

---

## 5. Virtuelle Umgebung deaktivieren

Wenn du mit dem Projekt fertig bist:

```bash
deactivate
```