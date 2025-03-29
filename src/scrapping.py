from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.edge.service import Service


def which_color(string):
    pink, orange, blue, yellow = 'pink', 'orange', 'blue', 'yellow'
    if string.find(pink)!=-1:
        color=pink
    elif string.find(orange)!=-1:
        color=orange
    elif string.find(blue)!=-1:
        color=blue
    elif string.find(yellow)!=-1:
        color=yellow
    else:
        color="error"
    return color

def scrap_notes():
# Setze den Pfad zu deinem WebDriver (z. B. EdgeDriver)
    driver_path = r"C:\Users\Benja\Code\Python\msedgedriver.exe"

    service = Service(driver_path)  # Service-Objekt für den EdgeDriver
    driver = webdriver.Edge(service=service)  # Korrekte Initialisierung

    # Starte den WebDriver
    # driver = webdriver.Edge(driver_path)

    # Öffne die Kindle Notizen-Seite
    driver.get("https://lesen.amazon.de/notebook?ref_=kcr_notebook_lib&language=de-DE")

    # Warte auf die Anmeldung
    time.sleep(10)  # Falls du dich manuell anmelden muszenzst

    # Warte, bis die Notizen geladen sind
    time.sleep(5)

    # Suche alle Notizen-Elemente (kann je nach HTML-Struktur variieren)
    notizen = driver.find_elements(By.CLASS_NAME, "kp-notebook-highlight")

    all_notes = []
    for notiz in notizen:
        text = notiz.text  # Text der Markierung
        farbe = which_color(notiz.get_attribute("class"))    
        all_notes.append([farbe, text])

    # Browser schließen
    driver.quit()
    return all_notes


def sort_notes(notes, color):
    new_notes = []
    for note in notes:
        if note[0] == color:
            new_notes.append(note[1])
    return new_notes