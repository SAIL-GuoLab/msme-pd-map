# compute_pd_map.py

This script computes a Proton Density (PD) map from two aligned echo images acquired with different echo times (TEs) using a Multi-Slice Multi-Echo (MSME) approach.

## Requirements

- Python 3
- nibabel
- numpy

You can install the required packages with:

```bash
pip install nibabel numpy
```

## Usage

```bash
python3 compute_pd_map.py -input1 <echo1.nii.gz> -input2 <echo2.nii.gz> -TE1 <short_TE> -TE2 <long_TE> [-output <output_filename>]
```

### Example 1: Specify all arguments including output filename

```bash
python3 compute_pd_map.py -input1 echo1.nii.gz -input2 echo2.nii.gz -TE1 10 -TE2 80 -output my_pd_map.nii.gz
```

### Example 2: Use default output filename

```bash
python3 compute_pd_map.py -input1 echo1.nii.gz -input2 echo2.nii.gz -TE1 10 -TE2 80
# Output: echo1_pd_map.nii.gz
```
