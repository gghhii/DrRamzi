import os
import glob

files = glob.glob(r'c:\Users\ThinkPad L590\Documents\drramzi\Views\Home\*.cshtml')

reps = {
    'Kantaoui Medical Center<br>Bloc A, 5ème Étage<br>Hammam Sousse, Sousse': 'Immeuble Misk Elil<br>4ème Étage, Bureau N°42<br>Khézama Est, Sousse',
    'T. +216 20 402 049<br>E. ash.laroussi@yahoo.fr': 'T. +216 98 643 807<br>E. moatemri_ramzi@yahoo.fr'
}

for f in files:
    content = None
    try:
        with open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
    except UnicodeDecodeError:
        with open(f, 'r', encoding='windows-1252') as file:
            content = file.read()
            
    if not content: continue
        
    original = content
    for k, v in reps.items():
        content = content.replace(k, v)
        
    if content != original:
        try:
            with open(f, 'w', encoding='utf-8-sig') as file:
                file.write(content)
        except Exception:
            with open(f, 'w', encoding='windows-1252') as file:
                file.write(content)
        print(f'Updated {os.path.basename(f)}')

print('Done!')
