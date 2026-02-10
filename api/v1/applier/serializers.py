from rest_framework import serializers
from web.models import Job,Apply

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields=["id","title","company_name","job_type","salary","location",]

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model=Apply
        fields=["id","applier","job","applied_at","cv"]
        extra_kwargs = {
            "applier": {"read_only": True},
            "applied_at": {"read_only": True},
        }