import os
import glob

files = glob.glob(r'c:\Users\ThinkPad L590\Documents\drramzi\Views\Home\*.cshtml')

reps = {
    '<div class="mf-background-text">PR. MOATEMRI</div>': '<div class="mf-background-text">DR. MOATEMRI</div>',
    '<span class="mf-logo">LES JASMINS</span>': '<span class="mf-logo">DR RAMZI MOATEMRI</span>',
    '<span class="mf-tagline">CHIRURGIE MAXILLO-FACIALE & ESTHÉTIQUE</span>': '<span class="mf-tagline">CHIRURGIEN MAXILLO-FACIAL ET ESTHÉTIQUE</span>',
    '<span>© 2026 LES JASMINS</span>': '<span>© 2026 DR RAMZI MOATEMRI</span>',
    '<div class="mf-management">DIRECTION : PROFESSEUR RAMZI MOATEMRI</div>': '<div class="mf-management">DIRECTION MÉDICALE : DR RAMZI MOATEMRI</div>',
    '<div class="mf-background-text">LES JASMINS</div>': '<div class="mf-background-text">DR. MOATEMRI</div>'
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
