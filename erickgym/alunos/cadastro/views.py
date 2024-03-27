from rest_framework.views import APIView
from rest_framework.response import Response
from alunos.models import Aluno
from alunos.serializers import AlunoSerializer
from django.http import Http404
from rest_framework import status


class AlunoView(APIView):
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


class DetalheAluno(APIView):
    def get_aluno(self,pk):
        try:
            return Aluno.objects.get()
        except Aluno.DoesNotExist:
            raise Http404

    
    def get(self,request,pk):
        aluno = self.get_aluno(pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)
    
    def put(self,request,pk):
        aluno = self.get_aluno(pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        aluno = self.get_aluno(pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

