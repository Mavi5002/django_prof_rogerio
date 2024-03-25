from rest_framework.views import APIView
from rest_framework.response import Response
from cadastro.models import Aluno
from cadastro.serializers import AlunoSerializer
from django.http import Http404
from rest_framework import status


class AlunoView(APIView):
    def get_aluno(self,pk,usuario):
        try:
            return Aluno.objects.get(pk=pk,usuario=usuario)
        except Aluno.DoesNotExist:
            raise Http404


    def get(self,resquest):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many = True)
        return Response(serializer.data,status = 200)
    
    def post(self,request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors,status=400)
    
    def put(self,request,pk):
        aluno = self.get_aluno(pk,request.user)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        aluno = self.get_aluno(pk,request.user)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
