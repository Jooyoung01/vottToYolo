# VoTT to YOLO Format Converter

Converts annotations from VoTT JSON format to YOLO format.

https://github.com/microsoft/VoTT</br>
https://github.com/ultralytics/yolov5

## Usage

Run the script from the command line using the following syntax(Example):

```bash
python ./vott_to_yolo.py \
    --vott_file ./video/truckLabeling-export.json \
    --video_names REG_long_710_day_2-01_clip1,REG_long_710_day_2-01_clip2 \
    --target_folder ./output \
    --video_ext .mov \
    --img_path ./video/vott-json-export \
    --save_labels

### Reporting Bugs or Requesting Features

If you encounter any bugs or have a feature request, please file an issue using our Issues section. Provide as much detail as you can to help us understand the problem or the proposed feature.
