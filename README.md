# primera subida de archivos

## 1. Crea y edita tu README
echo "# MotorFree" >> README.md

## 2. Inicializa el repositorio Git
git init

## 3. Añade el README al área de staging
git add README.md

## 4. Haz tu primer commit
git commit -m "first commit"

## 5. Cambia el nombre de la rama principal a 'main'
git branch -M main

## 6. Conecta con tu repositorio remoto en GitHub
git remote add origin https://github.com/asmundknute/MotorFree.git

## 7. Sube tu rama 'main' al remoto
git push -u origin main

# respaldo diario

## 1. Añade (o actualiza) la URL del remoto
git remote add origin https://github.com/asmundknute/MotorFree.git

## 2. Asegúrate de que tu rama principal se llame 'main'
git branch -M main

## 3. Empuja tus cambios al servidor remoto
git push -u origin main
