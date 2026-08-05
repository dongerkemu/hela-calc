with open(r'D:\hela-calc\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.index('<script>')
end = content.index('</script>')
js = content[start:end]
lines = js.split('\n')

print("=== Backtick count ===")
bt = js.count('`')
print(f"Total: {bt}")
if bt % 2 != 0:
    print("ODD - UNMATCHED BACKTICKS!")
    # Find which line has unbalanced
    count = 0
    for i, line in enumerate(lines, 1):
        for ch in line:
            if ch == '`':
                count += 1
        if count % 2 == 1:
            print(f"  Open after line {start+i}: {line.strip()[:100]}")

print("\n=== Functions ===")
import re
for m in re.finditer(r'function (\w+)\(', js):
    print(f"  {m.group(1)}")

print("\n=== Checking calcMonthlyRate (uses calcMonthlyNet without withFee) ===")
idx = js.find('function calcMonthlyRate')
if idx > 0:
    end_idx = js.index('\n}', idx) + 2
    print(js[idx:end_idx])

print("\n=== Checking renderAll ===")
idx = js.find('function renderAll')
if idx > 0:
    end_idx = js.index('\n}', idx) + 2
    print(js[idx:end_idx])

print("\n=== Variables used in renderSummary ===")
idx = js.find('function renderSummary')
if idx > 0:
    end_idx = js.index('\n}', idx) + 2
    snippet = js[idx:end_idx]
    # Check what's defined before use
    for line in snippet.split('\n'):
        s = line.strip()
        if 'const ' in s:
            print(f"  DEF: {s[:100]}")
        if 'days' in s.lower() and 'const ' not in s:
            print(f"  USE days: {s[:120]}")
