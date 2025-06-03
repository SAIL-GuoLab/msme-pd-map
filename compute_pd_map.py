
import nibabel as nib
import numpy as np
import argparse
import os

# Argument parser setup
parser = argparse.ArgumentParser(description='Compute Proton Density (PD) map from two-echo MSME images.')
parser.add_argument('-input1', type=str, required=True, help='Path to first echo NIfTI file (short TE).')
parser.add_argument('-input2', type=str, required=True, help='Path to second echo NIfTI file (long TE).')
parser.add_argument('-TE1', type=float, required=True, help='Echo time of the first image (in ms).')
parser.add_argument('-TE2', type=float, required=True, help='Echo time of the second image (in ms).')
parser.add_argument('-output', type=str, default=None, help='Output file name (NIfTI).')

args = parser.parse_args()

# Load the two echo images
img1 = nib.load(args.input1)
img2 = nib.load(args.input2)

S1 = img1.get_fdata()
S2 = img2.get_fdata()

# Avoid division by zero or log of zero
epsilon = 1e-10
S1 = np.clip(S1, epsilon, np.max(S1))
S2 = np.clip(S2, epsilon, np.max(S2))

# Compute T2 map
T2_map = -(args.TE2 - args.TE1) / np.log(S2 / S1)

# Optional: cap extreme T2 values for stability
T2_map = np.clip(T2_map, 1, 300)  # in ms

# Compute PD map: extrapolate signal to TE = 0
PD_map = S1 * np.exp(args.TE1 / T2_map)

# Determine output file name
if args.output is None:
    base_name = os.path.splitext(os.path.basename(args.input1))[0]
    output_file = f"{base_name}_pd_map.nii.gz"
else:
    output_file = args.output

# Save the PD map as a new NIfTI file with same header and affine
pd_nifti = nib.Nifti1Image(PD_map.astype(np.float32), img1.affine, img1.header)
nib.save(pd_nifti, output_file)

print(f"PD map saved as '{output_file}'")
