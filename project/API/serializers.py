from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        # fields = '__all__'
        fields = ('id','name','address','location','tech_skills','experience')
        read_only_fields = ('id',)
