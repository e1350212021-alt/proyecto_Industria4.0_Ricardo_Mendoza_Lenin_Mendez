# proyecto_Industria4.0_Ricardo_Mendoza_Lenin_Mendez
proyecto_rul_motores_Machine_Learning

- Predicción de Vida Útil Remanente (RUL) de Motores Eléctricos Industriales
- Descripción del Proyecto

Este proyecto implementa un sistema de Mantenimiento Predictivo basado en Machine Learning, cuyo objetivo es estimar la Vida Útil Remanente (RUL) de motores eléctricos industriales.

Se utiliza un modelo de regresión basado en Random Forest, el cual analiza variables operativas como horas de funcionamiento, temperatura y vibración para predecir el estado del equipo en tiempo real.

-Tecnologías Utilizadas
Python 3
Jupyter Notebook
Pandas
NumPy
Scikit-learn (Random Forest)
Joblib
Streamlit
-Variables del Modelo
Horas de operación (0 - 10000)
Temperatura (40°C - 100°C)
Vibración (1 - 10 mm/s)
⚙️ Modelo de Machine Learning

Se utilizó un modelo de Random Forest Regressor, entrenado con un dataset sintético generado mediante Python.

El modelo permite predecir la Vida Útil Remanente (RUL) en horas y clasificar el estado del motor en:

🟢 Bueno
🟡 Medio
🔴 Crítico

- Estructura del Proyecto
proyecto_final_industria4.0/
│
├── app.py                # Dashboard Streamlit
├── modelo_rul.pkl       # Modelo entrenado
├── dataset.xlsx         # Datos simulados
├── ProyectoIndustria4.0.ipynb       # Entrenamiento del modelo
└── README.md            # Documentación

- Instrucciones de Despliegue
🚀 Instrucciones de Despliegue
1. Descargar el proyecto
git clone https://github.com/e1350212021-alt/proyecto_Industria4.0_Ricardo_Mendoza_Lenin_Mendez.git
2. Acceder al repositorio
cd proyecto_Industria4.0_Ricardo_Mendoza_Lenin_Mendez
3. Acceder a la carpeta del proyecto
cd proyecto_final_industria4.0
4. Instalar las dependencias
pip install streamlit pandas numpy scikit-learn joblib
5. Ejecutar el dashboard
streamlit run app.py  



--Ejecución del Dashboard

Una vez ejecutado el comando anterior, Streamlit abrirá automáticamente una interfaz web en:

http://localhost:8501

En esta interfaz el usuario podrá ingresar valores de operación del motor y obtener la predicción de su vida útil remanente.



👨‍💻 Autor

Ricardo Mendoza-Lenin Mendez
