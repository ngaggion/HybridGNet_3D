import os 
from utils.file_utils import load_folder
import pandas as pd
import SimpleITK as sitk
from utils.segmentationMetrics import HD, MCD
from medpy.metric import dc
import numpy as np

def evaluate_model(models_path):
    faces = np.load("../Dataset/SurfaceFiles/faces_fhm_numpy.npy")
    subs = np.loadtxt("../Dataset/SurfaceFiles/subparts_fhm.txt", dtype=str)
    
    models = load_folder(models_path)
    
    for model_path in models:
        print("Evaluating model", model_path.split("/")[-1])
        
        dataframe = pd.DataFrame(columns=["ID",  
                            "LV Myo - DC", "LV Myo - HD", "LV Myo - MCD",
                            "LV Endo - DC", "LV Endo - HD", "LV Endo - MCD",
                            "RV Endo - DC", "RV Endo - HD", "RV Endo - MCD"])
        
        i = 0
        masks_path = os.path.join(model_path, "Masks")
        subjects = load_folder(masks_path)
        
        for subject in subjects:
            print('\r', 'Subject', i + 1, 'of', len(subjects), end='')
            
            timesteps = load_folder(subject)
            for time in timesteps:
                mask_path = os.path.join(time, "mask.nii.gz")
                mask_seg = sitk.GetArrayFromImage(sitk.ReadImage(mask_path))
                
                gt_path = os.path.join("../Dataset/Subjects", subject.split('/')[-1], "mesh", time.split('/')[-1], "lv_rv_mask.nii.gz")
                gt = sitk.GetArrayFromImage(sitk.ReadImage(gt_path))
                
                dice_myo = dc(gt == 250, mask_seg == 250)
                hausdorff_myo = HD(gt == 250, mask_seg == 250)
                assd_value_myo = MCD(gt == 250, mask_seg == 250)
                
                dice_Endo = dc(gt == 50, mask_seg == 50)
                hausdorff_Endo = HD(gt == 50, mask_seg == 50)
                assd_value_Endo = MCD(gt == 50, mask_seg == 50)

                dice_rv_Endo = dc(gt == 100, mask_seg == 100)
                hausdorff_rv_Endo = HD(gt == 100, mask_seg == 100)
                assd_value_rv_Endo = MCD(gt == 100, mask_seg == 100)
                
                dataframe.loc[i] = [subject.split('/')[-1], 
                    dice_myo, hausdorff_myo, assd_value_myo, 
                    dice_Endo, hausdorff_Endo, assd_value_Endo, 
                    dice_rv_Endo, hausdorff_rv_Endo, assd_value_rv_Endo]
                
            i += 1
        
        print("")
        dataframe.to_csv(os.path.join(model_path, "metrics.csv"), index=False)

if __name__ == "__main__":
    models_path = "../Predictions/Surface/"
    evaluate_model(models_path)