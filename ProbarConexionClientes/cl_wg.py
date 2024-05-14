import subprocess


print("WG show wg0")
print(subprocess.run(["wg", "show"]))