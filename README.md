# ⚡ CircuitSense AI

### Advanced Electronics Diagnostics, Circuit Analysis & Signal Intelligence

CircuitSense AI is an engineering toolkit built with **Python and Streamlit** to help students, electronics enthusiasts, and engineers analyze circuits, inspect signals, perform engineering calculations, and identify abnormal circuit behavior from measurements.

🌐 **Live Demo:**  
https://circuitsense-ai.streamlit.app/

---

## 🚀 Features

### 🔬 Circuit Diagnosis
Compare expected and measured circuit values to identify abnormal behavior.

- Supply voltage analysis
- Resistance-based calculations
- Expected vs measured current
- Expected vs measured output voltage
- Circuit health scoring
- Error percentage analysis
- Fault detection

### 📈 Signal Analyzer

Analyze signal data from CSV files.

- Waveform visualization
- RMS calculation
- Peak detection
- Frequency analysis
- Signal statistics
- Noise inspection
- FFT-based frequency analysis

### 🧪 Engineering Lab

A collection of electronics and electrical engineering calculations.

Includes tools for:

- Ohm's Law
- Voltage Divider
- Power calculations
- KCL Node Check
- KVL Loop Check
- Capacitive Reactance
- Inductive Reactance
- RC Time Constant
- AC/DC calculations
- Semiconductor calculations
- And more engineering utilities

### 🧠 Diagnostic Engine

Convert circuit measurements into practical diagnostic information.

The system evaluates measurement differences and provides:

- Circuit health estimation
- Error analysis
- Possible abnormal conditions
- Recommended checks

---

## 🖥️ Interface

CircuitSense AI provides a clean engineering workspace with four main areas:

```text
Dashboard
   │
   ├── Circuit Diagnosis
   │
   ├── Signal Analyzer
   │
   └── Engineering Lab

   | Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Core programming               |
| Streamlit  | Web application                |
| NumPy      | Numerical computation          |
| SciPy      | Scientific & signal processing |
| Pandas     | Data processing                |
| Plotly     | Interactive visualization      |
CircuitSense-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── core/
│   ├── engine.py
│   ├── fault_detection.py
│   ├── lab_calculations.py
│   └── signal_analysis.py
│
├── data/
│   └── sample_signal.csv
│
└── ui/
    └── dashboard.py
