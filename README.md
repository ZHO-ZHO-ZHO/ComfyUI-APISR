

![APISR](https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR/assets/140084057/740def33-964b-47ab-a2f0-e3a11fcbbd1c)


# APISR IN COMFYUI

Unofficial implementation of [APISR](https://github.com/Kiteretsu77/APISR) for ComfyUI


https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR/assets/140084057/e6deb435-d276-4726-9d6d-457cc99d433e


## 项目介绍 | Info

- 对 [APISR](https://github.com/Kiteretsu77/APISR) 的非官方实现

- APISR：专门用于动漫的超分模型，包含 2x 和 4x 双模型，速度飞快，效果很好
  
- 版本：V1.0 同时支持图像和视频放大（视频分为Batch和Lterative两种方式，分别适用于高/低显存）

![Dingtalk_20240319200511](https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR/assets/140084057/a6aaccf9-01e6-4c79-a9bf-6beb830e572a)


## 节点说明 | Features

- APISR 模型加载 | 🔎APISR ModelLoader
    - 支持 2 种官方模型：[2x_APISR_RRDB_GAN_generator](https://huggingface.co/camenduru/APISR/resolve/main/2x_APISR_RRDB_GAN_generator.pth?download=true) 和 [4x_APISR_GRL_GAN_generator](https://huggingface.co/camenduru/APISR/resolve/main/4x_APISR_GRL_GAN_generator.pth?download=true)，需手动下载放入 `/ComfyUI/models/apisr` 中
    
- 放大（批） | 🔎APISR
    - 同时支持 图像 和 视频
    - 批处理，帧数多的视频需要高显存
    
- 放大（逐张）| 🔎APISR Lterative
    - 同时支持 图像 和 视频
    - 逐张处理，低显存推荐使用
    - 若输出配合 Video Helper Suite 插件使用，则需要使用 ComfyUI 自带的 Split Image with Alpha 节点去除 Alpha 通道
 
 ![Dingtalk_20240319202553](https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR/assets/140084057/5cc2c2fc-dc09-44e2-a363-831910f77172)


## 安装 | Install

- 推荐使用管理器 ComfyUI Manager 安装（On the Way）

- 手动安装：
    1. `cd custom_nodes`
    2. `git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR`
    3. `cd custom_nodes/ComfyUI-APISR`
    4. `pip install -r requirements.txt`
    5. 重启 ComfyUI


## 工作流 | Workflows

V1.0

  - [V1.0 APISR img or video Batch](https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR/blob/main/APISR%20WORKFLOWS/APISR%20img%20or%20video%20Batch%E3%80%90Zho%E3%80%91.json)

    ![Dingtalk_20240319195936](https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR/assets/140084057/2dc21ac0-6ca4-45a6-8009-29f0eece7426)

  - [V1.0 APISR img or video Lterative](https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR/blob/main/APISR%20WORKFLOWS/APISR%20img%20or%20video%20Lterative%E3%80%90Zho%E3%80%91.json)
    
    ![Dingtalk_20240319203321](https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR/assets/140084057/9ebc1153-2d68-4fa2-b24a-b7bb8ebe437a)


## 更新日志

- 20240319

  创建项目

  V1.0 同时支持图像与视频的放大，还提供分别适合于高显存和低显存的 Batch 和 Lterative 两种模式


## Stars 

[![Star History Chart](https://api.star-history.com/svg?repos=ZHO-ZHO-ZHO/ComfyUI-APISR&type=Date)](https://star-history.com/#ZHO-ZHO-ZHO/ComfyUI-APISR&Date)


## Credits

[APISR](https://github.com/Kiteretsu77/APISR)




