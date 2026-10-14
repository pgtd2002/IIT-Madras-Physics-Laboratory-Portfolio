# IIT Madras Physics Laboratory Portfolio

A curated collection of course-based experimental laboratory reports completed during my M.Sc. studies in Physics at the **Indian Institute of Technology Madras (IIT Madras)**.

The portfolio brings together practical work in **semiconductor and materials characterization, thin-film metrology, electronics, experimental instrumentation, microwave measurements, signal detection, and computational analysis**.

> **Academic context:** The reports document laboratory experiments and analysis undertaken as part of coursework. They are presented as evidence of experimental methods, measurement techniques, data analysis, and technical reporting—not as independent industrial projects.

## Featured Work

### 1. Semiconductor & Materials Characterization

| Experiment | Work covered | Report |
|---|---|---|
| **Four-Probe Resistivity & Band-Gap Estimation** | Studied temperature-dependent semiconductor resistivity; used curve fitting to estimate band-gap energy and discussed measurement errors. | [`lab_sem_3_band_gap_four_probe.pdf`](01-semiconductor-and-materials/four-probe-band-gap/lab_sem_3_band_gap_four_probe.pdf) |
| **Hall Effect in a p-Type Semiconductor** | Investigated the temperature dependence of the Hall coefficient; included electromagnet calibration and estimation of the carrier-type inversion temperature. | [`lab_sem_3_hall_effect.pdf`](01-semiconductor-and-materials/hall-effect-temperature-dependence/lab_sem_3_hall_effect.pdf) |
| **Spectroscopic Ellipsometry & Thin-Film Characterization** | Characterized SiO₂ thin films using a Cauchy dispersion model to estimate film thickness, refractive index, and extinction coefficient. | [`lab_sem_3_Spectroscopic_Ellipsometry.pdf`](01-semiconductor-and-materials/spectroscopic-ellipsometry/lab_sem_3_Spectroscopic_Ellipsometry.pdf) |
| **Solar-Cell I–V Characteristics & Efficiency** | Analyzed I–V measurements at different illumination distances; calculated maximum power, fill factor, conversion efficiency, and propagated uncertainties. | [`lab_sem_3_Solar_Panel.pdf`](01-semiconductor-and-materials/solar-cell-iv-efficiency/lab_sem_3_Solar_Panel.pdf) |
| **X-Ray Powder Diffraction (XRD)** | Examined diffraction peak broadening and used peak fitting, instrumental-broadening estimates, Scherrer analysis, and Williamson–Hall analysis. | [`lab_sem3_XRD.pdf`](01-semiconductor-and-materials/x-ray-diffraction/lab_sem3_XRD.pdf) |
| **Temperature & Frequency Dependence of Dielectric Constant** | Studied dielectric properties of barium titanate using a Schering-bridge setup, including frequency and temperature dependence. | [`lab_sem_3_dielectric_constant.pdf`](01-semiconductor-and-materials/dielectric-constant-temperature-frequency/lab_sem_3_dielectric_constant.pdf) |
| **Contact Angle & Surface Wettability** | Used ImageJ-based contact-angle measurements to study wetting behavior and surface wettability on different surfaces. | [`lab_sem_2_contact_angle.pdf`](01-semiconductor-and-materials/contact-angle-wettability/lab_sem_2_contact_angle.pdf) |

### 2. Electronics, Instrumentation & Measurement

| Experiment | Work covered | Report |
|---|---|---|
| **Arduino-Based Sensor Automation & Motion Control** | Programmed LED PWM and stepper-motor control; interfaced a Hall-effect sensor for magnetic-field measurements and examined motion resolution, backlash, and ADC effects. | [`lab_sem_2_audrino.pdf`](02-electronics-and-instrumentation/arduino-sensor-automation/lab_sem_2_audrino.pdf) |
| **Digital Frequency Counter** | Worked with Arduino, digital integrated circuits, JK flip-flop logic, and a display-based frequency-measurement setup. | [`lab_sem_2_frequency_counter.pdf`](02-electronics-and-instrumentation/digital-frequency-counter/lab_sem_2_frequency_counter.pdf) |
| **Lock-In Amplifier & Weak-Signal Detection** | Investigated phase-sensitive detection, reference-frequency matching, frequency components, noise rejection, and resistance measurement in a voltage-divider circuit. | [`lab_sem_2_Lock_In_Amplifier.pdf`](02-electronics-and-instrumentation/lock-in-amplifier/lab_sem_2_Lock_In_Amplifier.pdf) |
| **Falling Magnet & Electromagnetic Induction** | Used pickup coils and an oscilloscope to study magnet motion through plastic, aluminium, and copper tubes and compare the effects of induced currents. | [`lab_sem_2_falling_magnet.pdf`](02-electronics-and-instrumentation/falling-magnet-induction/lab_sem_2_falling_magnet.pdf) |
| **Electron Spin Resonance (ESR)** | Analyzed resonance measurements and fitted experimental data to estimate the electron g-factor, with an error analysis. | [`lab_sem_3_ESR.pdf`](02-electronics-and-instrumentation/esr-g-factor/lab_sem_3_ESR.pdf) |
| **Franck–Hertz Experiment** | Studied electron excitation in an argon-filled tube by examining plate current as a function of accelerating voltage. | [`lab_sem_3_frank_hertz.pdf`](02-electronics-and-instrumentation/franck-hertz/lab_sem_3_frank_hertz.pdf) |

