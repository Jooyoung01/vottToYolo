import argparse
from utils import get_gt_data, img_matching_check
from data_management.label_saving import save_labels
import json

def main(vott_file, video_names, target_folder, video_ext, img_path, save_labels_flag):
    video_names_list = video_names.split(',')
    # Process each video
    gt_data_all = [get_gt_data(vott_file, vid) for vid in video_names_list]
    img_matching_check(gt_data_all, [img_path])

    # Save labels for each video
    if save_labels_flag:
        for data in gt_data_all:
            save_labels(data, target_folder, video_ext)
    else:
        print("Skipping label saving... Please use '--save_labels' arg to enable label saving.")
    # If you want to print the gt_data, you can do so here
    # for gt_data in gt_data_all:
    #     print(json.dumps(gt_data, indent=4, sort_keys=True))

if __name__ == "__main__":
    description_text = """
    ######### VoTT to YOLO format Converter #########
    Converts annotations from VoTT JSON format to YOLO format.
    
    Usage:
    python ./vott_to_yolo.py 
        --vott_file ./video/truckLabeling-export.json 
        --video_names REG_long_710_day_2-01_clip1,REG_long_710_day_2-01_clip2 
        --target_folder ./output 
        --video_ext .mov 
        --img_path ./video/vott-json-export
        --save_labels
    """
    parser = argparse.ArgumentParser(description="Convert VoTT JSON to YOLO format.", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--vott_file', type=str, required=True,
                        help='Path to the VoTT JSON file.\nExample: ./video/truckLabeling-export.json')
    parser.add_argument('--video_names', type=str, required=True,
                        help='Comma-separated list of video names without spaces.\nExample: REG_long_710_day_2-01_clip1,REG_long_710_day_2-01_clip2')
    parser.add_argument('--target_folder', type=str, required=True,
                        help='Path to the folder where output will be saved.\nExample: ./output')
    parser.add_argument('--video_ext', type=str, default='.mov',
                        help='Video file extension (default: .mov).\nExample: .mov')
    parser.add_argument('--img_path', type=str, required=True,
                        help='Path to the image folder for VoTT JSON export.\nExample: ./video/vott-json-export')
    parser.add_argument('--save_labels', action='store_true',
                        help='Enable this flag to save labels for each video.')

    args = parser.parse_args()
    main(args.vott_file, args.video_names, args.target_folder, args.video_ext, args.img_path, args.save_labels)




