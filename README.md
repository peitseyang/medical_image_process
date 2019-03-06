# medical_image_process

My Senior Course

## Data Preprocess

Doing Data Preprocessing

### Task 

1. Require medical data (dicom file)
    - put the dicom file in src/data/raw_data

2. Dicom file standard
    - (0028, xxxx) is all the information about the dicom image

    - it can be show by the following code

```
img = pydicom.dcmread(path)
print(img)
```

3. Linear Conversion
    - The following two properties specify a linear conversion 

```
(0028, 1050) Window Center                       DS: ['8408', '8443', '8408', '8497', '8443']
(0028, 1051) Window Width                        DS: ['1608', '1787', '1608', '1965', '1787']
```
[moreInfo1](https://dicom.innolitics.com/ciods/digital-x-ray-image/dx-image/00281055)
[moreInfo2](https://gist.github.com/PurpleBooth/b24679402957c63ec426)