# Guidelines para Agentes IA (Tríada SRE / Antigravity / Claude / Codex)

Documento normativo para cualquier agente autónomo que opere repositorios dentro de la organización **SlimefunNewHorizons** o el ecosistema **Star / DrakesCraft**.

---

## 🌿 1. Política Obligatoria de Rama Única (`Single-Branch`)

1. **Unificación Inmediata**:
   * Las ramas temporales (`feat/*`, `fix/*`, `docs/*`, `release/*`, `chore/*`) deben ser integradas (**mergeadas o fast-forwarded**) a la rama canónica correspondiente tan pronto como el trabajo sea verificado.
   * Rama canónica de producción / docs: **`main`**.
   * Rama canónica de porting / Season 2 (Paper 26.x / Java 25): **`port-26x`**.
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
   * Repositorio en migración activa: **Máximo 2 ramas (`main` y `port-26x`)**.

---

## 🛡️ 2. Regla de Oro SRE: Cero Afectación a Producción

1. **Dallas (Paper 1.21.11 en Vivo)**:
   * Los JARs en producción son intocables salvo autorización expresa y prueba previa en staging.
   * Prohibido desplegar builds experimentales de `26.x` o Java 25 en Dallas.
2. **Cero Daño a Jugadores**:
   * Cero reseteo o pérdida de datos de jugadores (`BlockStorage`, inventarios, bóvedas, economías, islas).
   * Ante cualquier duda de migración de datos, siempre se utiliza respaldo preventivo y aislamiento reversible.
