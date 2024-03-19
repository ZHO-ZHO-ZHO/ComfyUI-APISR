import torch
import os
import folder_paths
import numpy as np
from PIL import Image

from .test_code.test_utils import load_grl, load_rrdb, load_cunet


device = "cuda" if torch.cuda.is_available() else "cpu"
folder_paths.folder_names_and_paths["apisr"] = ([os.path.join(folder_paths.models_dir, "apisr")], folder_paths.supported_pt_extensions)


def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


class APISR_ModelLoader_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "apisr_model": (folder_paths.get_filename_list("apisr"), ),
            }
        }

    RETURN_TYPES = ("APISRMODEL",)
    RETURN_NAMES = ("pipe",)
    FUNCTION = "load_model"
    CATEGORY = "🔎APISR"
  
    def load_model(self, apisr_model):
        if not apisr_model:
            raise ValueError("Please provide the apisr_model parameter with the name of the model file.")

        apisr_path = folder_paths.get_full_path("apisr", apisr_model)
      
        if apisr_model == "4x_APISR_GRL_GAN_generator.pth":
            generator = load_grl(apisr_path, scale=4)
        elif apisr_model == "2x_APISR_RRDB_GAN_generator.pth":
            generator = load_rrdb(apisr_path, scale=2)
        else:
            raise gr.Error(error)
      
        return [generator]


class APISR_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pipe": ("APISRMODEL",),
                "image": ("IMAGE",),
                "crop_for_4x": ("BOOLEAN", {"default": True}),
                "dtype": (["float32", "float16"], ),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "sr_image"
    CATEGORY = "🔎APISR"
                       
    def sr_image(self, pipe, image, crop_for_4x, dtype):
        if dtype == "float32":
            weight_dtype = torch.float32
        elif dtype == "float16":
            weight_dtype = torch.float16
        
        pipe = pipe.to(device=device, dtype=weight_dtype)
        
        img_tensor = image.permute(0, 3, 1, 2).to(device=device, dtype=weight_dtype)
        
        if crop_for_4x:
            _, _, h, w = img_tensor.shape
            if h % 4 != 0:
                img_tensor = img_tensor[:, :, :4 * (h // 4), :]
            if w % 4 != 0:
                img_tensor = img_tensor[:, :, :, :4 * (w // 4)]
      
        super_resolved_img = pipe(img_tensor)

        super_resolved_img_nhwc = super_resolved_img.permute(0, 2, 3, 1)

        return (super_resolved_img_nhwc,)


class APISR_Lterative_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pipe": ("APISRMODEL",),
                "image": ("IMAGE",),
                "crop_for_4x": ("BOOLEAN", {"default": True}),
                "dtype": (["float32", "float16"], ),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "sr_image"
    CATEGORY = "🔎APISR"
                       
    def sr_image(self, pipe, image, crop_for_4x, dtype):
        if dtype == "float32":
            weight_dtype = torch.float32
        elif dtype == "float16":
            weight_dtype = torch.float16
        
        pipe = pipe.to(device=device, dtype=weight_dtype)

        processed_images = []
        for img_tensor in image: 
            img_tensor = img_tensor.to(device=device, dtype=weight_dtype).unsqueeze(0).permute(0, 3, 1, 2)
        
            if crop_for_4x:
                _, _, h, w = img_tensor.shape
                if h % 4 != 0:
                    img_tensor = img_tensor[:, :, :4 * (h // 4), :]
                if w % 4 != 0:
                    img_tensor = img_tensor[:, :, :, :4 * (w // 4)]
                    
            with torch.no_grad():  # 确保在推理时不计算梯度，节省内存
                super_resolved_img = pipe(img_tensor)

            super_resolved_img_nhwc = super_resolved_img.permute(0, 2, 3, 1).squeeze(0)
            
            processed_images.append(super_resolved_img_nhwc)
            
        return (processed_images,)


NODE_CLASS_MAPPINGS = {
    "APISR_ModelLoader_Zho": APISR_ModelLoader_Zho,
    "APISR_Zho": APISR_Zho,
    "APISR_Lterative_Zho": APISR_Lterative_Zho
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "APISR_ModelLoader_Zho": "🔎APISR ModelLoader",
    "APISR_Zho": "🔎APISR",
    "APISR_Lterative_Zho": "🔎APISR Lterative",
}
