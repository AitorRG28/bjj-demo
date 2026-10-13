"""Genera index.html (producción) o una versión contra emuladores: python3 src/build.py [--emu salida.html]"""
import sys, pathlib
src = pathlib.Path(__file__).parent
html = (src / 'app.template.html').read_text().replace('/*BASECSS*/', (src / 'base.css').read_text())
emu = '--emu' in sys.argv
rep = {'/*EMU_AUTH_IMPORT*/': ',connectAuthEmulator' if emu else '',
       '/*EMU_FS_IMPORT*/': ',connectFirestoreEmulator' if emu else '',
       '/*EMU_CONNECT*/': "connectAuthEmulator(auth,'http://127.0.0.1:9099');connectFirestoreEmulator(db,'127.0.0.1',8080);" if emu else ''}
for k, v in rep.items(): html = html.replace(k, v)
out = pathlib.Path(sys.argv[sys.argv.index('--emu') + 1]) if emu else src.parent / 'index.html'
out.write_text(html); print('OK ->', out)
