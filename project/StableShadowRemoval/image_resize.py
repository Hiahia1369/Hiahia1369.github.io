from PIL import Image
import os

def resize_images_in_folder(input_folder, output_folder, target_size=(640, 480)):
    """
    将指定文件夹中的所有图片调整为 640x480，并保存到另一个文件夹。

    :param input_folder: 源图片文件夹
    :param output_folder: 目标文件夹（存储 resized 图片）
    :param target_size: 目标尺寸，默认 (640, 480)
    """
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 获取文件夹中的所有图片
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp")  # 支持的图片格式
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(image_extensions)]

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        try:
            with Image.open(input_path) as img:
                # 调整大小
                img_resized = img.resize(target_size, Image.ANTIALIAS)  # 保持较高质量
                img_resized.save(output_path)  # 保存到目标文件夹
                print(f"✅ Resized: {image_file} -> {output_path}")
        except Exception as e:
            print(f"❌ Failed to resize {image_file}: {e}")

# 使用示例
input_folder = "static\images\cross_istd+_srd\DeS3"   # 替换为你的源图片文件夹
output_folder = "static\images\cross_istd+_srd\DeS3_resize" # 替换为目标存储文件夹
resize_images_in_folder(input_folder, output_folder)
