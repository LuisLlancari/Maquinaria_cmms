from django.shortcuts import render, redirect, get_object_or_404
from ..models import Tractorista
from ..forms import TractoristaForms
from usuario.models import Persona, Usuario
from usuario.forms import PersonaForm
from django.http import JsonResponse

#Manejo de errores
from django.contrib import messages

def tractoristas(request):
  datos_tractoristas = Tractorista.objects.filter(estado = True)
  datos_usuarios = Usuario.objects.filter(idrol = 3)
  return render(request, 'operarios/tractoristas.html', {'datos_tractoristas':datos_tractoristas, 'form':PersonaForm, 'datos_usuarios':datos_usuarios })

def registrarTractorista(request):
  datos_tractoristas = Tractorista.objects.filter(estado = True)



  if request.method == 'POST':
    id_usuario = request.POST.get('usuario')

    persona_form = PersonaForm(request.POST)
    dni = request.POST.get('dni').strip()
    persona_existe = Persona.objects.filter(dni = dni, estado = True).exists()
    if persona_form.is_valid() and persona_existe == False:
      persona_form.save()

      ultimo_registro = Persona.objects.latest('idpersona')
      id_persona = ultimo_registro.idpersona

      persona = Persona.objects.get(pk=id_persona)
      usuario = Usuario.objects.get(pk=id_usuario)

      Tractorista.objects.create(idusuario = usuario , idpersona = persona)

      messages.success(request, 'Tractorista registrado con exito', extra_tags='success')
      return redirect('tractorista')
  else:
     messages.error(request, 'El tractorista ya existe', extra_tags='danger')
     return render(request, 'operarios/tractoristas.html', {'datos_tractoristas': datos_tractoristas})

def eliminarTractorista(request, id_tractorista):
  registro = get_object_or_404(Tractorista, pk= id_tractorista)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('tractorista')

def editarTractoristas(request, id_tractorista):
  if request.method == 'POST':
    # Obtenemos el valor de usuario acargo
    id_usuario = request.POST.get('usuario')

    # Obtenemos el valor de la idpersona realacionada a el tractorista
    registro_tractorista = Tractorista.objects.filter(pk= id_tractorista).values('idpersona').first()
    id_persona = registro_tractorista['idpersona']

    # Buscamos a la persona por el id y lo instaciamos en formulario 
    persona = get_object_or_404(Persona, pk = id_persona)
    form_persona = PersonaForm(request.POST, instance=persona)

    # Validamos y actualizamos
    if form_persona.is_valid():
      form_persona.save()
      Tractorista.objects.filter(pk = id_tractorista).update(idusuario = id_usuario)
      messages.success(request, 'Tractorista actualizado con exito', extra_tags='success')
      return redirect('tractorista')
    else:
      messages.error(request, 'El tractorista ya existe', extra_tags='danger')
      return redirect('tractorista')
    
  else:
    return redirect('tractorista')

def obtenerDatos(request, id_tractorista):
  # Obtenmos los datos del tractorista por el id
  tractorista = list(Tractorista.objects.filter(pk=id_tractorista).values())

  # Obtenemos el id de la persona relacionada al tractorista
  primer_valor = tractorista[0]
  id_persona = primer_valor['idpersona_id']

  # Obtenemos el datos de la persona por el id
  persona = list(Persona.objects.filter(pk=id_persona).values())

  if(len(tractorista) > 0):
    data = {'mensaje': "Success", 'tractorista': tractorista, 'persona':persona }
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)