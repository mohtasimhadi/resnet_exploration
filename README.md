# Exploring Deep Residual Learning for Image Recognition

This project implements ResNet models from scratch and trains them on CIFAR-10, MS COCO, and ImageNet datasets. The performance of the models is evaluated using classification accuracy, precision, recall, and F1-score.

## File Structure
```
project/
└──resnet
    ├── block_config.py
    ├── __init__.py
    ├── models.py
    └── train.py
└──utils
    ├── datasets.py
    ├── evaluations.py
    ├── urls.json
    └── helpers.py
└── main.py
├── downloader.py
├── README.md
├── .gitignore
├── project_report.pdf
└── requirements.txt

```


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mohtasimhadi/resnet_exploration.git
    cd resnet_exploration
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. Install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Downloading Datasets
**ImageNet**

If ImageNet dataset is not downloaded, use the following code to download and extract it.
```bash
python downloader.py imageNet
```

**MS COCO**

If MS COCO dataset is not downloaded, use the following code to download and extract it.
```bash
python downloader.py ms_coco
```

### Notes
- CIFAR10 dataset will be downloaded automatically during the training.
- If download fails due to url issues, the urls can be changed from `utils/urls.json`

## Running the Code

```bash
python main.py --dataset <dataset_name> --layers <num_layers> [--epochs <num_epochs>] [--batch_size <batch_size>]
```

### Arguments:
- **dataset:** Specify the dataset to use for training.

  *choices:* `CIFAR10`, `MSCOCO`, `ImageNet`
- **layers:** Number of layers in the ResNet model.
- **epochs:** Number of epochs to train the model (default: 10).
- **batch_size:** Batch size for training and validation (default: 16).

### Example Commands:
Train ResNet on CIFAR-10 with 50 layers for 20 epochs:
```bash
python main.py --dataset CIFAR10 --layers 50 --epochs 20 --batch_size 32
```
Train ResNet on ImageNet with 101 layers for 50 epochs:
```bash
python main.py --dataset ImageNet --layers 101 --epochs 50 --batch_size 64
```
### Notes:
- Adjust `--batch_size` according to your system's GPU memory capacity.


## References
```tex
@inproceedings{he2016deep,
  title={Deep Residual Learning for Image Recognition},
  author={He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2016}
}

@article{deng2009imagenet,
  title={ImageNet: A Large-Scale Hierarchical Image Database},
  author={Deng, Jia and Dong, Wei and Socher, Richard and Li, Li-Jia and Li, Kai and Fei-Fei, Li},
  journal={IEEE Computer Vision and Pattern Recognition},
  year={2009}
}

@techreport{cifar10,
  author = {Krizhevsky, Alex and Hinton, Geoffrey},
  title = {Learning Multiple Layers of Features from Tiny Images},
  institution = {University of Toronto},
  year = {2009},
  type = {Technical Report}
}

@inproceedings{lin2014microsoft,
  author = {Lin, Tsung-Yi and Maire, Michael and Belongie, Serge and Hays, James and Perona, Pietro and Ramanan, Deva and Doll{\'a}r, Piotr and Zitnick, C. Lawrence},
  title = {{Microsoft COCO}: Common Objects in Context},
  booktitle = {European Conference on Computer Vision (ECCV)},
  year = {2014}
}

```
