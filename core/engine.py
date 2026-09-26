
def percentage_error(expected, measured):
    if expected == 0:
        return 0.0
    return abs(measured - expected) / abs(expected) * 100

def analyze_circuit(supply, resistance, expected_current_ma, measured_current_ma,
                    expected_output, measured_output):
    calculated_current_a = supply / resistance
    calculated_current_ma = calculated_current_a * 1000
    power_w = supply * calculated_current_a
    current_error = percentage_error(expected_current_ma, measured_current_ma)
    output_error = percentage_error(expected_output, measured_output)
    score = 100 - min(current_error * 0.5, 50) - min(output_error * 0.5, 40)
    return {
        "calculated_current_ma": calculated_current_ma,
        "current_error_pct": current_error,
        "output_error_pct": output_error,
        "power_w": power_w,
        "health_score": max(0, round(score)),
        "expected_current_ma": expected_current_ma,
        "measured_current_ma": measured_current_ma,
        "expected_output": expected_output,
        "measured_output": measured_output,
    }
