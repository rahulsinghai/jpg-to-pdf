# Jpg to PDF utility

Configure border and image quality (to restrict output PDF of a particular size) in the source code.

```shell
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python src/JpgToPdf.py <input_image_path> <output_pdf_path> <image_quality> <border_size>
deactivate
```

## Gitpod

With Gitpod, you spin up fresh, automated dev environments for each task, in the cloud, in seconds.

1. Commit your source code to Github/Gitlab/BitBucket.
2. Create a GitPod workspace by prefixing Repo URL by https://gitpod.io/#
3. `gp init`. This will auto-create a `.gitpod.yml` file by auto-detecting project type.
4. Run `python src/JpgToPdf.py <input_image_path> <output_pdf_path> <image_quality> <border_size>`. All 4 parameters are optional.
