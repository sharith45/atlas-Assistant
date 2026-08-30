<div align="center">

# atlas-Assistant

**Tu asistente personal. En tu ordenador. Sin depender de la nube de nadie.**

Habla contigo por voz, atiende tu WhatsApp — mensajes **y llamadas de teléfono** —,
controla tu ordenador, programa lo que necesites y recuerda lo que importa.

[![Versión](https://img.shields.io/badge/versión-1.0.0-8b5cf6)](../../releases/latest)
[![Windows](https://img.shields.io/badge/Windows-10%2B%20(64--bit)-0078d4)](../../releases/latest)
[![Descargar](https://img.shields.io/badge/descargar-Atlas.exe-22c55e)](../../releases/latest)

[Descargar](../../releases/latest) · [Instalación](#instalación) · [Qué sabe hacer](#qué-sabe-hacer) · [Cómo funciona](#cómo-funciona-por-dentro)

</div>

<!-- IMAGEN: captura o vídeo corto de la ventana principal con el orbe hablando
     Sube el fichero a `docs/img/atlas-hero.png` y quita este comentario
     (las dos lineas de <!-- y -->) para que se vea. -->
<!--
<p align="center">
  <img src="docs/img/atlas-hero.png" alt="ATLAS en funcionamiento" width="820">
</p>
-->

---

## Por qué ATLAS

Casi todos los asistentes son una caja de texto en una web. Tú escribes, ellos contestan, y ahí se acaba.

ATLAS no. **Vive en tu ordenador**, tiene tus archivos delante, tu WhatsApp conectado y memoria de lo que habéis hablado. Le hablas y te responde con voz. Le pides algo y lo hace — no te explica cómo hacerlo.

Y cuando no estás en casa, sigue trabajando: **le escribes por WhatsApp desde el móvil y te devuelve el trabajo hecho.**

---

## Lo que la hace distinta

### Contesta el teléfono

No es un bot que escribe mensajes. Cuando alguien te llama por WhatsApp, ATLAS **descuelga y conversa** en voz alta, en tiempo real. Toma el recado, te lo pasa al momento, y si hace falta te pregunta a ti en mitad de la llamada sin que el otro se entere.

<!-- IMAGEN: vídeo de una llamada entrante y Atlas contestando
     Sube el fichero a `docs/img/llamada.gif` y quita este comentario
     (las dos lineas de <!-- y -->) para que se vea. -->
<!--
<p align="center">
  <img src="docs/img/llamada.gif" alt="Atlas atendiendo una llamada de WhatsApp" width="720">
</p>
-->

### La manejas desde el móvil

Estás fuera y necesitas un informe, un archivo o que revise algo en tu ordenador. Le escribes por WhatsApp como a cualquier persona, y ATLAS lo hace en tu PC y te devuelve el resultado. Sin escritorio remoto, sin sentarte delante.

### Un modelo para cada tarea, no uno caro para todo

ATLAS reparte el trabajo entre varios modelos según lo que cueste cada cosa. El modelo caro y potente solo entra cuando toca programar o manejar el sistema; charlar, buscar o contestar un WhatsApp va con uno rápido y barato.

| Rol | Para qué |
|---|---|
| `conversational` | Hablar contigo |
| `os_agent` | Programar y manejar tu ordenador |
| `navigate` | Moverse por la web |
| `fast_search` | Buscar en internet |
| `memory_cortex` | Decidir qué recordar |
| `whatsapp_contacts` | Chats y llamadas |

Cada uno se cambia desde Ajustes, sin tocar código. **No pagas modelo de programador para decir "buenos días".**

<!-- IMAGEN: captura de Ajustes, seccion Agentes y Proveedores
     Sube el fichero a `docs/img/ajustes-agentes.png` y quita este comentario
     (las dos lineas de <!-- y -->) para que se vea. -->
<!--
<p align="center">
  <img src="docs/img/ajustes-agentes.png" alt="Un modelo distinto para cada rol" width="820">
</p>
-->

### Recuerda de verdad

Dos memorias, como una persona:

- **Corto plazo** — el hilo de la conversación de ahora.
- **Largo plazo** — una bóveda que crece sola. Lo que aprende contigo se consolida en notas enlazadas, y un córtex decide en cada turno qué merece recordar. No relee todo: trae solo lo que hace falta.

Todo en tu disco. Nada sube a ningún servidor.

<!-- IMAGEN: captura de la pestaña Memoria con el grafo
     Sube el fichero a `docs/img/memoria.png` y quita este comentario
     (las dos lineas de <!-- y -->) para que se vea. -->
<!--
<p align="center">
  <img src="docs/img/memoria.png" alt="La memoria de Atlas" width="820">
</p>
-->

---

## Qué sabe hacer

### Voz en tiempo real

Le hablas y te contesta hablando, sin tocar el teclado. Detecta cuándo empiezas y cuándo terminas de hablar, y puedes interrumpirla a media frase.

Su voz es tuya: **eliges cuál** entre decenas en español, y ajustas velocidad y tono. También cuánto silencio espera antes de dar tu turno por terminado.

<!-- IMAGEN: captura de Ajustes, seccion La voz de Atlas
     Sube el fichero a `docs/img/voz.png` y quita este comentario
     (las dos lineas de <!-- y -->) para que se vea. -->
<!--
<p align="center">
  <img src="docs/img/voz.png" alt="Ajustes de voz" width="820">
</p>
-->

### WhatsApp completo

- Lee y contesta tus chats, con el carácter que tú le pongas
- **Atiende las llamadas** y conversa por teléfono
- Te avisa cuando alguien te busca de verdad, y se calla cuando no hace falta
- Sabe cuándo apartarse: si estás tú escribiendo en ese chat, no se mete
- Devuelve las llamadas perdidas

<!-- IMAGEN: captura de la pestaña WhatsApp con chats y estado
     Sube el fichero a `docs/img/whatsapp.png` y quita este comentario
     (las dos lineas de <!-- y -->) para que se vea. -->
<!--
<p align="center">
  <img src="docs/img/whatsapp.png" alt="El módulo de WhatsApp" width="820">
</p>
-->

### Maneja tu ordenador

Crea y edita archivos, ejecuta comandos, instala cosas, programa lo que le pidas. Le dices qué quieres conseguir; ella decide los pasos y los va dando, corrigiéndose si algo falla.

<!-- IMAGEN: captura de la terminal / una tarea ejecutándose
     Sube el fichero a `docs/img/terminal.png` y quita este comentario
     (las dos lineas de <!-- y -->) para que se vea. -->
<!--
<p align="center">
  <img src="docs/img/terminal.png" alt="Atlas trabajando en el ordenador" width="820">
</p>
-->

### Navega la web

Abre un navegador de verdad, busca, entra en las páginas y saca lo que necesitas. No se inventa datos: los va a buscar.

### Documentos

Lee y crea Word, Excel, PowerPoint y PDF. Arrastra un archivo a la ventana y lo entiende — también fotos y documentos escaneados.

### Habilidades ampliables

ATLAS aprende cosas nuevas sin recompilar nada. Las **skills** son instrucciones especializadas que se instalan y quedan disponibles al instante. Le dices que instale una y ella la descarga, la ordena y la registra sola.

<!-- IMAGEN: captura de la pestaña Skills
     Sube el fichero a `docs/img/skills.png` y quita este comentario
     (las dos lineas de <!-- y -->) para que se vea. -->
<!--
<p align="center">
  <img src="docs/img/skills.png" alt="Habilidades instaladas" width="820">
</p>
-->

---

## Instalación

**No necesitas Python ni instalar dependencias.** Es un programa, se descomprime y se abre.

1. Descarga **`Atlas-v1.0.0-windows.zip`** desde [releases](../../releases/latest) y descomprímelo donde quieras.
2. Abre el archivo **`.env`** con el Bloc de notas y pon tus claves.
3. Ejecuta **`Atlas.exe`**.

### Claves

ATLAS usa modelos de IA que van por internet, así que necesitas claves propias. Las básicas son gratuitas:

- `GOOGLE_API_KEY` — inteligencia, voz y visión — https://aistudio.google.com/apikey
- `DEEPSEEK_API_KEY` — el agente que trabaja en tu ordenador — https://platform.deepseek.com
- `BRAVE_API_KEY` — búsqueda web, opcional — https://brave.com/search/api

Pon también tu `USER_NAME` para que sepa cómo llamarte.

**Las claves son tuyas.** ATLAS no incluye ninguna ni las comparte.

### Al abrirlo, Windows te avisará

Verás **"Windows protegió tu PC"**. Es porque el programa no lleva un certificado de firma comprado, no porque tenga nada malo. Pulsa *Más información → Ejecutar de todas formas*.

Tu antivirus puede quejarse por lo mismo. Si te lo bloquea, añade la carpeta a las excepciones.

### Requisitos

Windows 10 o superior (64 bits) · ~3 GB de disco · conexión a internet · micrófono para hablarle

---

## Cómo funciona por dentro

ATLAS no es un programa, son varios trabajando juntos:

```
Interfaz de escritorio        PyQt6, con la ventana dibujada en HTML/JS
Bucle conversacional          reparte cada turno entre los agentes
Agente de sistema             ejecuta, programa y corrige
Navegador                     Playwright, con su propio buscador
Módulo de WhatsApp            servidor en Go (whatsmeow) + agente propio
Voz                           síntesis en streaming y escucha con detector de voz
Memoria                       bóveda de notas enlazadas + córtex de recuperación
```

Todo corre en tu máquina. Lo único que sale de tu ordenador son las peticiones a los modelos de IA, con tus propias claves.

---

## Privacidad

Tus conversaciones, tus contactos, tu memoria y tu sesión de WhatsApp **se quedan en tu disco**, en la carpeta del programa. No hay servidor intermedio, no hay cuenta que crear, no hay telemetría.

---

## Estado del proyecto

ATLAS 1.0.0 es la primera versión pública. Funciona y se usa a diario, pero es joven: habrá cosas que fallen.

Si encuentras un error, abre un [issue](../../issues) contando qué hacías, qué esperabas y qué pasó. Si sale un mensaje de error, pégalo.

---

## Quién la hizo

**Sharith Javier Manjarrez Pacheco** — Ingeniero de Sistemas, Colombia.

Especializado en Inteligencia Artificial (machine learning y sistemas de agentes autónomos) y desarrollo backend.

[github.com/sharith45](https://github.com/sharith45)

---

<div align="center">

**ATLAS** — Tu asistente. Tu ordenador. Tu información.

</div>
