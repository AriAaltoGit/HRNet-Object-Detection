import pandas as pd
object = pd.read_pickle(r'drone/result.pkl')
object


# python tools/train.py configs/pascal_voc/faster_rcnn_r50_fpn_1x_voc_drone.py --work_dir drone
# python tools/test.py configs/pascal_voc/faster_rcnn_r50_fpn_1x_voc_drone.py drone/latest.pth --out drone/result.pkl
