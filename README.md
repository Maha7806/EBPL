
# 🏢 Smart Building Health Dashboard with Simulated Sensors

This project is a **real-time structural health monitoring dashboard** for buildings, using **simulated sensor data**. It helps visualize and track key metrics like vibration, temperature, strain, and humidity — all without requiring physical sensors.

Built using **Python** and **Streamlit**, this project is perfect for students, educators, and SHM enthusiasts who want to learn or demonstrate structural health monitoring concepts in an interactive way.

---

## 🚀 Features

- Real-time simulation of structural sensors
- Dashboard-style metric display
- Live graphs for data trends
- Alerts for abnormal readings
- Easy to run — no hardware required

---

## 📦 Technologies Used

- **Python 3**
- **Streamlit** – For UI and real-time updates
- **Plotly** – For interactive charts
- **NumPy / Pandas** – For data simulation and storage

---

## 🔧 Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/smart-building-dashboard.git
   cd smart-building-dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**:
   ```bash
   streamlit run app.py
   ```

---

## 📊 Sensor Metrics Simulated

| Sensor Type   | Unit       | Normal Range       |
|---------------|------------|--------------------|
| Vibration     | mm/s       | 2.0 – 6.0          |
| Temperature   | °C         | 20 – 30            |
| Strain        | microstrain| 4.0 – 6.0          |
| Humidity      | %          | 40 – 60            |

Alerts are triggered if values exceed safe thresholds.

---

## 📚 Use Cases

- Educational tool for teaching Structural Health Monitoring (SHM)
- Prototype dashboard for smart buildings
- Base project for integrating real IoT sensors

---

## 📌 Future Enhancements

- Add CSV export or database storage
- Integrate with real sensor devices (e.g., via MQTT or IoT APIs)
- User login and role-based access
- Email/SMS alert system

---

## 🧑‍💻 Author

Maha lekshmi M 
Feel free to reach out or fork the project!

---

## 📝 License

This project is open-source and free to use under the MIT License.

