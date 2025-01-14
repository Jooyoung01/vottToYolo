import os
from utils import convert_to_yolo
"""
Convert vott bbox coordinates to YOLO format.
"""
def save_labels(gt_data,target_base_folder, video_ext):
    for img_name, data_list in gt_data.items():
        folder_name = img_name.split(video_ext)[0]
        labels_folder_path = os.path.join(target_base_folder, folder_name, 'labels')
        os.makedirs(labels_folder_path, exist_ok=True)
        size_info = data_list[0]['size']
        label_file_name = img_name + ".txt"
        label_file_path = os.path.join(labels_folder_path, label_file_name)

        with open(label_file_path, 'w') as file:
            for region_info in data_list[1:]:
                class_id = 0  # Update this according to your class ID mapping
                x, y, w, h = convert_to_yolo(size_info, region_info)
                file.write(f"{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")
                #print(f"{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")
        # print(f"{label_file_name} was created")