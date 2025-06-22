# Installation

Die benötigten Pakete sind in `requirements.txt`. Es wird empfohlen, eine virtuelle Umgebung zu verwenden, um Konflikte
mit anderen Python-Projekten zu vermeiden. Die Datei `conda-environment.yml` enthält die Abhängigkeiten für die
Anaconda-Installation. Alternativ kann auch die Python-eigene `venv`-Umgebung verwendet werden.

### Installation über Anaconda:

```bash
conda env create -f conda-environment.yml
conda activate klimawandel-kurs
pip install -r requirements.txt
```

### Installation über Python-venv

```bash
# Create virtual environment
python -m venv venv  # ggf. python3 anstelle von python verwenden
source venv/bin/activate

# Upgrade pip and install packages
pip install --upgrade pip
pip install -r requirements.txt
```