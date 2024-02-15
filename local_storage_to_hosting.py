import os
import json
import argparse


def local_storage_to_hosting(port, filepath, replacements):

    # Sample output: Load the file from the filepath and print out the first object
    new_data = []
    with open(filepath, 'r') as f:
        data = json.load(f)
        for obj in data:
            for key in replacements:
                obj['data']['image'] = obj['data']['image'].replace(key, replacements[key])
            # print(obj['data']['image'])
            new_data.append(obj)
    # Save the new data to the same file location, appending the port number to the filename
    with open(filepath.replace('.json', f'_{port}.json'), 'w') as f:
        json.dump(new_data, f)


if __name__ == "__main__":
    port_num = 3030
    path_to_ls_annotations = os.path.abspath('./outputs/yolo_seg.json')
    path_to_images_directory = ''  # Empty string if the images are located at localhost:port_num with no path
    # Accept the port and filepath as arguments (-p and -f)
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int,
                        help='Port number to replace in the local storage path',
                        default=port_num)
    parser.add_argument('-ls', '--lsannotations', type=str,
                        help='Path to the Label Studio annotations file',
                        default=path_to_ls_annotations)
    parser.add_argument('-fp', '--filepath', type=str,
                        help='relative path from the root of the source files to the images directory'
                             ' (e.g. if serve-data.py is run from ~/data, and the images are in ~/data/yolo/images,'
                             ' the relative path is "yolo/images"',
                        default=path_to_images_directory)
    args = parser.parse_args()
    port_num = args.port
    path_to_ls_annotations = args.lsannotations
    path_to_images_directory = args.filepath
    if path_to_images_directory != '' and path_to_images_directory[0] != '/':
        path_to_images_directory = '/' + path_to_images_directory
    if path_to_images_directory != '' and path_to_images_directory[-1] == '/':
        path_to_images_directory = path_to_images_directory[:-1]

    replacement_strings = {
        '/data/local-files/?d=': f'http://localhost:{port_num}{path_to_images_directory}',
        '@': '%40'
    }

    local_storage_to_hosting(port_num, path_to_ls_annotations, replacement_strings)
