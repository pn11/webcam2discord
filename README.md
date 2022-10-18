# webcam-monitor

定期的に webcam で撮影して Discord に送る。

## 環境構築

Python の OpenCV を使う。 OpenCV のインストールは pip でやるとめんどうなので miniconda を使うのが良い。 (Python のバージョンは適宜)

```sh
conda create -n webcam2discord
conda activate webcam2discord
conda install opencv
pip install python-dotenv requests
```

## 使い方

1. `.env` に Discord の Webhook の URL を書く。
1. `python webcam2discord.py --interval 30` (インターバルは分単位で、webcam をキャプチャーして Discord に送る)  
   webcam が複数台ある場合は `vc = cv2.VideoCapture(1)` の部分を適宜変える
1. `python webcam2discord.py --interval 30 --use_poisson` すると平均30分のポワソン分布になる
