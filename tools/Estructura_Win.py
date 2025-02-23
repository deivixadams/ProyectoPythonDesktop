import os

# 📦 Definir la estructura del proyecto
project_structure = {
    "ProyectoPythonDesktop": [
        os.path.join("src", "modules"),
        os.path.join("src", "assets"),
        os.path.join("src", "ui"),
        os.path.join("src", "main.py"),  # 📌 El main.py va dentro de src/
        os.path.join("tests", "test_main.py"),
        os.path.join("docs", "README.md"),
        os.path.join("docs", "estructura.md"),
        os.path.join("tools"),  # 📌 Se agregó la carpeta tools/
        ".gitignore",
        ".env",
        "pyproject.toml",
        "LICENSE",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "estructura.md"
    ]
}

# 🚀 Función para crear la estructura en Windows
def create_structure():
    for root_folder, items in project_structure.items():
        root_folder = os.path.abspath(root_folder)  # Convierte la ruta en absoluta (Windows-friendly)
        if not os.path.exists(root_folder):
            os.makedirs(root_folder)
        for item in items:
            path = os.path.join(root_folder, item)
            if item.endswith((".py", ".md", ".toml", ".env", ".gitignore", "LICENSE", "CHANGELOG.md", "requirements.txt")):
                # 📜 Crear archivo si no existe
                folder = os.path.dirname(path)
                if folder and not os.path.exists(folder):
                    os.makedirs(folder)
                with open(path, "w", encoding="utf-8") as f:
                    f.write("")
            else:
                # 📂 Crear carpeta
                os.makedirs(path, exist_ok=True)
    
    print("✅ Estructura del proyecto creada correctamente en Windows.")

# Ejecutar función
if __name__ == "__main__":
    create_structure()
