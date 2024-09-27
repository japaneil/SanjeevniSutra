import numpy as np
import pandas as pd

# Number of samples
n_samples = 1000  # Split among Normal, Heart Attack, and Cardiac Arrest

# Generate normal vital signs (same as before)
heart_rate_normal = np.random.randint(60, 101, size=n_samples//3)
blood_pressure_systolic_normal = np.random.randint(90, 121, size=n_samples//3)
blood_pressure_diastolic_normal = np.random.randint(60, 81, size=n_samples//3)
oxygen_saturation_normal = np.random.uniform(95, 100, size=n_samples//3)
temperature_normal = np.random.uniform(36.5, 37.5, size=n_samples//3)
condition_normal = ['Normal'] * (n_samples//3)

# Generate heart attack vital signs (same as before)
heart_rate_attack = np.random.randint(100, 141, size=n_samples//3)
blood_pressure_systolic_attack = np.random.randint(130, 160, size=n_samples//3)
blood_pressure_diastolic_attack = np.random.randint(90, 110, size=n_samples//3)
oxygen_saturation_attack = np.random.uniform(85, 90, size=n_samples//3)
temperature_attack = np.random.uniform(37.5, 38.5, size=n_samples//3)
condition_attack = ['Heart Attack'] * (n_samples//3)

# Generate cardiac arrest vital signs
heart_rate_arrest = np.random.randint(0, 10, size=n_samples//3)  # Near-zero heart rate
blood_pressure_systolic_arrest = np.random.randint(0, 30, size=n_samples//3)
blood_pressure_diastolic_arrest = np.random.randint(0, 20, size=n_samples//3)
oxygen_saturation_arrest = np.random.uniform(60, 70, size=n_samples//3)
temperature_arrest = np.random.uniform(36.0, 36.5, size=n_samples//3)
condition_arrest = ['Cardiac Arrest'] * (n_samples//3)

# Combine all data
heart_rate = np.concatenate([heart_rate_normal, heart_rate_attack, heart_rate_arrest])
blood_pressure_systolic = np.concatenate([blood_pressure_systolic_normal, blood_pressure_systolic_attack, blood_pressure_systolic_arrest])
blood_pressure_diastolic = np.concatenate([blood_pressure_diastolic_normal, blood_pressure_diastolic_attack, blood_pressure_diastolic_arrest])
oxygen_saturation = np.concatenate([oxygen_saturation_normal, oxygen_saturation_attack, oxygen_saturation_arrest])
temperature = np.concatenate([temperature_normal, temperature_attack, temperature_arrest])
condition = np.concatenate([condition_normal, condition_attack, condition_arrest])

# Ensure all variables have the same length
print(f"Total samples: {len(heart_rate)}")
print(f"Heart rate samples: {len(heart_rate)}")
print(f"Systolic BP samples: {len(blood_pressure_systolic)}")
print(f"Diastolic BP samples: {len(blood_pressure_diastolic)}")
print(f"Oxygen saturation samples: {len(oxygen_saturation)}")
print(f"Temperature samples: {len(temperature)}")
print(f"Condition samples: {len(condition)}")

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
df.to_csv('vital_signs_dataset_Test_NHC.csv', index=False)

print("Dataset generated successfully!")
