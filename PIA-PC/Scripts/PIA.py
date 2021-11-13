import argparse
import Cifrado_Cesar
import Crackeo_Cesar
import Descifrado_Cesar
import Email
import Metadatos
import Escaneo_Web
import Hash
import logging


def main():
    class SmartFormatter(argparse.HelpFormatter):
        def _split_lines(self, text, width):
            if text.startswith('R|'):
                return text[2:].splitlines()
            return argparse.HelpFormatter._split_lines(self, text, width)

    logging.basicConfig(format='%(asctime)s %(message)s',
                        filename='logg.txt',
                        filemode='a')
    parser = argparse.ArgumentParser(
        description=
        ' PIA CIBERSEGURIDAD :)',
        formatter_class=SmartFormatter)

    parser.add_argument(
        '-tarea',
        choices=['1', '2', '3', '4', '5', '6', '7'],
        help=
        "R|SELECCIONAR UNA TAREA \n"
        
        '(    (               (             \n '        
        ' )\ ) )\ )    (       )\ )   (     \n '
        '(()/((()/(    )\     (()/(   )\    \n '
        '/(_))/(_))((((_)(    /(_))(((_)    \n '
        '  (_)) (_))   )\ _ )\  (_))  )\___ \n '
        ' | _ \|_ _|  (_)_\(_) | _ \((/ __| \n '
        ' |  _/ | |    / _ \   |  _/ | (__  \n '
        ' |_|  |___|  /_/ \_\  |_|    \___| \n '
        '\n'                         
        '\n'                  
        ' 1. Obtencion de metadatos      \n'
        ' 2. Obtención de claves HASH    \n'

        ' 3. Escaneo de páginas Web      \n'
        ' 4. Envio de emails con adjuntos\n'
        ' *** { Tareas Cesar }  ***\n'
        ' 5. Cifrado Cesar\n'
        ' 6. Descifrado Cesar\n'
        ' 7. Crackeo Cesar\n'
    )

    
    parser.add_argument(
        '-c',
        '--config',
        help=
        'TAREA NUMERO 1 ES NECESARIO INGRESAR LA RUTA \n'
        'Ejemplo: python PIA-MENU.py -tarea 1 -c "Ruta".,'
    )

    args = parser.parse_args()

    #Tareas a realizar  
    if args.tarea == "1":
        Metadatos.printMeta(args.config)

    if args.tarea == "2":
        Hash.Obtener_Claves()

    if args.tarea == "3":
        Escaneo_Web.Scan()

    if args.tarea == "4":
        Email.Enviar_Correo()

    if args.tarea == "5":
        Cifrado_Cesar.Cifrar()

    if args.tarea == "6":
        Descifrado_Cesar.Descifrar()

    if args.tarea == "7":
        Crackeo_Cesar.Hackear()


if __name__ == "__main__":
    main()
