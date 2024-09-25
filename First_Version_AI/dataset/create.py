import numpy as np
import pandas as pd

# Number of samples
n_samples = 250

# Generate normal vital signs
heart_rate_normal = np.random.randint(60, 101, size=n_samples//2)
blood_pressure_systolic_normal = np.random.randint(90, 121, size=n_samples//2)
blood_pressure_diastolic_normal = np.random.randint(60, 81, size=n_samples//2)
oxygen_saturation_normal = np.random.uniform(95, 100, size=n_samples//2)
temperature_normal = np.random.uniform(36.5, 37.5, size=n_samples//2)
condition_normal = ['Normal'] * (n_samples//2)

# Generate heart attack vital signs
heart_rate_attack = np.random.randint(100, 141, size=n_samples//2)
blood_pressure_systolic_attack = np.random.randint(130, 160, size=n_samples//2)
blood_pressure_diastolic_attack = np.random.randint(90, 110, size=n_samples//2)
oxygen_saturation_attack = np.random.uniform(85, 90, size=n_samples//2)
temperature_attack = np.random.uniform(37.5, 38.5, size=n_samples//2)
condition_attack = ['Heart Attack'] * (n_samples//2)

# Combine normal and heart attack data
heart_rate = np.concatenate([heart_rate_normal, heart_rate_attack])
blood_pressure_systolic = np.concatenate([blood_pressure_systolic_normal, blood_pressure_systolic_attack])
blood_pressure_diastolic = np.concatenate([blood_pressure_diastolic_normal, blood_pressure_diastolic_attack])
oxygen_saturation = np.concatenate([oxygen_saturation_normal, oxygen_saturation_attack])
temperature = np.concatenate([temperature_normal, temperature_attack])
condition = np.concatenate([condition_normal, condition_attack])

# Create a DataFrame
data = {
    'Heart Rate (bpm)': heart_rate,
    'Blood Pressure (Systolic)': blood_pressure_systolic,
    'Blood Pressure (Diastolic)': blood_pressure_diastolic,
    'Oxygen Saturation (%)': oxygen_saturation,
    'Body Temperature (°C)': temperature,
    'Condition': condition
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('vital_signs_dataset_Test.csv', index=False)

print("Dataset generated successfully!")
