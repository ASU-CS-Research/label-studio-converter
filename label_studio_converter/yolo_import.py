import os
from label_studio_converter.imports import yolo as import_yolo


input_data_dir = os.path.abspath('/home/bee/stripe-segmentation/train')
if not os.path.exists(input_data_dir):
    print(f'input_data_dir: {input_data_dir} does not exist!')
    exit(1)

output_data_file = os.path.abspath('./outputs/yolo_seg.json')
image_ext = '.png'

import_yolo.convert_yolo_to_ls(
    input_dir=input_data_dir,
    out_file=output_data_file,
    image_ext=image_ext,
    yolo_type="polygonlabels"
)

