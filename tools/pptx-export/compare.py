"""compare.py HARVEST KEYNOTE_DIR OUTPREFIX [indices...] — side-by-side browser | keynote pairs"""
import glob, os, sys
from PIL import Image, ImageDraw
harvest, kn, prefix = sys.argv[1:4]
refs = sorted(glob.glob(os.path.join(harvest, '*_ref.png')), key=lambda f: [int(x) for x in os.path.basename(f).split('_')[:3]])
kns = sorted(glob.glob(os.path.join(kn, '*.png')), key=lambda f: int(''.join(ch for ch in os.path.basename(f).split('.')[-2] if ch.isdigit())))
idx = [int(i) - 1 for i in sys.argv[4:]] or range(len(refs))
W, H = 960, 540
pairs = [(i, refs[i], kns[i]) for i in idx]
for page in range(0, len(pairs), 3):
    chunk = pairs[page:page + 3]
    sheet = Image.new('RGB', (2 * W + 10, len(chunk) * (H + 10)), 'red')
    for r, (i, a, b) in enumerate(chunk):
        sheet.paste(Image.open(a).convert('RGB').resize((W, H)), (0, r * (H + 10)))
        sheet.paste(Image.open(b).convert('RGB').resize((W, H)), (W + 10, r * (H + 10)))
        ImageDraw.Draw(sheet).text((5, r * (H + 10) + 5), str(i + 1), fill='red')
    sheet.save(f'{prefix}_{page // 3}.png')
    print(f'{prefix}_{page // 3}.png')
