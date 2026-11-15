data = input("Enter data: ")
gen = input("Enter generator: ")
n = len(gen)

def crc(bits):
    bits = list(bits)
    for i in range(len(bits) - n + 1):
        if bits[i] == "1":
            for j in range(n):
                bits[i+j] = "0" if bits[i+j] == gen[j] else "1"
    return "".join(bits[-(n-1):])

r = crc(data + "0" * (n-1))
print("CRC Remainder:", r)
print("Transmitted Codeword:", data + r)

rec = input("Enter received codeword: ")
if "1" in crc(rec):
    print("Error detected in received data.")
else:
    print("No error detected. Data received correctly.")