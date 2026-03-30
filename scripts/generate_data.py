from class_mapping import ClassDictionary
import json

cd = ClassDictionary()

classes = {}
for i in range(1, 50001):
    img_name = f"ILSVRC2012_val_{i:08d}.JPEG"
    label = cd.get_val_img_class(img_name)
    folder = cd.get_class_1k_r(label)
    if label not in classes:
        classes[label] = {
            'label': str(label),
            'folder': folder,
            'name': cd.get_gpt_class_name(label),
            'images': []
        }
    classes[label]['images'].append(img_name)

data = [classes[label] for label in sorted(classes.keys())]

with open('classes_data.js', 'w') as f:
    f.write('const CLASSES_DATA = ')
    json.dump(data, f, separators=(',', ':'))
    f.write(';')

print(f"Generated classes_data.js with {len(data)} classes")
