# Guidelines para Agentes IA (Tríada SRE / Antigravity / Claude / Codex)

Documento normativo para cualquier agente autónomo que opere repositorios dentro de la organización **SlimefunNewHorizons** o el ecosistema **Star / DrakesCraft**.

---

## 🌿 1. Política Obligatoria de Rama Única (`Single-Branch`)

1. **Unificación Inmediata**:
   * Las ramas temporales (`feat/*`, `fix/*`, `docs/*`, `release/*`, `chore/*`) deben ser integradas (**mergeadas o fast-forwarded**) a la rama canónica correspondiente tan pronto como el trabajo sea verificado.
   * Rama canónica de producción / docs: **`main`**.
   * Rama canónica de porting / Season 2 (Paper 26.x / Java 25): **`port-26x`** (excepción de nombre: **Drakes-Suites** usa **`26.x`**, la línea activa del port).
2. **Eliminación Obligatoria de Ramas Remotas**:
   * **Queda estrictamente prohibido dejar ramas remotas abandonadas o colgadas tras un merge o verificación.**
   * Todo agente debe borrar la rama remota al fusionar:
     ```bash
     gh pr merge <numero> --merge --delete-branch
     # o directamente en git:
     git push origin --delete <nombre-de-rama>
     ```
3. **Cero Ramas Redundantes o Idénticas**:
   * Si una rama contiene commits ya absorbidos por `main` o es idéntica en contenido, debe borrarse de inmediato sin postergación.
4. **Estado Ideal de Todo Repositorio**:
   * Repositorio de producción / utilidades: **Exactamente 1 rama (`main`)**.
   * Repositorio en migración activa o con desarrollo: **Máximo 2 ramas (`main` + UNA auxiliar permanente)**.
5. **Una sola rama auxiliar (decision de Jack, 2026-10-13)**:
   * Cada repo tiene `main` y, como MAXIMO, UNA rama auxiliar permanente: la del port (`port-26x`; en **Drakes-Suites** se llama `26.x` y es la **linea activa del port 26**, StarSuites en Purpur 26.2 / Java 25) o, si no hay port, una sola de desarrollo/pruebas (`dev`). Nunca dos auxiliares.
   * Prohibido crear ramas por ticket, por agente o por IA (`fix/*`, `feat/*`, `perf/*`, `docs/*`...). Se trabaja en la rama auxiliar o en `main` con commits pequenos. Si una rama temporal es inevitable, vive como maximo 24 h: se fusiona y se borra el mismo dia.
   * Produccion (Dallas, 1.21.11) = `main`. Lo experimental de 26.x nunca va a `main`.
6. **Antes de borrar una rama descartada con commits propios, archivala**: `git bundle` en `~/ai-hub/backups/` y una linea con su idea en `ai-hub/docs/ramas-archivadas-AAAAMMDD.md`. Asi se conservan las ideas sin conservar la rama.
7. **Dependabot/Renovate**: fusionar (si compila) o cerrar el mismo dia. No dejar PRs ni ramas `dependabot/*` acumuladas.
8. **No se tocan los README para esto**: la regla vive solo en `AGENTS.md`/`CLAUDE.md`; auditoria: `python3 ~/ai-hub/scripts/auditar_ramas.py`.

---

## 🛡️ 2. Regla de Oro SRE: Cero Afectación a Producción

1. **Dallas (Paper 1.21.11 en Vivo)**:
   * Los JARs en producción son intocables salvo autorización expresa y prueba previa en staging.
   * Prohibido desplegar builds experimentales de `26.x` o Java 25 en Dallas.
2. **Cero Daño a Jugadores**:
   * Cero reseteo o pérdida de datos de jugadores (`BlockStorage`, inventarios, bóvedas, economías, islas).
   * Ante cualquier duda de migración de datos, siempre se utiliza respaldo preventivo y aislamiento reversible.

## 🌐 3. Idioma de las GUI y mensajes al jugador (decision de Jack, 2026-10-14)
Todas las GUI (titulos, nombres y lore de items, botones) y los mensajes que ven los jugadores se escriben en **ingles**, en
todos los plugins y addons nuevos y al tocar los existentes. El codigo, los comentarios internos y la documentacion pueden
seguir en espanol. Los nombres de comandos no se renombran para no romper a los jugadores.

---

## 🤖 4. Estándares de Ingeniería para Contribuciones por IA / Agentes Externos (Anti-Slop & Anti-Alucinaciones)

Este estándar aplica tanto a desarrolladores que usen asistentes de IA (Cursor, Claude, Copilot, ChatGPT) como a agentes autónomos externos que abran Pull Requests o Issues:

1. **Responsabilidad Humana Absoluta (100% Ownership)**:
   * Toda persona o bot que envíe un Pull Request asume total responsabilidad del código. Decir *"la IA lo generó"* no exime de errores, vulnerabilidades ni fallas de compilación.
2. **Divulgación Transparente de Asistencia de IA**:
   * Todo PR generado con asistencia de modelos de IA debe declararlo en la descripción del PR (`AI Disclosure`), listando las herramientas y confirmando verificación local manual.
3. **Cero Tolerancia a Alucinaciones y Slop (Cierre Inmediato)**:
   * **Se cerrará de inmediato como spam cualquier PR que contenga**:
     - Métodos o APIs inexistentes o inventadas de Spigot, Paper, Purpur, Slimefun, Java o Rust.
     - Scaffolding o boilerplate vacío ("plumbing without water").
     - Reescrituras arbitrarias de código funcional sin justificación de rendimiento o bug medible.
     - Fallos de compilación en Maven o Cargo.
4. **Evidencia Obligatoria de Verificación**:
   * El autor debe adjuntar logs de compilación exitosa (`mvn clean package -DskipTests=false`) y verificación en un entorno de pruebas.
5. **Cumplimiento del Código de Conducta**:
   * Respuestas automatizadas circulares, comentarios spam o actitudes exigentes resultarán en bloqueo inmediato del usuario/agente en toda la organización SlimefunNewHorizons conforme a [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

