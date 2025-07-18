# Reconocimiento
> Información  obtenida de [Passive Reconnaissance](https://tryhackme.com/room/passiverecon)

Si está jugando el papel de un atacante, necesita recopilar información sobre sus sistemas de destino. Si está desempeñando el papel de defensor, necesita saber qué descubrirá su adversario sobre sus sistemas y redes.

**Tipos de reconocimiento**
- **Pasivo:** Información pública y puede ser obtenida sin comprometerse directamente con el objetivo.
- **Activo:** No se puede lograr tan discretamente. Requiere compromiso directo con el objetivo.

## Comandos útiles
- **whois:** Un servidor WHOIS escucha en el puerto TCP 43 las solicitudes entrantes (RFC 3912)
- **nslookup** (Name Server Look Up.)
- **dig** (Domain Information Groper)

| Proposito      | Comando |
| ----------- | ----------- |
| Lookup WHOIS record | `whois tryhackme.com`
| Lookup DNS A records | `nslookup -type=A tryhackme.com`
| Lookup DNS MX records at DNS server | `nslookup -type=MX tryhackme.com 1.1.1.1`
| Lookup DNS TXT records | `nslookup -type=TXT tryhackme.com`
| Lookup DNS A records | `dig tryhackme.com A`
| Lookup DNS MX records  at DNS server | `dig @1.1.1.1 tryhackme.com MX`
| Lookup DNS TXT records | `dig tryhackme.com TXT`

## Herramientas útiles
Herramientas que permiten recolectar información del objetivo sin conectarse directamente con el.
- **DNSDumpter:** Obtiene información del dominio y subdominios. 
- **Shodan:** Shodan.io puede ser útil para aprender varios datos sobre la red del cliente.