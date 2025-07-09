import os
import shutil
from datetime import datetime

"""
---

**Step 1: Data Organization**

The dataset was first organized into the following diagnostic groups:

* **CN** (Cognitively Normal)
* **MCI** ( Mild Cognitive Impairment)
* **AD** (Alzheimer’s Disease)
---

 Image Selection Criteria

 For the AD and CN groups:

* We retained only the images with the following preprocessing pipeline:
  `MPR-R__GradWarp__B1_Correction__N3__Scaled` or
  `MPR__GradWarp__B1_Correction__N3__Scaled`.

* Images labeled with `*_scaled_2*` were removed.
  These images were adjusted to disable scaling on axes where the phantom's measurements are considered unreliable.
  While `*_scaled_2*` images may offer higher accuracy, they are significantly fewer in number and **cannot be mixed** with the standard `*_scaled*` images for model training due to consistency issues.

---

 For the MCI

* Due to the limited availability of subjects in these groups, we included:

  * `MPR-R__GradWarp__B1_Correction__N3__Scaled`
  * `MPR__GradWarp__B1_Correction__N3__Scaled`
  * `MPR__GradWarp__N3__Scaled`

* Subjects with only `MPR__GradWarp__N3__Scaled` images will undergo additional preprocessing, specifically:

  *Bias field correction, to reduce intensity non-uniformity and improve image quality before training.


 """

def delete_scaled_2_folders_in_group(parent_folder_path, group_name):
    """
    Deletes all folders ending with 'Scaled_2' inside subject folders within a given group folder on the local filesystem.

    Args:
        parent_folder_path (str): Full path to the parent folder that contains group folders (e.g., 'AD', 'CN').
        group_name (str): Name of the group folder to process (e.g., 'AD').

    This function iterates through each subject folder under the specified group and deletes any
    subfolder whose name ends with 'Scaled_2'.
    """
    group_path = os.path.join(parent_folder_path, group_name)
    if not os.path.isdir(group_path):
        print(f" Group folder not found: {group_path}")
        return

    print(f"\n Processing group: {group_name}")

    # Loop over subject folders
    for subject in os.listdir(group_path):
        subject_path = os.path.join(group_path, subject)
        if not os.path.isdir(subject_path):
            continue

        print(f" Checking subject: {subject}")

        # Loop over subfolders inside subject folder
        for folder in os.listdir(subject_path):
            folder_path = os.path.join(subject_path, folder)
            if os.path.isdir(folder_path) and folder.endswith("Scaled_2"):
                print(f"🗑️ Deleting folder: {folder} in subject {subject}")
                shutil.rmtree(folder_path)


def clean_mpr_vs_mprr(root_dir):
    """
    For each subject folder in the given root directory, find MPR__ and MPR-R__ folders.
    Keep the one with more files, and delete the other.
    """
    for subject_name in os.listdir(root_dir):
        subject_path = os.path.join(root_dir, subject_name)
        if not os.path.isdir(subject_path):
            continue

        print(f"\nChecking subject: {subject_name}")

        mpr_folder = None
        mprr_folder = None
        mpr_count = 0
        mprr_count = 0

        for subfolder in os.listdir(subject_path):
            subfolder_path = os.path.join(subject_path, subfolder)
            if not os.path.isdir(subfolder_path):
                continue

            if subfolder.startswith("MPR__") and not subfolder.startswith("MPR-R__"):
                mpr_folder = subfolder_path
                mpr_count = len(os.listdir(subfolder_path))

            elif subfolder.startswith("MPR-R__"):
                mprr_folder = subfolder_path
                mprr_count = len(os.listdir(subfolder_path))

        if mpr_folder and mprr_folder:
            print(f" MPR: {mpr_count} files, MPR-R: {mprr_count} files")

            if mprr_count >= mpr_count:
                print(" Deleting MPR")
                shutil.rmtree(mpr_folder)
            else:
                print(" Deleting MPR-R")
                shutil.rmtree(mprr_folder)
        else:
            print(" One or both MPR versions not found.")
            
