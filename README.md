# QPSK BER Performance over AWGN Channel

## Overview
This project presents a simulation-based analysis of the Bit Error Rate (BER) performance of a Gray-coded Quadrature Phase Shift Keying (QPSK) communication system over an Additive White Gaussian Noise (AWGN) channel. The simulated BER results are compared with theoretical BER expressions to validate system correctness.

## Objective
- Implement a Gray-coded QPSK modulator and demodulator
- Model an AWGN channel using Eb/N0
- Evaluate BER using Monte Carlo simulation
- Compare simulated BER with theoretical performance

## System Description
The communication system follows this baseband model:
Random Bits → QPSK Modulation → AWGN Channel → Detection → BER Calculation

Key assumptions:
- Ideal synchronization
- No RF impairments
- AWGN-only channel

## Key Concepts Used
- Quadrature Phase Shift Keying (QPSK)
- Gray coding
- AWGN noise modeling
- Eb/N0 based noise scaling
- Maximum likelihood (minimum-distance) detection
- Monte Carlo BER estimation

## Results
The simulated BER curve closely follows the theoretical BER curve for QPSK over an AWGN channel.
Minor deviations at high Eb/N0 values are expected due to finite simulation length.

## Tools & Technologies
- Python
- NumPy
- Matplotlib
- SciPy

## How to Run
```bash
python qpsk_ber_awgn.py
