# bot-servicios-471
  bot que informa sobre instituciones gubernamentales en mexico encargadas de servicios 

# Desarrollo

`virtualenv` es recomendado.

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecuta el bot:
```bash
python bot.py [opciones]
```

### Opciones:

#### -d  Dry run
No _retuitea_, sólo envía los tweets encontrados al log.

### Configuración

#### Variables de entorno necesarias:
Consíguelas [acá](https://apps.twitter.com/)

* `CONSUMER_KEY`
* `CONSUMER_SECRET`
* `ACCESS_TOKEN`
* `ACCESS_TOKEN_SECRET`

Puedes o exportarlas o usarlas en cada ejecución.

#### Cuentas a retweetear

En `config.yml` hay un array con la lista de cuentas.

La API de Twitter necesita el `id` – *no el screen name*. Es importante que el `id` sea un `string`.

Consigue el `id` [acá](http://gettwitterid.com/)

## Trae tu bot!
Como la aplicación busca los tokens para comunicarse con la API de Twitter en variables de entorno, puedes usar cualquier cuenta.
