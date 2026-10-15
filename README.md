# Milas Zeitreise – Hörabenteuer

Interaktive Schatzsuche in Neckartailfingen mit 29 Szenen und Milas Erzählstimme.

## Veröffentlichung (GitHub Pages)

1. Ein **öffentliches** GitHub-Repository `milas-zeitreise` erstellen (Standardbranch `main`).
2. Alle Dateien **aus diesem Ordner** in das Repository hochladen, einschließlich `.github/workflows/pages.yml` und `tools/bootstrap_audio.py`.
3. Unter **Settings → Pages → Build and deployment → Source** die Option **GitHub Actions** auswählen.
4. Unter **Actions** den Workflow **Milas Zeitreise veroeffentlichen** starten, sofern er nicht automatisch läuft.
5. Erfolgreicher Lauf lädt 29 Original-MP3s herunter, speichert sie im Repository und stellt die Seite bereit.
6. Die Webseite ist dann unter `https://<github-benutzername>.github.io/milas-zeitreise/` erreichbar.

**Wichtig:** Die Audioquellen sind nur kurzfristig erreichbar. Den allerersten Workflow möglichst sofort ausführen. Wenn die Links bereits abgelaufen sind, gelingt die Sicherung nicht mehr. Ohne MP3s fällt die Seite auf die synthetische Handy-Stimme zurück.

**Privatsphäre:** Ein öffentliches GitHub-Repository zeigt HTML-Quelltext und Hörtexte öffentlich. Die Geschichte enthält Ortsnamen aus Neckartailfingen, aber keine private Hausnummer. Die MP3s werden ebenfalls öffentlich erreichbar sein.

**Technik:** Keine Benutzerkonten, keine externen Trackingdienste. Der Fortschritt wird lokal im Browser gespeichert. Das Spiel speichert auf Wunsch Audiodateien im Browser (IndexedDB), sofern unterstützt.
