# medical_image_process

My Senior Course

## Data Preprocess

### Require medical data (dicom file) 

1. Put the dicom file in src/data/raw_data

2. The output will be reposit at src/data/process_data

### Dicom file standard

1. (0028, xxxx) is all the information about the dicom image

2. It can be show by the following code

```
img = pydicom.dcmread(path)
print(img)
```

### Linear conversion

1. The following two properties specify a linear conversion

2. Each pair represent a brightness parameter to it's dicom file

```
(0028, 1050) Window Center                       DS: ['8408', '8443', '8408', '8497', '8443']
(0028, 1051) Window Width                        DS: ['1608', '1787', '1608', '1965', '1787']
```
[ref1](https://dicom.innolitics.com/ciods/digital-x-ray-image/dx-image/00281055)
[ref2](https://gist.github.com/PurpleBooth/b24679402957c63ec426) about Window Center & Window Width