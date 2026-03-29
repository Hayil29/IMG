import os

folder_images = 'img'  
output_file = 'index.html'
extensiones_validas = ('.jpg', '.jpeg', '.png', '.webp', '.gif')

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galería de Descargas</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #121212; color: white; padding: 40px; }
        h1 { text-align: center; margin-bottom: 40px; }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 20px;
            max-width: 1300px;
            margin: 0 auto;
        }
        .card {
            background: #1e1e1e;
            padding: 10px;
            border-radius: 12px;
            transition: transform 0.2s;
            text-align: center;
            border: 1px solid #333;
        }
        .card:hover { transform: translateY(-5px); border-color: #007bff; }
        .card img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 8px;
        }
        .btn-download {
            display: block;
            margin-top: 12px;
            padding: 10px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: bold;
        }
        .btn-download:hover { background: #0056b3; }
    </style>
</head>
<body>
    <h1>Mis Imágenes ({count})</h1>
    <div class="gallery">
"""

count = 0
for filename in sorted(os.listdir(folder_images)):
    if filename.lower().endswith(extensiones_validas):
        path = f"{folder_images}/{filename}"
        html_content += f"""
        <div class="card">
            <img src="{path}" alt="{filename}">
            <a href="{path}" download="{filename}" class="btn-download">Descargar</a>
        </div>"""
        count += 1

html_content += """
    </div>
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content.replace("{count}", str(count)))

print(f"✅ ¡Listo! Se generó '{output_file}' con {count} imágenes.")