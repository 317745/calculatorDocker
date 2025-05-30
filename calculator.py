from simpleeval import simple_eval
def evaluar(argumentos):
    try: 
        return {'ok': True, 
        'result': simple_eval(argumentos)
        }
    except Exception as e:
        return {'ok': False, 
        'error': e
        }