### 3. Microwave Measurements & Communications

| Experiment | Work covered | Report |
|---|---|---|
| **Microwave Bridge Dielectric Characterization** | Used a calibrated microwave-bridge setup with a source, waveguide, detector, and probe to measure dielectric properties of solid samples. | [`lab_sem_3_microwave_bridge.pdf`](03-microwave-and-communications/microwave-bridge-dielectric-characterization/lab_sem_3_microwave_bridge.pdf) |

### 4. Computational & Statistical Physics

| Experiment | Work covered | Report |
|---|---|---|
| **Electrical Resistance & Percolation Transition** | Studied how resistance changes as bonds are removed from a two-dimensional lattice and examined behavior near the percolation threshold. | [`lab_sem_2_percolation.pdf`](04-computational-physics/percolation-resistance-transition/lab_sem_2_percolation.pdf) |

### 5. Virtual Laboratory

| Experiment | Work covered | Report |
|---|---|---|
| **Geiger–Müller Counter & Radioactive Decay** | Virtual laboratory work involving GM-counter operation, operating-voltage behavior, radiation counting, and radioactive half-life estimation. | [`lab_sem_2_Virtual_lab_on_GM_counter.pdf`](05-virtual-laboratories/geiger-muller-counter-radioactive-decay/lab_sem_2_Virtual_lab_on_GM_counter.pdf) |

## Techniques & Tools Covered

- **Semiconductor and device characterization:** four-probe resistivity, Hall-effect measurements, solar-cell I–V analysis, thin-film ellipsometry, XRD, dielectric characterization, and contact-angle analysis.
- **Electronics and instrumentation:** Arduino, PWM, stepper-motor control, Hall sensors, JK flip-flop circuitry, frequency counting, oscilloscope measurements, and lock-in amplification.
- **Microwave and signal measurements:** microwave-bridge measurements, phase-sensitive detection, frequency response, and measurement calibration.
- **Data analysis:** curve fitting, parameter extraction, graphical analysis, and experimental error/uncertainty analysis.
- **Scientific computing:** Python-based analysis was used in the corresponding work; report-specific code and data should be included only where available and permitted to share.

## Repository Organization

Each experiment has its own folder containing the full report and, where available and appropriate, a short `README.md`, figures, data, or analysis code.

```text
IITM-Physics-Laboratory-Portfolio/
├── README.md
├── 01-semiconductor-and-materials/
│   ├── four-probe-band-gap/
│   ├── hall-effect-temperature-dependence/
│   ├── spectroscopic-ellipsometry/
│   ├── solar-cell-iv-efficiency/
│   ├── x-ray-diffraction/
│   ├── dielectric-constant-temperature-frequency/
│   └── contact-angle-wettability/
├── 02-electronics-and-instrumentation/
│   ├── arduino-sensor-automation/
│   ├── digital-frequency-counter/
│   ├── lock-in-amplifier/
│   ├── falling-magnet-induction/
│   ├── esr-g-factor/
│   └── franck-hertz/
├── 03-microwave-and-communications/
│   └── microwave-bridge-dielectric-characterization/
├── 04-computational-physics/
│   └── percolation-resistance-transition/
└── 05-virtual-laboratories/
    └── geiger-muller-counter-radioactive-decay/
```

## Notes

- Reports are organized by technical theme so that relevant work can be found quickly.
- The repository is intended to demonstrate experimental familiarity, data analysis, and technical documentation.
- Additional datasets, scripts, or plots should only be included when they are genuinely available and permitted to be shared.
- Any industrial R&D material is kept separate and is not included here unless it is approved for public release.
