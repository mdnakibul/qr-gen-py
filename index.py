import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

# Function to generate QR code
def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter some text or URL.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.thumbnail((250, 250))  # Resize for display

    # Display the QR code in the GUI
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    # Save the image to a temporary variable for saving later
    global generated_image
    generated_image = img

# Function to save the QR code as an image file
def save_qr():
    if generated_image is None:
        messagebox.showerror("Error", "No QR code generated to save!")
        return

    filepath = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if filepath:
        generated_image.save(filepath)
        messagebox.showinfo("Success", "QR Code saved successfully!")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")

# Input label and entry
label = tk.Label(root, text="Enter Text or URL:", font=("Helvetica", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), width=30)
entry.pack(pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", font=("Helvetica", 14), command=generate_qr)
generate_button.pack(pady=10)

# QR Code display
qr_label = tk.Label(root, bg="white", width=250, height=250)
qr_label.pack(pady=20)

# Save button
save_button = tk.Button(root, text="Save QR Code", font=("Helvetica", 14), command=save_qr)
save_button.pack(pady=10)

# Initialize a variable to store the generated QR image
generated_image = None

# Run the GUI
root.mainloop()
