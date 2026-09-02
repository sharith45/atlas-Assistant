# ATLAS Wiki System Rules

Este archivo contiene la especificación de comportamiento y reglas de formato para que ATLAS mantenga de forma autónoma y autodidacta esta Bóveda de Conocimiento (Wiki).

## Estructura de Carpetas

- `raw/`: Contiene archivos de texto, documentación cruda o código inyectado por el usuario o por ATLAS. Son de solo lectura (inmutables).
- `wiki/`: Contiene las notas compiladas de forma limpia por ATLAS.
- `index.md`: Punto de entrada raíz. Contiene la lista temática de conceptos con enlaces a las notas en `wiki/`.

## Reglas de Edición para ATLAS (Mantenimiento del Wiki)

1. **Nombres de Archivos:** Las notas dentro de `wiki/` deben nombrarse usando minúsculas y guiones bajos (ej: `servidores_web_python.md`, `stack_tecnologico.md`). No usar espacios ni caracteres especiales.
2. **Enlaces Cruzados (Wiki-links):** Toda nota creada o editada debe vincularse de forma bidireccional usando el formato de doble corchete de Obsidian:
   - Ejemplo: `[[wiki/servidores_web_python|Servidores Web en Python]]` o simplemente `[[wiki/stack_tecnologico]]`.
   - Se debe enlazar a conceptos relacionados en la bóveda para formar un grafo interconectado de conocimiento.
3. **Consolidación vs Duplicidad:** Si un nuevo tema en `raw/` expande un concepto que ya existe en `wiki/`, se debe **editar y expandir la nota existente** en lugar de crear una nota nueva.
4. **Formato de Notas en `wiki/`:**
   - Cada nota debe tener un título principal `# Título`.
   - Debe iniciar con metadatos de frontmatter (tags, fecha de última edición, etc.).
   - Debe finalizar con una sección de **Enlaces Relacionados** que apunte a otras notas vinculadas del Wiki.
5. **Actualización de Índices (Preservación Absoluta):**
   - Cada vez que se cree o modifique una nota en `wiki/`, se debe añadir o actualizar su enlace correspondiente en `index.md` bajo la categoría correcta.
   - **PRESERVACIÓN EXIGIDA:** Al modificar `index.md`, es obligatorio preservar íntegramente todas las categorías y todos los enlaces preexistentes. Está terminantemente prohibido truncar, recortar o dejar incompleto el índice, ya que esto borraría las conexiones en la memoria de ATLAS.
6. **Unificación de Sesiones de Chat (Evitar Duplicados):**
   - Todas las conversaciones o resúmenes de sesión de un mismo día se deben consolidar y añadir a una única nota llamada `wiki/chat_session_YYYY_MM_DD.md` (por ejemplo, `wiki/chat_session_2026_07_20.md`).
   - Está estrictamente prohibido crear archivos separados con horas o números al final (como `chat_session_YYYY_MM_DD_HHMMSS.md`). Si ya existe la nota de chat para ese día, se debe actualizar agregando la nueva sesión al final de la misma.
   - **Formato Estricto de Turnos:** Cada turno de conversación dentro de la nota debe seguir estrictamente esta estructura:
     ### Turno N
     **USER**: [Mensaje del usuario]
     **ATLAS**: [Respuesta de ATLAS]
   - Está estrictamente prohibido usar iconos (como 👤, 🤖, 💬) o encabezados alternativos (como `--- 💬 [CHAT: TURNO 1] ---`). Todo el contenido se debe unificar y limpiar en base a este formato estándar de negritas y cabeceras `### Turno N`.

7. **Las personas de la vida del usuario tienen su propia nota:**
   - Cuando en una conversación aparezca alguien que importa —familia, pareja, amistades, socios, compañeros de trabajo, un médico, quien sea—, además de la nota del día se debe crear o **actualizar** una nota propia de esa persona: `wiki/persona_<nombre>.md`.
   - Esta regla **no es una excepción a la regla 6**: la conversación completa sigue yendo a la nota diaria. Lo que se guarda aquí es lo que hay que recordar de esa persona, extraído de lo que se habló.
   - **Por qué existe esta regla:** sin ella todo lo personal acaba enterrado dentro de un `chat_session_2026_08_13.md` entre encargos técnicos, y no hay forma de recuperarlo cuando hace falta. Una semana después nadie encuentra que a la hermana la operaban el martes.
   - Qué va en la nota: quién es respecto al usuario, lo que se ha ido contando de ella, y lo que quedó pendiente de saber. Cada entrada con su fecha, para que se note qué es reciente y qué es de hace meses.
   - Las notas de persona se enlazan con la nota del día en que salió el tema y entre ellas cuando la relación exista (`[[wiki/persona_ana]]` y `[[wiki/persona_luis]]` si son hermanos).
   - **Solo lo que el usuario contó**, tal y como lo contó. Nada de deducir, interpretar ni diagnosticar a nadie, ni al usuario ni a terceros. Si alguien se mencionó de pasada y no se dijo nada de él, no hay nota que crear.


