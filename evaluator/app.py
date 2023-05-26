import src.common.parameters as args
from src.internal.init import SetUpValidator
from src.internal.loader import DataLoader


class App:
    if __name__ == "__main__":
    
       #try:
            # get parameters
        parameters = args.get_args().parse_args()
        if parameters.command == "init":
            SetUpValidator(parameters).run()
        else:
            # leer configuracion
            # cargar logo
            # iniciar ejecución programa
            # definir  seión de base de datos
            
            loader = DataLoader(parameters)
            loader.start()
            if parameters.command == "teachers":
                # generar procesos para listar datos
                # insertar
                # inactivar
                
                print(parameters)
        #
            # classes instance
            #show = Show(parameters)
            #template = Template(parameters, show)
            #template.run()
        #except Exception as ex:
        #    print("some problems were detected : \n")
        #    print(str(ex))
        #    exit(1)