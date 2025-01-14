import json

def get_gt_data(vott_file_name, video_id):
    """
    Get ground truth
    """
    f = open(vott_file_name)
    gt_json = json.load(f)
    gt_data = {}
    all_labeled_keys = []
    valid_regions = []

    for label_key in gt_json['assets']:
        if video_id in gt_json['assets'][label_key]['asset']['name']:
            ##### KEY check
            all_labeled_keys.append(label_key)

            ##### REGION check(get valid tags)
            if not gt_json['assets'][label_key]['regions']:
                pass
                # print(label_key, "has no region.")
            else:
                ##### ImageNAME check
                valid_regions.append(gt_json['assets'][label_key]['regions'])
                img_name = gt_json['assets'][label_key]['asset']['name']
                gt_data[img_name] = []
                gt_data[img_name].append({'size': gt_json['assets'][label_key]['asset']['size']})
                valid_regions_count = 0

                ##### Tag processing
                for regions in gt_json['assets'][label_key]['regions']:
                    if len(regions['tags']) > 1:
                        # print(f"> Tag error: {gt_json['assets'][label_key]['asset']['name']} region {regions['id']} has multiple tags: {regions['tags']}")
                        selected_tag = regions['tags'][-1]
                        # print(f">> Selected tag: {selected_tag}")
                    elif len(regions['tags']) == 1:
                        selected_tag = regions['tags'][0]
                    else:
                        print(f"{gt_json['assets'][label_key]['asset']['name']} region {regions['id']} has no tags")
                        continue

                    bbox = regions['boundingBox']
                    points = regions['points']
                    gt_data[img_name].append({
                        'label': selected_tag,
                        'x': bbox['left'],
                        'y': bbox['top'],
                        'w': bbox['width'],
                        'h': bbox['height']
                    })
                    valid_regions_count += 1

                if valid_regions_count == 0:
                    print("No valid tag. Please check the tags.")
                    print(img_name, "has been deleted")
                    gt_data.pop(img_name, None)

    print("[", video_id, "] has", len(valid_regions), "valid_region_keys")
    return gt_data
