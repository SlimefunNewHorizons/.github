# Guia de Uso e Instalacion de Modificadores DLSS (DLSS 5 / Frame Generation / Upscaler Mods)

> **ADVERTENCIA DE SEGURIDAD CRITICA - ANTI-CHEAT Y PROHIBICION EN LINEA**
> 
> **BAJO NINGUNA CIRCUNSTANCIA UTILIZAR MODS DE DLSS/FSR EN JUEGOS MULTIJUGADOR EN LINEA.**
> 
> Los paquetes no oficiales denominados informalmente como 'DLSS 5 / DLSS Next / OptiScaler / DLSS-G to FSR3 / Frame Gen Enablers' funcionan mediante reemplazo de bibliotecas del sistema (dxgi.dll, d3d12.dll) o inyeccion directa en memoria del proceso (nvngx_dlss.dll).
> 
> Sistemas anti-cheat a nivel de kernel y de usuario (como Easy Anti-Cheat, BattlEye, Riot Vanguard, Ricochet, Valve Anti-Cheat (VAC), Ubisoft BE, PunkBuster, Denuvo Anti-Cheat) detectan de forma automatizada estas librerias inyectadas como software malicioso o herramientas de trampas (memory tampering / unauthorized DLL injection).
> **El resultado es un baneo permanente e irreversible de la cuenta o del hardware (HWID ban).**

---

## 1. Politica Estricta de Uso
- **PERMITIDO Y SEGURO**: Exclusivamente en juegos **Single Player (Un Jugador) / Modo Desconectado (Offline)** instalados localmente.
  - Ejemplos seguros: *Cyberpunk 2077, The Witcher 3: Wild Hunt, Hogwarts Legacy, Black Myth: Wukong, The Elder Scrolls V: Skyrim, Fallout 4, God of War, Horizon Zero Dawn, Starfield, Red Dead Redemption 2 (solo Modo Historia sin conexion a Red Dead Online)*.
- **ESTRICTAMENTE PROHIBIDO**: Cualquier juego con conexion multijugador o anti-cheat.
  - Ejemplos prohibidos: *Call of Duty / Warzone, Apex Legends, Fortnite, Valorant, Rainbow Six Siege, Counter-Strike 2, Rust, GTA Online, Destiny 2, The Finals, Helldivers 2, EA Sports FC*.

---

## 2. Como Funciona el Ecosistema de Upscaling Moderno
1. **DLLs Oficiales de NVIDIA DLSS (v3.8.x+)**:
   - Se descargan oficialmente o desde TechPowerUp DLSS Database.
   - Mejoran nitidez, estabilidad temporal y reducen ghosting.
   - Son reemplazos directos de nvngx_dlss.dll en la carpeta binaria del juego.
2. **OptiScaler / DLSS Enablers (GitHub)**:
   - Proyectos open source que traducen llamadas de DLSS 2/3 a FSR 3.1 / XeSS o permiten generacion de fotogramas (Frame Generation) en tarjetas de generaciones anteriores.
   - Usan un wrapper dxgi.dll que intercepta la cadena de intercambio DirectX.

---

## 3. Protocolo de Instalacion para Juegos Locales
1. **Crear Backup previo**:
   - En la carpeta de ejecutables del juego (ej. .../bin/x64/), respalda cualquier archivo .dll original antes de sobreescribir.
2. **Colocacion de Archivos**:
   - Colocar nvngx_dlss.dll (version verificada) o los wrappers correspondientes.
3. **Verificacion de Parametros**:
   - Iniciar el juego, abrir el menu de video/graficos, y confirmar que las opciones de Super Resolution o Generacion de Fotogramas se activan de forma estable.
4. **Desinstalacion Rapida**:
   - Si el juego presenta artefactos visuales o crashes, simplemente eliminar el dxgi.dll o restaurar la .dll original.
