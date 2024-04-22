from django.shortcuts import render, redirect, get_object_or_404
from ..models import Solicitante , TipoSolicitante
from usuario.forms import PersonaForm
from usuario.models import Persona
from ..forms import SolicitanteForms
from django.http import JsonResponse

def solicitante(request):
  datos_solicitantes = Solicitante.objects.filter(estado=True)
  datos_tiposolicitante = TipoSolicitante.objects.filter(estado=True)
  return render(request, 'operarios/solicitante.html', {'datos_solicitantes': datos_solicitantes, 'form':PersonaForm, 'datos_tiposolicitante':datos_tiposolicitante})

def registrarSolicitante(request):
  if request.method == 'POST':
      tipo_solicitante = request.POST.get('tiposolicitante')
      persona_form = PersonaForm(request.POST)
      if persona_form.is_valid():
        persona_form.save()

        ultimo_registro = Persona.objects.latest('idpersona')
        id_persona = ultimo_registro.idpersona

        persona = Persona.objects.get(pk=id_persona)
        tipo_solicitante = TipoSolicitante.objects.get(pk=tipo_solicitante)


        Solicitante.objects.create(idtiposolicitante = tipo_solicitante , idpersona = persona)
      return redirect('solicitante')
  else:
      return redirect('solicitante')


def eliminarSolicitante(request, id_solicitante):
  registro = get_object_or_404(Solicitante, pk= id_solicitante)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('solicitante')
  
def editarSolicitante(request, id_solicitante):
  if request.method == 'POST':
    # Obtenemos el valor del tipo solicitante
    id_tiposolicitante = request.POST.get('tiposolicitante')

    # Obtenemos el valor de la idpersona realacionada a el solicitante
    registro_solicitante = Solicitante.objects.filter(pk= id_solicitante).values('idpersona').first()
    id_persona = registro_solicitante['idpersona']

    # Buscamos a la persona por el id y lo instaciamos en formulario 
    persona = get_object_or_404(Persona, pk = id_persona)
    form_persona = PersonaForm(request.POST, instance=persona)

    # Validamos y actualizamos
    if form_persona.is_valid():
      form_persona.save()
      Solicitante.objects.filter(pk = id_solicitante).update(idtiposolicitante = id_tiposolicitante)

      return redirect('solicitante')
  else: 
    return redirect('solicitante')

def obtenerDatos(request, id_solicitante):
  # Obtenemos el solicitante por el id
  solicitante = list(Solicitante.objects.filter(pk=id_solicitante).values())

  # Obtenemos el id de la persona ligada a solicitante
  primer_valor = solicitante[0]
  id_persona = primer_valor['idpersona_id']

  # Obtenemos datos de la persona por el id
  persona = list(Persona.objects.filter(pk=id_persona).values())

  if(len(solicitante) > 0):
    data = {'mensaje': "Success", 'solicitante': solicitante, 'persona':persona }
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)