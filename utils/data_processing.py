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
                #print(label_key,"has no region.")
            else:
                ##### ImageNAME check
                #print(label_key,"has regions.")
                valid_regions.append(gt_json['assets'][label_key]['regions'])
                #print(gt_json['assets'][label_key]['asset']['name'],"has ",len(gt_json['assets'][label_key]['regions']),"regions")
                # timestamp = gt_json['assets'][label_key]['asset']['timestamp']
                img_name = gt_json['assets'][label_key]['asset']['name']
                gt_data[img_name]=[]
                gt_data[img_name].append({'size':gt_json['assets'][label_key]['asset']['size']})
                valid_regions_count = 0

                ##### Tag error check
                for regions in gt_json['assets'][label_key]['regions']:
                    if len(regions['tags'])<=1:
                        #pass
                        bbox = regions['boundingBox']
                        points = regions['points']
                        gt_data[img_name].append({'label':regions['tags'],
                                            'x': bbox['left'],
                                            'y': bbox['top'],
                                            'w': bbox['width'],
                                            'h': bbox['height']})
                                            #'points': points})#,
                                            #'time_stamp':timestamp })
                        valid_regions_count += 1
                    else:
                        # pass
                        print(gt_json['assets'][label_key]['asset']['name'],regions['id'],"has a tag error")
                if valid_regions_count == 0:
                    print("No valid tag. Please check the tags.")
                    print(img_name,"has been deleted")
                    gt_data.pop(img_name, None)
    # print(video_id,"has",len(all_labeled_keys),"annotated_keys",)
    print("[",video_id,"] has",len(valid_regions),"valid_region_keys" )
    return gt_data