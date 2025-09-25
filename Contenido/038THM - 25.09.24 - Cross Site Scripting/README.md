# 🛡️ Resumen de DOM-Based XSS, eval() y Polyglots

## 📌 DOM-Based XSS
- Vulnerabilidad que ocurre **en el navegador**, no en el servidor.
- El ataque surge cuando el **JavaScript del sitio** toma datos controlados por el usuario y los inserta en el DOM sin validación.
- **Fuentes comunes de entrada**:
  - `window.location` (`hash`, `search`, `pathname`, `href`)
  - `document.URL`, `document.referrer`
  - `document.cookie` (si no es HttpOnly)
  - `localStorage` / `sessionStorage`
  - `postMessage`
- **Sinks peligrosos (métodos inseguros de salida)**:
  - `eval()`
  - `document.write()`
  - `innerHTML` / `outerHTML`
  - `Function()`
  - `setTimeout()` / `setInterval()` con strings
  - Asignaciones directas a `element.src`, `element.href`, etc.

---

## ⚠️ Función `eval()`
- Ejecuta cualquier **cadena como código JavaScript**.
- Ejemplo seguro:
  ```js
  eval("2+2"); // devuelve 4
  ```
- Ejemplo inseguro:
  ```js
  eval(window.location.hash);
  // Si la URL contiene #alert(1), se ejecuta directamente
  ```
- Riesgos:
  - XSS
  - Robo de cookies / tokens
  - Ejecución de código arbitrario
- **Regla de oro**: no usar `eval()` → reemplazar por métodos seguros (`JSON.parse()`, funciones específicas).

---

## 🧩 Polyglots en XSS
- Un **polyglot** es un payload “todo terreno” capaz de:
  - Escapar de etiquetas (`</textarea>`, `</script>`, etc.)
  - Escapar de atributos (`">`, `onerror=`, etc.)
  - Escapar de bloques JS (`';alert(1);//`)
  - Bypassear filtros con comentarios, codificación y mayúsculas/minúsculas.

### Ejemplo de polyglot:
```js
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */onerror=alert('THM') )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert('THM')//>\x3e
```

### Ventajas
- Funciona en muchos contextos: HTML, atributos, cierre de etiquetas, SVG, etc.
- Útil para pruebas rápidas y CTFs.

### Limitaciones
- No es 100% universal:
  - Puede fallar en **JS puro** (variables, objetos).
  - Puede fallar en **CSS o JSON**.
  - Filtros/WAF avanzados lo pueden bloquear.
  - Librerías de sanitización modernas (ej. DOMPurify) lo neutralizan.

---

## ✅ Conclusión
- DOM-Based XSS ocurre por **mal uso del DOM con datos del usuario**.
- `eval()` es **muy inseguro** y debe evitarse siempre.
- Un **polyglot** permite atacar múltiples contextos, pero no sustituye la necesidad de probar payloads adaptados según el escenario.