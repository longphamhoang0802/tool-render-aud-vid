import os


def config_data(self, bientap_id):        
    file = os.path.join(DIR_UPLOAD, bientap_id + ".txt")
    response = {"arr_audio": [],
                "arr_effect": [],
                "video_effect": "",
                "video_2d": "",
                "crop_effect_status": "",
                "crop_effect": {},
                "sceneChange": "",
                "frame": "",
                "arr_logo": []
                }
    with open(file, encoding="UTF-8") as fp:
        for cnt, line in enumerate(fp):
            line = line.replace("\n", "")
            # audio
            if line.startswith("audio:"):
                full_line = line.replace("audio:", DIR_HOME)
                video = {"path": str(full_line).split("&&duration")[0],
                        "duration": str(full_line).split("&&duration=")[-1].split("&&croptime=")[0],
                        "range_time": str(full_line).split("&&croptime=")[-1]}
                response['arr_audio'].append(video)
            # video
            if line.startswith("effect:"):
                effect = {"path": line.replace("effect:http://171.244.10.137:13000", DIR_HOME)}
                effect = {"path": line.replace("effect:http://210.245.90.204:13000", DIR_HOME)}
                response['arr_effect'].append(effect)
            # video effect
            if line.startswith("video_effect_file:"):
                video_effect = {"path": line.replace("video_effect_file:http://171.244.10.137:13000", DIR_HOME)}
                video_effect = {"path": line.replace("video_effect_file:http://210.245.90.204:13000", DIR_HOME)}
                response['video_effect'] = video_effect
            if line.startswith("video_2d_file:"):
                video_2d = line.replace("video_2d_file:http://171.244.10.137:13000", DIR_HOME)
                video_2d = line.replace("video_2d_file:http://210.245.90.204:13000", DIR_HOME)
                response['video_2d'] = video_2d
            # crop effect
            if line.startswith("crop_effect_status:"):
                response['crop_effect_status'] = line.replace("crop_effect_status:", "")
            if line.startswith("crop_effect:"):
                data = line.replace("crop_effect:", "")
                if data == 'dataX=&dataY=&dataWidth=&dataHeight=&dataScaleX=&dataScaleY=':
                    response['crop_effect_status'] = 0
                else:
                    response['crop_effect'] = {
                        "dataX": data.split("&")[0].split("=")[-1],
                        "dataY": data.split("&")[1].split("=")[-1],
                        "dataWidth": data.split("&")[2].split("=")[-1],
                        "dataHeight": data.split("&")[3].split("=")[-1],
                        "dataScaleX": data.split("&")[4].split("=")[-1],
                        "dataScaleY": data.split("&")[5].split("=")[-1],
                    }
            if line.startswith("scene_change_file:"):
                response['sceneChange'] = line.replace("scene_change_file:", DIR_HOME)
            if line.startswith("frames:"):
                response['frame'] = line.replace("frames:", "")
            if line.startswith("logo:"):
                full_line = line.replace("logo:", DIR_HOME)
                logo = {"path": str(full_line).split("&&position=")[0],
                        "position": str(full_line).split("&&position=")[-1]}
                response['arr_logo'].append(logo)
    return response
        
        
if __name__ == '__main__':
    config_data()