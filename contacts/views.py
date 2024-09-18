# contacts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})



# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Contact
# from .forms import ContactForm

# @login_required
# def contact_list(request):
#     contacts = Contact.objects.all()
#     return render(request, 'contacts/contact_list.html', {'contacts': contacts})

# @login_required
# def add_contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact_list')
#     else:
#         form = ContactForm()
#     return render(request, 'contacts/add_contact.html', {'form': form})

# @login_required
# def contact_detail(request, pk):
#     contact = Contact.objects.get(pk=pk)
#     return render(request, 'contacts/contact_detail.html', {'contact': contact})

# @login_required
# def edit_contact(request, pk):
#     contact = Contact.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ContactForm(request.POST, instance=contact)
#         if form.is_valid():
#             form.save()
#             return redirect('contact_list')
#     else:
#         form = ContactForm(instance=contact)
#     return render(request, 'contacts/edit_contact.html', {'form': form})

# @login_required
# def delete_contact(request, pk):
#     contact = Contact.objects.get(pk=pk)
#     contact.delete()
#     return redirect('contact_list')

# @login_required
# def search_contacts(request):
#     query = request.GET.get('q')
#     contacts = Contact.objects.filter(first_name__icontains=query) | Contact.objects.filter(email__icontains=query)
#     return render(request, 'contacts/contact_list.html', {'contacts': contacts})