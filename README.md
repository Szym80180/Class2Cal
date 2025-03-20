# Class2Cal

Przenieś swój kalendarz z Systemu Informacji Studenckiej bezpośrednio do Kalendarza Google.
---

**Spis treści / Table of Contents:**

### Wersja polska
1. [Przegląd](#przegląd)
2. [Wymagania](#wymagania)
3. [Instrukcja uruchomienia](#instrukcja-uruchomienia)
4. [Rozwiązywanie problemów](#rozwiązywanie-problemów)
5. [Licencja i wsparcie](#licencja-i-wsparcie)
6. [Zgłaszanie błędów i propozycje poprawek](#zgłaszanie-błędów-i-propozycje-poprawek)

### English Version
7. [Overview](#overview)
8. [Requirements](#requirements)
9. [Setup Instructions](#setup-instructions)
10. [Troubleshooting](#troubleshooting)
11. [License and Support](#license-and-support)
12. [Reporting Issues and Contributions](#reporting-issues-and-contributions)

---
## Przegląd
Class2Cal to proste narzędzie umożliwiające migrację wydarzeń z kalendarza studenckiego do Kalendarza Google. Możesz wybrać uruchomienie programu z poziomu kodu lub skorzystać z dostarczonego pliku wykonywalnego (.exe).

## Wymagania
- **Python 3.11** (jeśli uruchamiasz program ze źródeł)
- Edytor kodu (jeśli uruchamiasz program ze źródeł)
- Projekt w Google Cloud z włączonym API Kalendarza
- Plik `credentials.json` zawierający dane uwierzytelniające Google API

## Instrukcja uruchomienia

### Opcja 1: Uruchamianie ze źródeł
Jeśli nie ufasz plikowi `.exe`, możesz uruchomić program bezpośrednio z kodu.

1. **Pobierz pliki projektu.**
2. Otwórz terminal i zainstaluj zależności: `pip install -r requirements.txt`
3. **Utwórz projekt w Google Cloud** oraz włącz API Kalendarza. Szczegółową instrukcję znajdziesz [tutaj](https://developers.google.com/calendar/api/quickstart/python).
4. Pobierz dane uwierzytelniające i zapisz je w pliku `credentials.json` w katalogu projektu.
5. Uruchom program.
6. Zaloguj się na konto Google, do którego chcesz dodać kalendarz.
7. Postępuj zgodnie z wyświetlanymi zapytaniami i podawaj wymagane informacje.  
Aby zobaczyć dostępne kolory, sprawdź sekcję [Modern colors](https://google-calendar-simple-api.readthedocs.io/en/latest/colors.html).
8. **Sprawdź**, czy kalendarz został poprawnie przepisany.

### Opcja 2: Uruchamianie za pomocą pliku wykonywalnego (.exe)
1. **Pobierz najnowszą wersję pliku wykonywalnego** z sekcji Releases.
2. Uruchom program.
3. Zaloguj się na konto Google, do którego chcesz dodać kalendarz.
4. Postępuj zgodnie z wyświetlanymi zapytaniami i podawaj wymagane informacje.  
Aby zobaczyć dostępne kolory, sprawdź sekcję [Modern colors](https://google-calendar-simple-api.readthedocs.io/en/latest/colors.html).
5. **Sprawdź**, czy kalendarz został poprawnie przepisany.

## Rozwiązywanie problemów
- **Problemy z autoryzacją:** Upewnij się, że plik `credentials.json` jest poprawny oraz że API Kalendarza jest włączone w Twoim projekcie Google Cloud.
- **Problemy z zależnościami:** Sprawdź, czy używasz Pythona w wersji 3.11 oraz czy wszystkie moduły zostały poprawnie zainstalowane.
- W razie problemów lub błędów, odwiedź naszą stronę Issues na GitHubie lub skontaktuj się z autorem projektu (Discord: Szym80180).


## Licencja i wsparcie
- Projekt Class2Cal jest udostępniany do bezpłatnego użytku wyłącznie w celach niekomercyjnych.  
**Zastrzeżenia:**
- Zabrania się komercyjnego wykorzystywania tego projektu.
- W przypadku redystrybucji kodu, autorzy redystrybucji zobowiązani są do zachowania informacji o oryginalnym autorze (np. poprzez umieszczenie stosownego nagłówka lub notatki w kodzie źródłowym). 
Szczegóły dotyczące licencji znajdziesz w pliku LICENSE.
- Aby uzyskać wsparcie lub sprawdzić aktualizacje, odwiedź sekcję Releases lub repozytorium projektu.


## Zgłaszanie błędów i propozycje poprawek
Chętnie przyjmuję zgłoszenia wszelkich błędów oraz propozycje poprawek, aby projekt Class2Cal mógł się stale rozwijać i lepiej służyć społeczności studenckiej.

Jeśli natkniesz się na błąd lub problem, proszę zgłoś go poprzez sekcję [Issues](https://github.com/Szym80180/Class2Cal/issues) w repozytorium GitHub.

Jeśli masz pomysł na poprawę lub chcesz samodzielnie wprowadzić zmiany, zachęcam do tworzenia pull requestów.
Twoje propozycje i wkład w rozwój projektu są bardzo mile widziane!

---

## Overview
Class2Cal is a simple tool designed to migrate events from your Student Information System calendar directly to Google Calendar. You can choose to run the program from the source code or use the provided executable (.exe).

## Requirements
- **Python 3.11** (if running the program from source)
- A code editor (if running the program from source)
- A Google Cloud project with the Calendar API enabled
- A `credentials.json` file containing your Google API authentication data

## Setup Instructions

### Option 1: Running from Source
If you prefer not to use the `.exe` file, you can run the program directly from the source code.

1. **Download the project files.**
2. Open your terminal and install the dependencies: `pip install -r requirements.txt`
3. **Create a project in Google Cloud** and enable the Calendar API. Follow the detailed instructions [here](https://developers.google.com/calendar/api/quickstart/python).
4. Download your authentication credentials and save them as `credentials.json` in the project directory.
5. Run the program.
6. Log in to the Google account where you want to add the calendar.
7. Follow the program prompts and provide the required information.  
For available color options, check the [Modern colors](https://google-calendar-simple-api.readthedocs.io/en/latest/colors.html) section.
8. **Verify** that the calendar has been correctly imported.

### Option 2: Running with the Executable (.exe)
1. **Download the latest executable** from the Releases section.
2. Run the program.
3. Log in to the Google account where you want to add the calendar.
4. Follow the program prompts and provide the required information.  
For available color options, check the [Modern colors](https://google-calendar-simple-api.readthedocs.io/en/latest/colors.html) section.
5. **Verify** that the calendar has been correctly imported.

## Troubleshooting
- **Authorization issues:** Ensure that your `credentials.json` file is correct and that the Calendar API is enabled in your Google Cloud project.
- **Dependency issues:** Check that you are using Python 3.11 and that all required modules are installed.

## License and Support
- Class2Cal is provided free of charge for non-commercial use only.  
**Restrictions:**
- Commercial use of this project is prohibited.
- In case of code redistribution, redistributors are required to retain information about the original author (e.g., by including an appropriate header or note in the source code).  
Detailed license information can be found in the LICENSE file.
- For support or to check for updates, please visit the Releases section or the project repository.

## Reporting Issues and Contributions
We welcome any bug reports and suggestions for improvements to help Class2Cal evolve and better serve the student community.

If you encounter an error or problem, please report it via the [Issues](https://github.com/Szym80180/Class2Cal/issues) section on GitHub.

If you have suggestions for improvements or wish to contribute code, feel free to create a pull request.

Your contributions and feedback are greatly appreciated!

---

