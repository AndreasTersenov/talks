#!/usr/bin/env python3
"""Angular -> comoving conversions for the defense backup card "What these
angular scales are, in megaparsecs" (PhD_Defense_2026, backup column 4).

Prints the table that card hard-codes, so the numbers can be re-derived rather
than trusted.  Cosmology is the cosmoGRID fiducial of the baryonic-feedback
paper: Om = 0.26, h = 0.6736, flat.  Distances in comoving h^-1 Mpc, which is
the unit BAO and sigma_8 are quoted in.

    python3 tools/make-scale-table.py
"""
import numpy as np

OM, H0 = 0.26, 67.36
DH = 2997.92458                       # c / (100 km/s/Mpc), in h^-1 Mpc
ARCMIN = np.pi / (180 * 60)

# nominal scale and measured multipole at peak response, N_side = 512
# (Tersenov et al., baryonic-feedback paper, Table "starlet_bands")
BANDS = [(1, 10, 767), (2, 20, 228), (3, 40, 114), (4, 80, 57)]

# the lensing kernels put their weight here; see the peak calculation below
Z_LO, Z_HI = 0.1, 0.6


def E(z):
    return np.sqrt(OM * (1 + z) ** 3 + (1 - OM))


def chi(z, n=20001):
    """comoving distance to z, in h^-1 Mpc"""
    zz = np.linspace(0.0, z, n)
    return DH * np.trapz(1.0 / E(zz), zz)


def kernel_peak(z_source):
    """z at which the single-source-plane lensing efficiency peaks.

    q(chi) ~ chi (1 - chi/chi_s) / a.  The n(z) of each tomographic bin is
    broad, so this is an indication of where the bin is sensitive, not a
    number to quote on its own.
    """
    zl = np.linspace(0.001, z_source, 2000)[:-1]
    cl = np.array([chi(z) for z in zl])
    cs = chi(z_source)
    return zl[np.argmax(cl * (1 - cl / cs) * (1 + zl))]


def main():
    print("lensing kernel peaks (single source plane)")
    for zs in (0.3, 0.5, 0.7, 0.9):
        print("    source z = %.1f  ->  lenses at z ~ %.2f" % (zs, kernel_peak(zs)))

    c_lo, c_hi = chi(Z_LO), chi(Z_HI)
    print("\nchi(%.1f) = %.0f, chi(%.1f) = %.0f h^-1 Mpc" % (Z_LO, c_lo, Z_HI, c_hi))
    print("\nband  theta  l_peak     R [h^-1 Mpc]       k [h/Mpc]")
    for j, theta, lpeak in BANDS:
        r_lo, r_hi = theta * ARCMIN * c_lo, theta * ARCMIN * c_hi
        k_hi, k_lo = (lpeak + 0.5) / c_lo, (lpeak + 0.5) / c_hi
        print("j=%d   %2d'   %4d    %5.1f - %-5.1f     %5.2f - %.2f"
              % (j, theta, lpeak, r_lo, r_hi, k_hi, k_lo))

    print("\none angular scale spans a factor %.1f in physical scale over that range"
          % (c_hi / c_lo))
    print("map limit   l = 1024  ->  k = %.2f - %.2f h/Mpc" % (1024.5 / c_lo, 1024.5 / c_hi))
    print("PS baryon-safe cut  l = 340  ->  k = %.2f - %.2f h/Mpc" % (340.5 / c_lo, 340.5 / c_hi))


if __name__ == "__main__":
    main()
