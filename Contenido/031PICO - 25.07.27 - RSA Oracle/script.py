from Crypto.Util.number import getPrime , long_to_bytes           


m2 = "2"
c_pwd = 4228273471152570993857755209040611143227336245190875847649142807501848960847851973658239485570030833999780269457000091948785164374915942471027917017922546
c2 = 4707619883686427763240856106433203231481313994680729548861877810439954027216515481620077982254465432294427487895036699854948548980054737181231034760249505

m2_hex = m2.encode().hex()
print(f"m2: {m2} (hex: {m2_hex})")

c_fake = c_pwd*c2
print(f"c_fake: {c_fake})")

m2 = '2'
m_fake = 'ûk-"'

m_fake_hex = "139afb6b2d22"
pwd_int = int(m_fake_hex, 16) // 2          # división entera
pwd_hex = f"{pwd_int:0x}"                   # → 9cd7db59691
if len(pwd_hex) % 2:                        # longitud par para bytes
    pwd_hex = "0" + pwd_hex                 # → 09cd7db59691
password = bytes.fromhex(pwd_hex)           # b'\t\xcd}\xb5\x96\x91'
print("hex:", pwd_hex)
print("raw bytes:", password)

# c = m^e mod n
# n = p * q
# m = c + nk
# (m - c )/k = n



