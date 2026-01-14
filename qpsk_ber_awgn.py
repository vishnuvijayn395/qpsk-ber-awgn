import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# =============================
# PARAMETERS
# =============================
N_BITS = 200000                 # total bits (must be even)
EbN0_dB = np.arange(0, 13, 2)   # Eb/N0 range

# =============================
# GRAY-CODED QPSK CONSTELLATION
# =============================
constellation = np.array([
    1 + 1j,     # 00
    -1 + 1j,     # 01
    -1 - 1j,     # 11
    1 - 1j      # 10
]) / np.sqrt(2)

bit_map = np.array([
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0]
])

# =============================
# BIT GENERATION
# =============================
bits = np.random.randint(0, 2, N_BITS)

# =============================
# QPSK MODULATION
# =============================
symbols = []
for i in range(0, N_BITS, 2):
    b = bits[i:i+2]
    idx = np.where((bit_map == b).all(axis=1))[0][0]
    symbols.append(constellation[idx])

symbols = np.array(symbols)

# =============================
# BER SIMULATION
# =============================
ber_sim = []

for ebn0_db in EbN0_dB:

    ebn0 = 10**(ebn0_db / 10)

    # AWGN (CORRECT)
    noise = np.sqrt(1 / (2 * ebn0)) * (
            np.random.randn(len(symbols)) +
            1j * np.random.randn(len(symbols))
    )

    rx = symbols + noise

    # MINIMUM-DISTANCE DETECTION
    rx_bits = []
    for r in rx:
        idx = np.argmin(np.abs(r - constellation))
        rx_bits.extend(bit_map[idx])

    rx_bits = np.array(rx_bits)

    # BER
    ber_sim.append(np.mean(bits != rx_bits))

# =============================
# THEORY
# =============================
ber_theory = 0.5 * erfc(np.sqrt(10**(EbN0_dB / 10)))

# =============================
# PLOT
# =============================
plt.figure()
plt.semilogy(EbN0_dB, ber_sim, 'o-', label='Simulated')
plt.semilogy(EbN0_dB, ber_theory, '--', label='Theory')
plt.grid(True, which='both')
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('Bit Error Rate (BER)')
plt.title('QPSK BER over AWGN')
plt.legend()
plt.show()

# =============================
# PRINT RESULTS
# =============================
print("Eb/N0 (dB):", EbN0_dB)
print("Simulated BER:", ber_sim)
print("Theoretical BER:", ber_theory)
