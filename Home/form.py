from django import forms

class ContactForm(forms.Form):
    area_of_interest = forms.ChoiceField(
        choices=[('', '--None--'), ('sales', 'Sales'), ('support', 'Support')],
        required=True,
        label="Area of Interest",
        widget=forms.Select(attrs={"class": "block w-full outline-none py-2 px-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"})
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={"class": "block w-full outline-none py-2 px-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50", "placeholder": "Your email address"})
    )
    phone_number = forms.CharField(
        required=True,
        label="Phone Number",
        widget=forms.TextInput(attrs={"class": "block w-full outline-none py-2 px-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50", "placeholder": "Your phone number"})
    )
    first_name = forms.CharField(
        required=True,
        label="First Name",
        widget=forms.TextInput(attrs={"class": "block w-full outline-none py-2 px-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50", "placeholder": "Your first name"})
    )
    last_name = forms.CharField(
        required=True,
        label="Last Name",
        widget=forms.TextInput(attrs={"class": "block w-full outline-none py-2 px-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50", "placeholder": "Your last name"})
    )
    company = forms.CharField(
        required=False,
        label="Company",
        widget=forms.TextInput(attrs={"class": "block w-full outline-none py-2 px-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50", "placeholder": "Your company name"})
    )
    message = forms.CharField(
        required=True,
        label="Message",
        widget=forms.Textarea(attrs={"class": "block w-full outline-none py-2 px-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50", "placeholder": "Your message", "rows": 4})
    )
