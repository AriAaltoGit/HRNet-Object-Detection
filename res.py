import pandas as pd
object = pd.read_pickle(r'../data_drive/HRNet-drone/result.pkl')
print(object)


# python tools/train.py configs/pascal_voc/faster_rcnn_r50_fpn_1x_voc_drone.py --work_dir drone
# python tools/test.py configs/pascal_voc/faster_rcnn_r50_fpn_1x_voc_drone.py drone/latest.pth --out drone/result.pkl

# python tools/train.py configs/pascal_voc/faster_rcnn_r50_fpn_1x_voc_drone.py --work_dir ../data_drive/HRNet-drone
