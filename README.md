# 💰 Expense Splitter

Una aplicación web hecha con **Python + Flask** para dividir gastos grupales (viajes, cenas, proyectos, etc.) y calcular automáticamente cuánto debe pagar o recibir cada persona.

---

## 🚀 Características

- Agregar personas al grupo  
- Registrar gastos indicando quién pagó y cuánto  
- Calcular cuánto corresponde a cada uno  
- Mostrar balances individuales y pagos sugeridos  
- Eliminar personas junto con sus gastos  
- Interfaz moderna y responsive con **Bootstrap 5**

---

## 🧱 Tecnologías utilizadas

- **Python 3**
- **Flask**
- **Flask-SQLAlchemy**
- **Pandas**
- **Bootstrap 5**
- **HTML / CSS / JS**

---

## ⚙️ Instalación y uso

1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/tuusuario/expense-splitter.git
    cd expense-splitter

2. **Crear entorno virtual**
    python -m venv venv
    source venv/bin/activate   # Linux / Mac
    venv\Scripts\activate      # Windows

3. **Instalar Dependencias**
    pip install -r requirements.txt

4. **Ejecutar la aplicación**
    pyton app.py

5. Abrir en el navegador
    http://127.0.0.1:5000

📂 Estructura del proyecto

    expense-splitter/
    │
    ├── app.py
    ├── config.py
    ├── requirements.txt
    ├── README.md
    │
    ├── models/
    │   └── database.py
    │
    ├── static/
    │   ├── style.css
    │   └── script.js
    │
    └── templates/
        ├── base.html
        ├── index.html
        └── summary.html

💡 Ejemplo de uso

1. Agrega a los participantes: Roberto, Faviola, Irene.

2. Registra un gasto:

    Descripción: Salida al cine

    Monto: 15000

    Pagado por: Roberto

3. Ve a Resumen →
    Verás algo como:
    **Faviola debe pagarle $5000.00 a Roberto**
    **Irene debe pagarle $5000.00 a Roberto**
    (o los nombres que hayas registrado)

🧹 Mejoras futuras

    Editar nombres y gastos existentes

    Crear distintos grupos de gasto

    Exportar resumen a CSV o PDF

    Autenticación de usuarios

📜 Licencia

    Este proyecto se distribuye bajo la licencia MIT.
    Puedes usarlo, modificarlo y compartirlo libremente.

👨‍💻 Desarrollado con ❤️ por NeviumDev