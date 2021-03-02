from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Rfq,Component,Consumable,Part


class Componentserializer(serializers.ModelSerializer):
    number=serializers.SerializerMethodField()
    component_name=serializers.SerializerMethodField()
    description=serializers.SerializerMethodField()
    quantity=serializers.SerializerMethodField()
    manufacturer=serializers.SerializerMethodField()



    def get_number(self,data):
        if data.component_type=='P':
            return Part.objects.get(component_id=data).part_number
        else:
            return Consumable.objects.get(component_id=data).part_number

    def get_component_name(self,data):
        if data.component_type=='P':
            return Part.objects.get(component_id=data).part_name
        else:
            return Consumable.objects.get(component_id=data).consumable_name

    def get_description(self,data):
        if data.component_type=='P':
            return Part.objects.get(component_id=data).description
        else:
            return Consumable.objects.get(component_id=data).description

    def get_quantity(self,data):
        if data.component_type=='P':
            return Part.objects.get(component_id=data).quantity
        else:
            return Consumable.objects.get(component_id=data).quantity

    def get_manufacturer(self,data):
        if data.component_type=='P':
            return Part.objects.get(component_id=data).manufacturer
        else:
            return Consumable.objects.get(component_id=data).manufacturer

    

    class Meta:
        model=Component
        fields=['component_id','component_type','number','component_name','description','quantity','manufacturer',]




class Listofrfqserializer(serializers.ModelSerializer):
    component_set= Componentserializer(many=True) 
    #Componentserializer(Component.objects.all().filter(rfq_id=data,many=True)

    '''def get_components(self,data):
        return Componentserializer(Component.objects.all().filter(rfq_id=data),many=True)'''


    class Meta:
        model=Rfq
        fields=['rfq_id','create_date','deadline','targetdate','description',
        'attachment','rfq_reach','preference','component_set',]

