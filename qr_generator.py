import qrcode
from PIL import Image
import os
from qrcode.image.svg import SvgImage  # SVG seguro

def gerar_qrcode(url, formato):
    nome_padrao = "qr_code"
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    if formato == "png":
        img = qrcode.make(url)
        output_path = os.path.join(desktop_path, f"{nome_padrao}.png")
        img.save(output_path)
        return output_path
    
    elif formato == "jpeg":
        temp_path = os.path.join(desktop_path, f"{nome_padrao}_temp.png")
        img = qrcode.make(url)
        img.save(temp_path)

        final_path = os.path.join(desktop_path, f"{nome_padrao}.jpeg")
        Image.open(temp_path).convert("RGB").save(final_path, "JPEG")
        os.remove(temp_path)
        return final_path
    
    elif formato == "svg":
        img = qrcode.make(url, image_factory=SvgImage)
        output_path = os.path.join(desktop_path, f"{nome_padrao}.svg")
        img.save(output_path)
        return output_path
    
    else:
        raise ValueError("Formato inválido.")

def main():
    print("=== Gerador de QR Code ===")
    url = input("Cole aqui o link para o QR Code: ").strip()

    if not url.startswith("http"):
        print("❌ URL inválida! Certifique-se de colar um link que comece com 'http'.")
        return

    print("\nEscolha o formato da imagem do QR Code:")
    print("1 - PNG")
    print("2 - JPEG")
    print("3 - SVG")
    escolha = input("Digite o número da opção desejada: ").strip()

    formatos = {"1": "png", "2": "jpeg", "3": "svg"}
    formato = formatos.get(escolha)

    if not formato:
        print("❌ Opção inválida.")
        return

    caminho = gerar_qrcode(url, formato)
    print(f"\n✅ QR Code gerado com sucesso em formato {formato.upper()}!")
    print(f"📁 Arquivo salvo em: {caminho}")

if __name__ == "__main__":
    main()
