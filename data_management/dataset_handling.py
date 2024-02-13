'''
Save Labels without specific condition
'''
def save_labels_cond(gt_data, base_folder, condition_name, img_base_folder):
    saved_file_cnt = 0
    tag_cnt = 0
    for img_name, data_list in gt_data.items():
        folder_name = img_name.split('.m4v')[0]
        labels_folder_path = os.path.join(base_folder, condition_name, folder_name, 'labels')
        images_folder_path = os.path.join(base_folder, condition_name, folder_name, 'images')

        # Create the specific folder for the image if it doesn't exist
        os.makedirs(labels_folder_path, exist_ok=True)
        os.makedirs(images_folder_path, exist_ok=True)

        size_info = data_list[0]['size']
        # Adjusting file name to remove the time stamp and extension for the label file
        label_file_name = img_name.replace('.jpg', '.txt')
        label_file_path = os.path.join(labels_folder_path, label_file_name)

        with open(label_file_path, 'w') as file:
            for region_info in data_list[1:]:
                class_id = 0  # Update this according to your class ID mapping
                x, y, w, h = convert_to_yolo(size_info, region_info)
                file.write(f"{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")
                tag_cnt += 1
                #print(f"{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")

        # print(f"{label_file_name} was created")
        saved_file_cnt += 1
        original_img_path = os.path.join(img_base_folder,folder_name,'images',img_name)
        # print("ori_img_path:",original_img_path)
        dest_img_path = os.path.join(images_folder_path, img_name)
        print(f"{img_name} was created")
        shutil.copy(original_img_path, dest_img_path)
    if saved_file_cnt == 0:
        print("There is no Labels")
    print(f"-------- {saved_file_cnt} files were created,({tag_cnt} tags are saved.)")