def clean_subjects_with_mpr(root_dirs):
    keep_folders = {
        "MPR__GradWarp__B1_Correction__N3__Scaled",
        "MPR-R__GradWarp__B1_Correction__N3__Scaled"
    }

    for root_dir in root_dirs:
        print(f"\n Scanning root directory: {root_dir}")
        for subject_id in os.listdir(root_dir):
            subject_path = os.path.join(root_dir, subject_id)
            if not os.path.isdir(subject_path):
                continue

            # Check if the subject contains any of the desired folders
            subfolders = os.listdir(subject_path)
            has_valid_mpr = any(folder in keep_folders for folder in subfolders)

            if not has_valid_mpr:
                print(f" Deleting subject (no valid MPR): {subject_path}")
                shutil.rmtree(subject_path)
            else:
                print(f" Keeping subject: {subject_path}")



def process_subjects_for_mpr(root_dirs):
    """
    now for the MCI groups we will keep the MPR-R/MPR__GradWarp__B1_Correction__N3__Scaled
    and the  MPR__GradWarp__N3__Scaled we be saved in a new subfolder to be bias corrected later

   """
    keep_folders = {
        "MPR__GradWarp__B1_Correction__N3__Scaled",
        "MPR-R__GradWarp__B1_Correction__N3__Scaled"
    }
    preprocess_folder = "NeedsPreprocessing"
    n3_folder = "MPR__GradWarp__N3__Scaled"

    for root_dir in root_dirs:
        print(f"\n Processing root: {root_dir}")
        for subject_id in os.listdir(root_dir):
            subject_path = os.path.join(root_dir, subject_id)
            if not os.path.isdir(subject_path):
                continue

            subfolders = os.listdir(subject_path)
            has_b1 = any(folder in keep_folders for folder in subfolders)
            has_n3 = n3_folder in subfolders

            if has_b1:
                print(f" Keeping subject with B1: {subject_path}")
                continue

            elif has_n3:
                print(f" Subject with N3 only: {subject_path}")
                # Create NeedsPreprocessing folder if not exists
                preprocess_path = os.path.join(subject_path, preprocess_folder)
                os.makedirs(preprocess_path, exist_ok=True)

                old_n3_path = os.path.join(subject_path, n3_folder)
                new_n3_path = os.path.join(preprocess_path, n3_folder)

                # Move N3 folder to NeedsPreprocessing
                shutil.move(old_n3_path, new_n3_path)
                print(f" Moved {n3_folder} to {preprocess_folder}")

                # Delete any other irrelevant folders
                for folder in subfolders:
                    if folder != preprocess_folder and folder != n3_folder:
                        folder_path = os.path.join(subject_path, folder)
                        if os.path.isdir(folder_path):
                            print(f"🗑️ Deleting other folder: {folder_path}")
                            shutil.rmtree(folder_path)

            else:
                print(f" No valid MPR found. Deleting subject: {subject_path}")
                shutil.rmtree(subject_path)


def organize_timepoints(source_root, destination_root):
    """
    Traverses subject MRI folders and organizes timepoint subfolders by datetime.
    
    Args:
        source_root (str): Path to root folder containing groups (e.g., AD, CN, MCI).
        destination_root (str): Path to write organized timepoints (e.g., timepoint_1, timepoint_2).
    """
    input_groups = [g for g in os.listdir(source_root) if os.path.isdir(os.path.join(source_root, g))]

    for group in input_groups:
        group_path = os.path.join(source_root, group)
        subjects = [s for s in os.listdir(group_path) if os.path.isdir(os.path.join(group_path, s))]

        for subject in subjects:
            subject_path = os.path.join(group_path, subject)

            # Look for scan types like MPR__ or MPR-R__
            for scan_type in os.listdir(subject_path):
                scan_path = os.path.join(subject_path, scan_type)
                if not os.path.isdir(scan_path):
                    continue

                # Collect timepoint folders and sort by datetime
                time_folders = []
                for time_folder in os.listdir(scan_path):
                    try:
                        time_obj = datetime.strptime(time_folder, "%Y-%m-%d_%H_%M_%S.0")
                        full_path = os.path.join(scan_path, time_folder)
                        time_folders.append((time_obj, full_path))
                    except ValueError:
                        continue  # Skip malformed time folders

                # Sort by date
                time_folders.sort()

                # Copy to new organized folder
                for idx, (dt, full_path) in enumerate(time_folders, start=1):
                    new_folder = os.path.join(destination_root, group, subject, f"timepoint_{idx}")
                    os.makedirs(new_folder, exist_ok=True)

                    for root, _, files in os.walk(full_path):
                        for file in files:
                            src = os.path.join(root, file)
                            dst = os.path.join(new_folder, file)