import glob
import os

def img_matching_check(gt_data, img_paths=[]):
    print(img_paths)
    error_check = 0
    img_tag_matched_by_path = {path: [] for path in img_paths}
    # img_tag_mached = []
    for gt_data_each in gt_data:
        for img_name in gt_data_each.keys():
            print(img_name)
            file_found = False  # file found flag
            img_name_with_ext = img_name + ".jpg" 
            for img_path in img_paths:
                full_path = os.path.join(img_path, img_name_with_ext) 
                matching_files = glob.glob(full_path)
                if matching_files:
                    file_found = True
                    img_tag_matched_by_path[img_path].extend(matching_files)
                    break
        if not file_found:
            error_check += 1
            print(f"Error: {img_name} not found.") 
    for path, matched_files in img_tag_matched_by_path.items():
        print(f"Total # of images in {path} : {sum(1 for file in os.listdir(path) if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')))}")
        print(f"Total # of images matching gt_data : {len(matched_files)}")
        if error_check >= 1:
            print("Please check for images where errors occurred!")
        # for file in matched_files:
        #     print(f"  {file}")
