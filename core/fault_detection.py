
def detect_faults(result):
    faults = []
    expected = result["expected_current_ma"]
    measured = result["measured_current_ma"]
    output_expected = result["expected_output"]
    output_measured = result["measured_output"]

    if expected > 0 and measured <= expected * 0.05:
        faults.append({
            "title": "Possible Open Circuit", "confidence": 90, "severity": "High",
            "explanation": "Current is almost zero even though current flow is expected.",
            "checks": ["Check wiring and continuity.", "Verify power and ground.", "Inspect the component path."]
        })
    elif expected > 0 and measured >= expected * 2:
        faults.append({
            "title": "Possible Short Circuit or Wrong Resistance", "confidence": 82, "severity": "High",
            "explanation": "Measured current is much higher than expected.",
            "checks": ["Verify resistor value.", "Check accidental shorts.", "Inspect component placement."]
        })

    if output_expected > 0 and output_measured < output_expected * 0.5:
        faults.append({
            "title": "Output Voltage Too Low", "confidence": 78, "severity": "Medium",
            "explanation": "Measured output is substantially below expected.",
            "checks": ["Check polarity.", "Measure each circuit stage.", "Check loose connections."]
        })
    return faults
