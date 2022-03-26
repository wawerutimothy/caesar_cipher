def CaesarEncrypt(message,shift):
	final_result = ""
	for i in range(len(message)):
		char = message[i]
		if (char.isupper()):
			final_result += chr((ord(char) + shift-65) % 26 + 65)
		else:
			final_result += chr((ord(char) + shift - 97) % 26 + 97)
	return final_result

message = "He went home yesternight"
shift = 8
print ("Cipher: " + CaesarEncrypt(message,shift))
print ("Message : " + message)
