
# Posibilidad de realizar pruebas 
Dado que se ha vuelto costoso hacer pruebas en la nube
¿Qué posibilidad hay de usar sofware como Vagrant? U
otro virtualizador e ¿incluir esto en la tesis?

# Bibliografica básica
Además de lo considerado:

[1] Kurose, J. F., & Ross, K. W. (2017). Computer networking: a top-down approach,
Pearson, 7th edition.

[2] WireGuard, WireGuard: fast, modern, secure VPN tunnel, https://www.
wireguard.com/, 2021.

[3] Linux Documentation Project, Linux Advanced Routing & Traffic Control HOW-
TO, https://tldp.org/HOWTO/Adv-Routing-HOWTO/index.html, 2021.

[4] Bautts, M., & Dawson, M. (2000). Linux Network Administrator’s Guide, O’Reilly
Media, 3rd edition.

[5] Bautts, M., & Dawson, M. (2000). Linux IP Masquerade HOWTO, https://
tldp.org/HOWTO/IP-Masquerade-HOWTO/index.html, 2021


# Cliente state-less? o crear un Deamon?
Información que el cliente deberia poder consultar:
1. Su ip publica si es que aplica
2. Su llave pública de wireguard
3. El puerto de escucha de wireguard
4. Configuración de sus peers

¿Como es posible guardar el estado del cliente?
- No guardarlo en el cliente y todo consultarlo del servidor
- Usar los registros al ejecutar wg show, pero tendriamos que serealizar.

# Duda en el diseño
Cuando un cliente quiere añadir un endpoint $e_n$. 
Debe intentar conectar directamente con $e_n$ y guardar en el orquestrador  $O$
la configuración de este, pero ¿Debera el servidor intentar establecer conexión?
Y registrar en $e_{n+1}$ la conexión a $x_n$ y $O$? 

Luego forzosamente ¿Debemos tener una conexion $e_n$ a $O$?


---
Como estaba manejando el registro de endpoints en un red privada en el servidor
era

{
    "id_red_privada":int,
    "name":String,
    ...
    "endpoints":[
        {
            "id_Endpoint":int,
            "Endpoint":{
                "id_endpoint":int,
                "wireguard_ip" = ""
                "wireguard_port" = ""
                "wireguard_private_key" = ""
                "wireguard_public_key" = ""
                "public_ip" = ""
            }
        }
    ]

}


