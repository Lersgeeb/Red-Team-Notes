# Verify

## Detalles Máquina
- **H1.** La maquina contenía 3 archivos/folders principales al momento de acceder mediante SSH: `checksum.txt`, `decrypt.sh`. `files/` este ultimo siendo una carpeta con multiples archivos con nombres aleatorios
- **H2.** El objetivo del laboratorio es obtener el archivo "Legítimo" entre todos los archivos existentes en la carpeta `files/` 
- **H3.** El archivo `checksum.txt` contiene la firma en SHA256 del archivo que estamos buscando.
- **H4.** Se ejecuta un comando para realizar la validación en todos los archivos y obtener directamente el legítimo 
- **H5.** Se usa el archivo `decrypt.sh` sobre el archivo legítimo para obtener el Flag del laboratorio

## Comandos útiles 

Comando utilizado en bash para realizar el Checksum en los archivos existentes (H4)
```bash
for f in ./files/*; do sha256sum "$f"; done | grep -Ff checksum.txt

# output:
# fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7  ./files/87590c24
```

Comando utilizado para obtener el Flag (H5)
```bash
./decrypt.sh ./files/87590c24 

# output:
# picoCTF{trust_but_verify_87590c24}
```

## Tags
- Forensics
- checksum
- bash
- sha256