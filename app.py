
import streamlit as st
import pandas as pd
from core.engine import analyze_circuit
from core.fault_detection import detect_faults
from core.signal_analysis import analyze_signal
from core.lab_calculations import calculate

st.set_page_config(
    page_title="CircuitSense AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Modern UI ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0b1120;
}

[data-testid="stHeader"] {
    background: rgba(11,17,32,0.85);
}

.block-container {
    max-width: 1400px;
    padding: 2rem 2.5rem 3rem;
}

section[data-testid="stSidebar"] {
    background: #0f172a;
    border-right: 1px solid #1e293b;
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

.brand {
    padding: 4px 4px 22px;
    border-bottom: 1px solid #1e293b;
    margin-bottom: 22px;
}

.brand-title {
    font-size: 23px;
    font-weight: 700;
    color: #f8fafc;
}

.brand-title span {
    color: #38bdf8;
}

.brand-sub {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 4px;
}

.hero {
    background: linear-gradient(135deg, #111c35 0%, #0f172a 55%, #10253a 100%);
    border: 1px solid #1e3a5f;
    border-radius: 18px;
    padding: 28px 30px;
    margin-bottom: 24px;
}

.hero h1 {
    margin: 0;
    color: #f8fafc;
    font-size: 34px;
    letter-spacing: -1px;
}

.hero p {
    color: #94a3b8;
    margin: 8px 0 0;
    font-size: 15px;
}

.status {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: #0b2a25;
    color: #5eead4;
    border: 1px solid #134e4a;
    border-radius: 999px;
    padding: 6px 11px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 14px;
}

.dot {
    width: 7px;
    height: 7px;
    background: #2dd4bf;
    border-radius: 50%;
}

.card {
    background: #111827;
    border: 1px solid #1e293b;
    border-radius: 15px;
    padding: 18px;
    min-height: 118px;
}

.card-label {
    color: #94a3b8;
    font-size: 12px;
    font-weight: 500;
}

.card-value {
    color: #f8fafc;
    font-size: 27px;
    font-weight: 700;
    margin-top: 9px;
}

.card-note {
    color: #64748b;
    font-size: 11px;
    margin-top: 5px;
}

.section-title {
    color: #f8fafc;
    font-size: 20px;
    font-weight: 650;
    margin: 28px 0 12px;
}

.module {
    background: #111827;
    border: 1px solid #1e293b;
    border-radius: 15px;
    padding: 20px;
    min-height: 145px;
}

.module h3 {
    color: #f8fafc;
    font-size: 16px;
    margin: 0 0 7px;
}

.module p {
    color: #94a3b8;
    font-size: 13px;
    line-height: 1.55;
}

div[data-testid="stMetric"] {
    background: #111827;
    border: 1px solid #1e293b;
    border-radius: 15px;
    padding: 15px;
}

div[data-testid="stMetricLabel"] {
    color: #94a3b8;
}

div[data-testid="stMetricValue"] {
    color: #f8fafc;
}

.stButton > button {
    border-radius: 10px;
    font-weight: 600;
    min-height: 42px;
}

div[data-baseweb="select"] > div {
    background: #111827;
    border-color: #334155;
}

.stTextInput input, .stNumberInput input {
    background: #0f172a;
    color: #f8fafc;
    border-color: #334155;
}

.stAlert {
    border-radius: 12px;
}

[data-testid="stFileUploader"] {
    background: #111827;
    border: 1px dashed #334155;
    border-radius: 14px;
    padding: 8px;
}

hr {
    border-color: #1e293b;
}

.small-muted {
    color: #64748b;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)


# ---------- Sidebar ----------
st.sidebar.markdown("""
<div class="brand">
    <div class="brand-title">⚡ Circuit<span>Sense</span> AI</div>
    <div class="brand-sub">Electronics Intelligence Platform</div>
</div>
""", unsafe_allow_html=True)

mode = st.sidebar.radio(
    "WORKSPACE",
    ["Dashboard", "Circuit Diagnosis", "Signal Analyzer", "Engineering Lab"],
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    '<div class="small-muted">V3 • Local Development<br>Engineering diagnostic toolkit</div>',
    unsafe_allow_html=True
)


def hero(title, subtitle):
    st.markdown(
        f"""
        <div class="hero">
            <div class="status"><span class="dot"></span> SYSTEM READY</div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------- Dashboard ----------
if mode == "Dashboard":
    hero(
        "Engineering Intelligence, simplified.",
        "Analyze circuits, inspect signals and solve electronics problems from one clean workspace."
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="card"><div class="card-label">ANALYSIS MODES</div><div class="card-value">4</div><div class="card-note">Core workspaces</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><div class="card-label">LAB TOOLS</div><div class="card-value">17+</div><div class="card-note">Engineering calculations</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card"><div class="card-label">SIGNAL TOOLS</div><div class="card-value">FFT</div><div class="card-note">RMS • Peak • Frequency</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="card"><div class="card-label">DIAGNOSTICS</div><div class="card-value">AI Ready</div><div class="card-note">Fault analysis engine</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Explore the workspace</div>', unsafe_allow_html=True)

    cols = st.columns(4)
    modules = [
        ("01", "Circuit Diagnosis", "Compare expected and measured values, calculate health and identify abnormal circuit behavior."),
        ("02", "Signal Analyzer", "Upload real measurements and inspect waveform, RMS, noise and frequency spectrum."),
        ("03", "Engineering Lab", "Solve common DC, AC, semiconductor and time-constant calculations."),
        ("04", "Diagnostic Engine", "Turn measurements into practical fault findings with confidence and recommended checks."),
    ]

    for col, (num, title, desc) in zip(cols, modules):
        with col:
            st.markdown(
                f'<div class="module"><div class="card-label">{num}</div><h3>{title}</h3><p>{desc}</p></div>',
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-title">Recommended workflow</div>', unsafe_allow_html=True)
    st.info("Start with Circuit Diagnosis for component measurements, or open Signal Analyzer if you already have a CSV waveform.")


# ---------- Circuit Diagnosis ----------
elif mode == "Circuit Diagnosis":
    hero(
        "Circuit Diagnosis",
        "Compare expected and measured behavior to detect abnormal circuit conditions."
    )

    left, right = st.columns(2, gap="large")
    with left:
        st.markdown(
            '<div class="section-title">Expected circuit</div>',
            unsafe_allow_html=True,
        )

        circuit_type = st.selectbox(
            "Circuit type",
            ["Resistive Load", "LED + Resistor"],
        )

        supply = st.number_input(
            "Supply voltage (V)",
            min_value=0.0,
            value=5.0,
            step=0.1,
        )

        resistance = st.number_input(
            "Resistance (Ω)",
            min_value=0.01,
            value=220.0,
            step=10.0,
        )

        if circuit_type == "Resistive Load":
            # Ohm's Law
            expected_current = (supply / resistance) * 1000
            expected_output = supply

            st.info(f"Calculated current: **{expected_current:.2f} mA**")
            st.info(f"Expected output: **{expected_output:.2f} V**")

        else:
            led_voltage = st.number_input(
                "LED forward voltage (V)",
                min_value=0.1,
                max_value=5.0,
                value=2.0,
                step=0.1,
            )

            expected_current = max(
                ((supply - led_voltage) / resistance) * 1000,
                0,
            )
            expected_output = led_voltage

            st.info(f"Calculated LED current: **{expected_current:.2f} mA**")
            st.info(f"Expected LED voltage: **{expected_output:.2f} V**")
    with right:
        st.markdown('<div class="section-title">Measured circuit</div>', unsafe_allow_html=True)
        measured_current = st.number_input("Measured current (mA)", min_value=0.0, value=0.0, step=0.1)
        measured_output = st.number_input("Measured output (V)", min_value=0.0, value=0.2, step=0.1)

    if st.button("Run full diagnosis", type="primary", use_container_width=True):
        result = analyze_circuit(
            supply, resistance, expected_current, measured_current,
            expected_output, measured_output
        )
        faults = detect_faults(result)

        st.markdown('<div class="section-title">Circuit health</div>', unsafe_allow_html=True)
        a, b, c, d = st.columns(4)
        a.metric("Health score", f"{result['health_score']}/100")
        b.metric("Calculated current", f"{result['calculated_current_ma']:.2f} mA")
        c.metric("Current error", f"{result['current_error_pct']:.1f}%")
        d.metric("Output error", f"{result['output_error_pct']:.1f}%")

        st.markdown('<div class="section-title">Expected vs measured</div>', unsafe_allow_html=True)
        comparison = pd.DataFrame({
            "Expected": [expected_current, expected_output],
            "Measured": [measured_current, measured_output],
        }, index=["Current (mA)", "Output voltage (V)"])
        st.bar_chart(comparison)

        st.markdown('<div class="section-title">Diagnostic findings</div>', unsafe_allow_html=True)
        if faults:
            for fault in faults:
                if fault["severity"] == "High":
                    st.error(f"{fault['title']}  •  {fault['confidence']}% confidence")
                else:
                    st.warning(f"{fault['title']}  •  {fault['confidence']}% confidence")
                st.write(fault["explanation"])
                with st.expander("Recommended checks"):
                    for check in fault["checks"]:
                        st.write("• " + check)
        else:
            st.success("No major fault pattern detected from the supplied measurements.")


# ---------- Signal Analyzer ----------
elif mode == "Signal Analyzer":
    hero(
        "Signal Analyzer",
        "Turn raw measurement data into useful time-domain and frequency-domain insights."
    )

    uploaded = st.file_uploader("Upload measurement CSV", type=["csv"])

    if not uploaded:
        st.info("Upload a CSV with a time column and a signal column. Try data/sample_signal.csv for a quick test.")
    else:
        df = pd.read_csv(uploaded)

        st.markdown('<div class="section-title">Dataset</div>', unsafe_allow_html=True)
        st.dataframe(df.head(10), use_container_width=True)

        c1, c2 = st.columns(2)
        with c1:
            time_col = st.selectbox("Time column", list(df.columns))
        with c2:
            signal_col = st.selectbox("Signal column", [c for c in df.columns if c != time_col])

        if st.button("Analyze signal", type="primary", use_container_width=True):
            try:
                result = analyze_signal(df[time_col], df[signal_col])

                st.markdown('<div class="section-title">Signal metrics</div>', unsafe_allow_html=True)
                a, b, c, d = st.columns(4)
                a.metric("RMS", f"{result['rms']:.4f}")
                b.metric("Peak", f"{result['peak']:.4f}")
                c.metric("Peak-to-peak", f"{result['peak_to_peak']:.4f}")
                d.metric("Dominant frequency", f"{result['frequency']:.3f} Hz")

                st.markdown('<div class="section-title">Waveform</div>', unsafe_allow_html=True)
                st.line_chart(pd.DataFrame({"Signal": result["clean_signal"]}, index=result["time"]))

                st.markdown('<div class="section-title">FFT spectrum</div>', unsafe_allow_html=True)
                st.line_chart(pd.DataFrame({"Magnitude": result["magnitudes"]}, index=result["frequencies"]))

                st.caption(f"Estimated noise level: {result['noise_std']:.5f}")

            except Exception as e:
                st.error(f"Could not analyze this signal: {e}")


# ---------- Engineering Lab ----------
else:
    hero(
        "Engineering Lab",
        "A practical calculation workspace for electronics students, makers and engineers."
    )

    categories = {
        "DC Circuits": [
            "Ohm's Law", "Power", "Series Resistance", "Parallel Resistance",
            "Voltage Divider", "Current Divider", "KVL Loop Check", "KCL Node Check"
        ],
        "AC Circuits": [
            "Capacitive Reactance", "Inductive Reactance", "RLC Impedance",
            "RLC Resonant Frequency", "AC Power Factor"
        ],
        "Time & Semiconductor": [
            "RC Time Constant", "RL Time Constant", "Diode Series Resistor",
            "Transformer Turns Ratio"
        ]
    }

    c1, c2 = st.columns([1, 2])
    with c1:
        category = st.selectbox("Category", list(categories.keys()))
    with c2:
        calc = st.selectbox("Calculation", categories[category])

    st.markdown("---")

    if calc == "Ohm's Law":
        v = st.number_input("Voltage (V)", min_value=0.0, value=5.0)
        r = st.number_input("Resistance (Ω)", min_value=0.0001, value=1000.0)
        result = calculate(calc, v=v, r=r)
        st.success(f"Current = **{result:.4f} A**  ({result*1000:.3f} mA)")

    elif calc == "Power":
        v = st.number_input("Voltage (V)", min_value=0.0, value=5.0)
        i = st.number_input("Current (A)", min_value=0.0, value=0.02)
        st.success(f"Power = **{calculate(calc, v=v, i=i):.4f} W**")

    elif calc in ["Series Resistance", "Parallel Resistance"]:
        values = st.text_input("Resistor values (Ω), separated by commas", "100,220,330")
        try:
            vals = [float(x.strip()) for x in values.split(",") if x.strip()]
            st.success(f"Equivalent Resistance = **{calculate(calc, values=vals):.4f} Ω**")
        except ValueError:
            st.error("Enter valid numbers separated by commas.")

    elif calc == "Voltage Divider":
        vin = st.number_input("Input voltage (V)", min_value=0.0, value=12.0)
        r1 = st.number_input("R1 (Ω)", min_value=0.0001, value=1000.0)
        r2 = st.number_input("R2 (Ω)", min_value=0.0001, value=1000.0)
        st.success(f"Output voltage = **{calculate(calc, vin=vin, r1=r1, r2=r2):.4f} V**")

    elif calc == "Current Divider":
        total = st.number_input("Total current (A)", min_value=0.0, value=0.01)
        r1 = st.number_input("R1 (Ω)", min_value=0.0001, value=100.0)
        r2 = st.number_input("R2 (Ω)", min_value=0.0001, value=200.0)
        st.success(f"Current through R1 = **{calculate(calc, total=total, r1=r1, r2=r2):.6f} A**")

    elif calc == "KVL Loop Check":
        values = st.text_input("Signed voltage changes", "12,-5,-7")
        try:
            vals = [float(x.strip()) for x in values.split(",") if x.strip()]
            result = calculate(calc, values=vals)
            if abs(result) < 1e-9:
                st.success("KVL satisfied: ΣV = 0 V")
            else:
                st.warning(f"KVL mismatch: ΣV = {result:.4f} V")
        except ValueError:
            st.error("Enter valid voltage values.")

    elif calc == "KCL Node Check":
        entering = st.number_input("Total entering current (A)", min_value=0.0, value=0.02)
        leaving = st.number_input("Total leaving current (A)", min_value=0.0, value=0.02)
        st.success(f"KCL residual = **{calculate(calc, entering=entering, leaving=leaving):.6f} A**")

    elif calc == "Capacitive Reactance":
        f = st.number_input("Frequency (Hz)", min_value=0.0001, value=1000.0)
        c = st.number_input("Capacitance (µF)", min_value=0.000001, value=1.0)
        st.success(f"Xc = **{calculate(calc, f=f, c=c):.4f} Ω**")

    elif calc == "Inductive Reactance":
        f = st.number_input("Frequency (Hz)", min_value=0.0001, value=1000.0)
        l = st.number_input("Inductance (mH)", min_value=0.000001, value=10.0)
        st.success(f"Xl = **{calculate(calc, f=f, l=l):.4f} Ω**")

    elif calc == "RLC Impedance":
        r = st.number_input("Resistance R (Ω)", min_value=0.0, value=100.0)
        l = st.number_input("Inductance L (mH)", min_value=0.0, value=10.0)
        c = st.number_input("Capacitance C (µF)", min_value=0.000001, value=1.0)
        f = st.number_input("Frequency (Hz)", min_value=0.0001, value=1000.0)
        st.success(f"Impedance |Z| = **{calculate(calc, r=r, l=l, c=c, f=f):.4f} Ω**")

    elif calc == "RLC Resonant Frequency":
        l = st.number_input("Inductance (mH)", min_value=0.000001, value=10.0)
        c = st.number_input("Capacitance (µF)", min_value=0.000001, value=1.0)
        st.success(f"Resonant frequency = **{calculate(calc, l=l, c=c):.4f} Hz**")

    elif calc == "AC Power Factor":
        real = st.number_input("Real power P (W)", min_value=0.0, value=80.0)
        apparent = st.number_input("Apparent power S (VA)", min_value=0.0001, value=100.0)
        st.success(f"Power factor = **{calculate(calc, real=real, apparent=apparent):.4f}**")

    elif calc == "RC Time Constant":
        r = st.number_input("Resistance (Ω)", min_value=0.0, value=10000.0)
        c = st.number_input("Capacitance (µF)", min_value=0.000001, value=10.0)
        st.success(f"τ = **{calculate(calc, r=r, c=c):.6f} s**")

    elif calc == "RL Time Constant":
        l = st.number_input("Inductance (mH)", min_value=0.000001, value=100.0)
        r = st.number_input("Resistance (Ω)", min_value=0.0001, value=100.0)
        st.success(f"τ = **{calculate(calc, l=l, r=r):.6f} s**")

    elif calc == "Diode Series Resistor":
        vs = st.number_input("Supply voltage (V)", min_value=0.0, value=5.0)
        vd = st.number_input("Diode forward voltage (V)", min_value=0.0, value=2.0)
        current_ma = st.number_input("Desired current (mA)", min_value=0.001, value=10.0)
        st.success(f"Required series resistor = **{calculate(calc, vs=vs, vd=vd, current_ma=current_ma):.2f} Ω**")

    elif calc == "Transformer Turns Ratio":
        vp = st.number_input("Primary voltage (V)", min_value=0.0001, value=230.0)
        np = st.number_input("Primary turns", min_value=1.0, value=1000.0)
        ns = st.number_input("Secondary turns", min_value=1.0, value=100.0)
        st.success(f"Secondary voltage = **{calculate(calc, vp=vp, np=np, ns=ns):.4f} V**")
