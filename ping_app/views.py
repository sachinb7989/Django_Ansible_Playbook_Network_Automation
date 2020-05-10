from django.shortcuts import render, HttpResponse
from ping_app.models import Devices
from ping_app.forms import MyForm
import subprocess, json
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    form = MyForm(request.POST)
    if form.is_valid():
        hostname = request.POST.get('hostname')
        Command = request.POST.get('Command')
    else:
        form = MyForm()
    return render(request, 'index.html', {'form': form})


def output(request):
    hostname = request.POST.get('hostname')
    command = request.POST.get('command')
    command2 = "\'"+command+"\'"
    print(hostname)
    print(command)
#    print('ansible-playbook', 'show.yaml', '--extra-var', '"hostname=' + hostname, 'command_input=\'' + command+'\'"')
#    query='ansible-playbook show.yaml --extra-var  "hostname=R1  command_input=\'show ip int bri\'"'
#    result = subprocess.Popen([query], stdout=subprocess.PIPE)
    result = subprocess.Popen(['ansible-playbook', 'show.yaml', '--extra-var', 'hostname=' + hostname, '--extra-var', 'command_input=' +  command2], stdout=subprocess.PIPE)
    out, err = result.communicate()
    print(out)
    return HttpResponse(out, content_type='application/json')
    # return JsonResponse(json.loads(output))
