import os
from typing import Optional
import argparse
from label_studio_converter.imports import yolo as import_yolo


ACCEPTED_YOLO_ANNOTATION_TYPES = ['rectanglelabels', 'polygonlabels']


def yolo_import(input_data_dir: str, output_filepath: str, yolo_type: str, image_ext: Optional[str] = '.png'):
    if not os.path.exists(input_data_dir):
        print(f'Input data directory: {input_data_dir} does not exist!')
    elif not os.path.exists(os.path.join(input_data_dir, "labels")) \
        or not os.path.exists(os.path.join(input_data_dir, "images")) \
        or not os.path.exists(os.path.join(input_data_dir, "classes.txt")):
        print(f'Input data directory: {input_data_dir} does not contain the required subdirectories and files!\n'
              f'Please ensure that the input data directory contains the following subdirectories and files:\n'
              f'labels/, images/, classes.txt')
    elif os.path.exists(output_filepath):
        print(f'Output file: {output_filepath} already exists! Please specify a new output file.')
    elif not output_file.endswith('.json'):
        print(f'Output file: {output_filepath} must be a json file!')
    elif yolo_type not in ACCEPTED_YOLO_ANNOTATION_TYPES:
        print(f'Invalid YOLO annotation type: "{yolo_type}", Must be one of: {ACCEPTED_YOLO_ANNOTATION_TYPES}')
    else:
        import_yolo.convert_yolo_to_ls(
            input_dir=input_data_dir,
            out_file=output_filepath,
            image_ext=image_ext,
            yolo_type=yolo_type
        )


if __name__ == '__main__':
    input_data_directory = os.path.abspath('/home/bee/stripe-segmentation/test')
    yolo_annotations_type = accepted_yolo_annotation_types[1]
    image_extensions = '.png'
    output_data_file = os.path.abspath('./outputs/yolo.json')
    # Accept the above four parameters as arguments (-i, -o, -y, -e)
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='Path to the input data directory',
                        default=input_data_directory)
    parser.add_argument('-o', '--output', type=str,
                        help='Path to an output file. This file must not already exist, and must be a json file.',
                        default=output_data_file)
    parser.add_argument('-y', '--yolo-type', type=str,
                        help=f'Type of YOLO annotations, any of: {accepted_yolo_annotation_types}',
                        default=yolo_annotations_type)
    parser.add_argument('-e', '--image-ext', type=str, help='Image extension to search as a comma '
                                                            'separated string, e.g. ".jpg,.jpeg,.png"',
                        default=image_extensions)
    args = parser.parse_args()
    input_data_directory = args.input
    output_data_file = args.output

    yolo_annotations_type = args.yolo_type
    image_extensions = args.image_ext

    yolo_import(input_data_directory, output_data_file, yolo_annotations_type, image_extensions)
