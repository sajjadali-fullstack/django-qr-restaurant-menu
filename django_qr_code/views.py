from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings





def generate_qr_code(request):
    if request.method == 'POST':  # True
        form = QRCodeForm(request.POST)
        if form.is_valid():
            resturant_name = form.cleaned_data['resturant_name']
            url = form.cleaned_data['url']
            
            # For testing purpose
            print("="*30)
            print(f'Resturant Name: {resturant_name}\nURL: {url}')
            print("="*30)

            # Generate QR Code
            qr = qrcode.make(url)
            file_name = resturant_name.replace(" ", "_").lower() + "_menu.png"  # replace all the spaces into underscores
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)  # media/sajjad_ali_resturant_menu.png
            qr.save(file_path)
            # qr.save(f' Menu {resturant_name}.png')
            context = {
                'resturant_name':resturant_name
                }
            return render(request, 'qr_result.html', context)

    else:
        form = QRCodeForm()
        return render(request, 'generate_qr_code.html', {'form':form})

