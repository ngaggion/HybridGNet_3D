# HybridVNet: Multi-view Hybrid Graph Convolutional Network for Volume-to-mesh Reconstruction in Cardiovascular MRI

This repository contains the implementation of HybridVNet, a novel architecture for generating high-quality surface and volumetric meshes directly from Cardiovascular Magnetic Resonance (CMR) images, as described in our paper "Multi-view Hybrid Graph Convolutional Network for Volume-to-mesh Reconstruction in Cardiovascular MRI".

## Features

- Direct volume-to-mesh reconstruction from CMR images
- Multiview integration of Short Axis (SAX) and Long Axis (LAX) CMR views
- Generation of both surface and tetrahedral meshes
- Novel differentiable regularization term for tetrahedral meshes

### Dependencies

Main dependencies include:
- PyTorch
- PyTorch Geometric
- PyTorch3D (only required for training, for the surface mesh losses)
- psbody (only required to generate downsampling and upsampling matrices)
- NumPy
- Matplotlib
- SimpleITK

Training models with soon be available.

## Inference

We provide pre-trained weights for two model variants:
1. Complete short-axis image model
2. Multi-view long axis model

You can download the weights from our [Hugging Face repository](https://huggingface.co/datasets/ngaggion/HybridVNet_Weights/tree/main).

### Input Image Sizes

- Short-axis images: (210, 210, 16)
- Long-axis images (2CH, 3CH, 4CH): (224, 224, 1) each

Note: If you don't have the 3CH long-axis image, you can use an empty image as input.

### Docker Image

We offer a Docker image with pre-downloaded weights for easy setup:

1. Pull the Docker image:
   ```bash
   docker pull ngaggion/hybridvnet:latest
   ```

2. Run the Docker container:
   ```bash
   MOUNT="YOUR_LOCAL_INFORMATION_PATH"
   docker run -it --gpus all -v $MOUNT:/DATA/ hybrivnet:latest
   ```

3. (Optional) Update the repository:
   ```bash
   git pull
   ```

#### Docker Requirements

To use GPU support, install the `nvidia-docker2` package. For Ubuntu-based distributions:

```bash
# Add GPG key
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg

# Add repository
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
echo "deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://nvidia.github.io/nvidia-docker/$distribution/$(arch)/" | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# Update and install
sudo apt-get update
sudo apt-get install -y nvidia-docker2
```

Note: We use CUDA 11.8. If your GPU has different requirements, you may need to build your own image by modifying the Dockerfile.

### Example Files

We provide example files to help structure your dataset and inference pipeline:
- `utils/dataset_inference_w_LAX_example.py`
- `inference_example.py`

These files demonstrate how to set up your data and run inference using HybridVNet.

## Citation

If you use this code in your research, please cite our paper:

```
@article{GAGGION2025103630,
title = {Multi-view hybrid graph convolutional network for volume-to-mesh reconstruction in cardiovascular MRI},
journal = {Medical Image Analysis},
volume = {104},
pages = {103630},
year = {2025},
issn = {1361-8415},
doi = {https://doi.org/10.1016/j.media.2025.103630},
url = {https://www.sciencedirect.com/science/article/pii/S136184152500177X},
author = {Nicolás Gaggion and Benjamin A. Matheson and Yan Xia and Rodrigo Bonazzola and Nishant Ravikumar and Zeike A. Taylor and Diego H. Milone and Alejandro F. Frangi and Enzo Ferrante},
keywords = {Cardiac imaging, Geometric deep learning, Hybrid graph convolutional neural network, Volume-to-mesh},
}
```

## Contributing

We welcome contributions to improve HybridVNet. Please feel free to submit issues and pull requests.
