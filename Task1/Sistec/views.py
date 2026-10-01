from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def About2(request):
    s="<h1>Hod-Nargis Gupta</h1>"
    return HttpResponse
def Information3(request):
    s="<h1>SISTec Bhopal (Sagar Institute of Science and Technology) is a leading private engineering and management college in Gandhi Nagar, Bhopal, established in 2007 under the Sagar Group of Institutions. It is AICTE-approved, NAAC-accredited, affiliated to RGPV (engineering) and Barkatullah University (management), and known for strong placements with top recruiters like Infosys, TCS, Deloitte, and Amazon</h1>"
    return HttpResponse(s)