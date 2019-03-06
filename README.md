# medical_image_process

My Senior Course

## Data Preprocess

Doing Data Preprocessing

### Task 

1. Require medical data (dicom file)
    - put the dicom file in src/data/raw_data

2. Dicom file standard
    - (0028, xxxx) is all the information about the dicom image

it can be show by the following code

```
img = pydicom.dcmread(path)
print(img)
```

3. Linear Conversion

```
(0028, 1050) Window Center                       DS: ['8408', '8443', '8408', '8497', '8443']
(0028, 1051) Window Width                        DS: ['1608', '1787', '1608', '1965', '1787']
```

These two properties specify a linear conversion (unless otherwise specified by the value of VOI LUT Function (0028,1056); from the output of the (conceptual) Modality LUT values to the input to the (conceptual) Presentation LUT. Window Center contains the value that is the center of the window. Window Width contains the width of the window.

[more info](https://gist.github.com/PurpleBooth/b24679402957c63ec426)