fd = r"C:\Users\Abhijit_asus\OneDrive\Desktop\sanskrit_files\विष्णुबलि.pdf"


from pdfreader import PDFDocument, SimplePDFViewer
from PIL import Image
from io import BytesIO

def extract_first_page_image(pdf_file):
    print('eneterd ')
    with open(pdf_file, "rb") as file:
        viewer = SimplePDFViewer(file)
        viewer.render()
        
        # Extract images from the first page
        images = viewer.canvas.images
        print("yikes")
        if images:
            image_key = list(images.keys())[0]
            image_data = images[image_key]
            print("djfjsd")
            if image_data:
                print(type(image_data))
                image_bytes = BytesIO(image_data)
                print("dsjkf")
                pil_image = Image.open(image_bytes)
                print("sg")
                pil_image.show()  # Display the image
            else:
                print("Image data is None.")
        else:
            print("No images found on the first page.")



extract_first_page_image(fd)
