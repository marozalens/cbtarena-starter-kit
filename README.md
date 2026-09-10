# Starter kit — CaixaBank Tech × UPC, Reto de innovación 2026

Plantilla base para construir vuestro router: el código que decide, para
cada ticket de desarrollo que os llega, si lo resuelve un modelo LLM (y
cuál) o si hay que escalarlo a un desarrollador humano.

## Qué hay aquí

```
router/
  decide.py       <- AQUÍ escribís vuestro código. Solo este fichero.
  _contract.py    <- no tocar: define Task y Decision
  __main__.py     <- no tocar: habla con la Arena por stdin/stdout
practice_harness.py   <- para probar en local
practice_tasks.json   <- tareas de ejemplo para practicar
```

`router/decide.py` es lo único que enviáis. Todo lo demás es la
fontanería que hace que vuestro código hable con la Arena — si la rompéis,
vuestras tareas fallarán aunque la lógica de `decide()` esté bien.

## El contrato

`decide()` recibe una `Task` y devuelve una `Decision`:

```python
def decide(task: Task) -> Decision:
    ...
```

- `task.task_id` — identificador del ticket (p. ej. `"t007"`).
- `task.prompt` — el ticket en sí, en texto.
- `task.context` — `module`, `change_type`, `risk_area`, `estimated_size`.
- `task.constraints` — `max_cost_eur`, `max_latency_ms` para esa tarea.

```python
Decision(
    route="model",              # "model" o "human"
    target="claude-haiku-4-5",  # un id del catálogo, o "human_developer"
    reasoning="...",             # por qué (texto libre, para vuestro propio análisis)
)
```

`risk_area` no siempre es `null` — cuando aparece, alguien decidió que esa
zona del código es sensible (aislamiento del sandbox, integridad del
marcador, autenticación...). Qué hacer con eso — incluido si escaláis algo
a `human_developer` — es vuestra decisión de diseño.

## Primera versión, la más simple posible

```python
from router._contract import Task, Decision

def decide(task: Task) -> Decision:
    return Decision(
        route="model",
        target="claude-haiku-4-5",
        reasoning="de momento, todo al modelo barato",
    )
```

## Probar en local — modo práctica

Sin tocar la Arena, sin gastar ningún intento oficial:

```bash
python practice_harness.py
```

Os enseña, tarea a tarea, qué destino elegiríais y por qué.

## Enviar oficialmente

1. Conseguid vuestro equipo y token (os los da la organización — no os
   dais de alta vosotros mismos).
2. Subid vuestro trabajo a **vuestro propio** repo (este, con vuestros
   cambios) y etiquetad el commit que queréis enviar:

   ```bash
   git add .
   git commit -m "primera version que funciona"
   git tag v1
   git push origin main --tags
   ```

3. Enviad el intento oficial:

   ```bash
   curl -X POST https://cbtarena.redmushroom-ead22109.swedencentral.azurecontainerapps.io/submit \
     -H "Content-Type: application/json" \
     -d '{
       "team": "vuestro_equipo",
       "token": "el_token_que_os_dieron",
       "repo_url": "https://github.com/vuestro-equipo/vuestro-repo",
       "ref": "v1",
       "batch": "known_batch"
     }'
   ```

Hasta un número limitado de intentos oficiales (os lo dice la
organización) — se queda con el mejor. Podéis repetir el envío (con un tag
nuevo) si algo salió mal en el primero.

## Dudas, marcador, y qué puede salir mal

Todo esto está en la página de Ayuda de la propia plataforma:
<https://cbtarena.redmushroom-ead22109.swedencentral.azurecontainerapps.io/help>
