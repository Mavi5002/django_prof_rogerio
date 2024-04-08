from rest_framework.views import APIView
from rest_framework.response import Response
from aluno.models import CadastroAluno
from aluno.serializers import CadastroAlunoSerializer
from django.http import Http404
from rest_framework import status

class AlunoView(APIView):
    def get(self,resquest):
        alunos = CadastroAluno.objects.all()
        serializer = CadastroAlunoSerializer(alunos, many = True)
        return Response(serializer.data,status = 200)
     
    def post(self,request):
        serializer = CadastroAlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors,status=400)


class DetalheAluno(APIView):
    def get_aluno(self,pk):
        try:
            return CadastroAluno.objects.get()
        except CadastroAluno.DoesNotExist:
            raise Http404

    
    def get(self,request,pk):
        aluno = self.get_aluno(pk)
        serializer = CadastroAlunoSerializer(aluno)
        return Response(serializer.data)
    
    def put(self,request,pk):
        aluno = self.get_aluno(pk)
        serializer = CadastroAlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        aluno = self.get_aluno(pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
