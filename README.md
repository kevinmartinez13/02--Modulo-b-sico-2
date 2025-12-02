# modulo2

Proyecto de ejemplo con varios submódulos (1,2,3).

## Contenido

- `1/`, `2/`, `3/` — carpetas con scripts y paquetes.

## Cómo subir este proyecto a GitHub

1. Inicializar repo git localmente:

```powershell
cd C:\Users\orakp\Desktop\modulo2
git init
```

2. (Opcional) Crear `.gitignore` y `README.md` — ya vienen incluidos en este repo.

3. Añadir y confirmar los cambios:

```powershell
git add .
git commit -m "Initial commit"
```

4. Crear el repositorio en GitHub (a) usando la web o (b) la CLI `gh`.

- Web: crear un nuevo repositorio (sin README si ya lo tienes) y copiar la URL remota.
- `gh` (si instalado):

```powershell
gh repo create nombre-de-usuario/nombre-repo --public --source=. --remote=origin
```

5. Subir la rama (main):

```powershell
git branch -M main
git remote add origin https://github.com/usuario/nombre-repo.git
git push -u origin main
```

6. (Opcional) Configurar SSH:

- Generar par: `ssh-keygen -t ed25519 -C "tu-email@example.com"`.
- Añadir la llave pública en GitHub Settings → SSH and GPG keys.
- Usar: `git remote set-url origin git@github.com:usuario/nombre-repo.git`.

Listo — después de esto tu proyecto `modulo2` estará en GitHub.

Si quieres, puedo ejecutar los comandos por ti o ayudarte a crear el repo remoto también.