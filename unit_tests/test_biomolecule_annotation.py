import unittest
from api_python_3decision import api
import json

class AnnotationTests(unittest.TestCase):
    
    annotationJson={"biomolecules": [{"general": {"biomoleculeCode": "HS90A_HUMAN"},"annotations": [{"value": {"AnnotationValueString": "test annotation"}}]}]}
    annotationJson2=json.loads("""
{
    "biomolecules": [
        {
            "general": {
                "biomoleculeCode": "HS90A_HUMAN"
            },
            "annotations": [
                {
                    "value": {
                        "AnnotationValueString": "test annotation"
                    },
                    "type": "User Annotation"
                }
            ],
            "sequences": [
                {
                    "sequence": "MPEETQTQDQPMEEEEVETFAFQAEIAQLMSLIINTFYSNKEIFLRELISNSSDALDKIRYESLTDPSKLDSGKELHINLIPNKQDRTLTIVDTGIGMTKADLINNLGTIAKSGTKAFMEALQAGADISMIGQFGVGFYSAYLVAEKVTVITKHNDDEQYAWESSAGGSFTVRTDTGEPMGRGTKVILHLKEDQTEYLEERRIKEIVKKHSQFIGYPITLFVEKERDKEVSDDEAEEKEDKEEEKEKEEKESEDKPEIEDVGSDEEEEKKDGDKKKKKKIKEKYIDQEELNKTKPIWTRNPDDITNEEYGEFYKSLTNDWEDHLAVKHFSVEGQLEFRALLFVPRRAPFDLFENRKKKNNIKLYVRRVFIMDNCEELIPEYLNFIRGVVDSEDLPLNISREMLQQSKILKVIRKNLVKKCLELFTELAEDKENYKKFYEQFSKNIKLGIHEDSQNRKKLSELLRYYTSASGDEMVSLKDYCTRMKENQKHIYYITGETKDQVANSAFVERLRKHGLEVIYMIEPIDEYCVQQLKEFEGKTLVSVTKEGLELPEDEEEKKKQEEKKTKFENLCKIMKDILEKKVEKVVVSNRLVTSPCCIVTSTYGWTANMERIMKAQALRDNSTMGYMAAKKHLEINPDHSIIETLRQKAEADKNDKSVKDLVILLYETALLSSGFSLEDPQTHANRIYRMIKLGLGIDEDDPTADDTSAAVTEEMPPLEGDDDTSRMEEVD",
                    "annotations": [
                        {
                            "value": {
                                "AnnotationValueString": "test annotation from sequence variant a"
                            },
                            "type": "User Annotation"
                        },
                        {
                            "value": {
                                "AnnotationValueString": "test second annotation from sequence variant a"
                            }
                        }
                    ]
                }
            ]
        }
    ]
}
    """)
    annotationJson3=json.loads("""
    {
"biomolecules": [
{
"general": {
"biomoleculeCode": "NOTTHEGOODONE"
},
"annotations": [
{
"value": {
"AnnotationValueString": "test annotation"
},
"type": "User Annotation"
}
],
"sequences": [
{
"sequence": "MPEETQTQDQPMEEEEVETFAFQAEIAQLMSLIINTFYSNKEIFLRELISNSSDALDKIRYESLTDPSKLDSGKELHINLIPNKQDRTLTIVDTGIGMTKADLINNLGTIAKSGTKAFMEALQAGADISMIGQFGVGFYSAYLVAEKVTVITKHNDDEQYAWESSAGGSFTVRTDTGEPMGRGTKVILHLKEDQTEYLEERRIKEIVKKHSQFIGYPITLFVEKERDKEVSDDEAEEKEDKEEEKEKEEKESEDKPEIEDVGSDEEEEKKDGDKKKKKKIKEKYIDQEELNKTKPIWTRNPDDITNEEYGEFYKSLTNDWEDHLAVKHFSVEGQLEFRALLFVPRRAPFDLFENRKKKNNIKLYVRRVFIMDNCEELIPEYLNFIRGVVDSEDLPLNISREMLQQSKILKVIRKNLVKKCLELFTELAEDKENYKKFYEQFSKNIKLGIHEDSQNRKKLSELLRYYTSASGDEMVSLKDYCTRMKENQKHIYYITGETKDQVANSAFVERLRKHGLEVIYMIEPIDEYCVQQLKEFEGKTLVSVTKEGLELPEDEEEKKKQEEKKTKFENLCKIMKDILEKKVEKVVVSNRLVTSPCCIVTSTYGWTANMERIMKAQALRDNSTMGYMAAKKHLEINPDHSIIETLRQKAEADKNDKSVKDLVILLYETALLSSGFSLEDPQTHANRIYRMIKLGLGIDEDDPTADDTSAAVTEEMPPLEGDDDTSRMEEVD",
"annotations": [
{
"value": {
"AnnotationValueString": "test annotation from sequence variant a"
},
"type": "User Annotation"
},
{
"value": {
"AnnotationValueString": "test second annotation from sequence variant a"
}
}
]
}
]
}
]
}

""")
    annotationJson4=json.loads("""
    {
    "biomolecules": [
        {
            "general": 
                {
                    "biomoleculeCode": "HS90A_HUMAN"
                },
            "annotations":[{"value": { "AnnotationValueString": "test annotation"}, "type":"User Annotation"}],
            "sequences":[
                {
                    "sequence":"MPEETQTQDQPMEEEEVETFAFQAEIAQLMSLIINTFYSNKEIFLRELISNSSDALDKIRYESLTDPSKLDSGKELHINLIPNKQDRTLTIVDTGIGMTKADLINNLGTIAKSGTKAFMEALQAGADISMIGQFGVGFYSAYLVAEKVTVITKHNDDEQYAWESSAGGSFTVRTDTGEPMGRGTKVILHLKEDQTEYLEERRIKEIVKKHSQFIGYPITLFVEKERDKEVSDDEAEEKEDKEEEKEKEEKESEDKPEIEDVGSDEEEEKKDGDKKKKKKIKEKYIDQEELNKTKPIWTRNPDDITNEEYGEFYKSLTNDWEDHLAVKHFSVEGQLEFRALLFVPRRAPFDLFENRKKKNNIKLYVRRVFIMDNCEELIPEYLNFIRGVVDSEDLPLNISREMLQQSKILKVIRKNLVKKCLELFTELAEDKENYKKFYEQFSKNIKLGIHEDSQNRKKLSELLRYYTSASGDEMVSLKDYCTRMKENQKHIYYITGETKDQVANSAFVERLRKHGLEVIYMIEPIDEYCVQQLKEFEGKTLVSVTKEGLELPEDEEEKKKQEEKKTKFENLCKIMKDILEKKVEKVVVSNRLVTSPCCIVTSTYGWTANMERIMKAQALRDNSTMGYMAAKKHLEINPDHSIIETLRQKAEADKNDKSVKDLVILLYETALLSSGFSLEDPQTHANRIYRMIKLGLGIDEDDPTADDTSAAVTEEMPPLEGDDDTSRMEEVD",
                    "annotations": [
                        {"value": { "AnnotationValueString": "test annotation from sequence variant a"}, "type":"User Annotation"}, 
                        {"value": { "AnnotationValueString": "test second annotation from sequence variant a"}} 
                        ],
                    "sequenceRegions":[
                        {
                            "label": "optional label if region is created",
                            "start":1,
                            "end":3,
                            "subsequence":"MPE",
                            "annotations":[
                                {
                                    "type":"User Annotation",
                                    "value":{ "AnnotationValueString":  "test annotation API : 3 first residues, seq variant a"},
                                    "group":"Serie 1324",
                                    "annotationData":[
                                        {"type": "Ki","label": "Inhibition DataBatch 1324230","value": { "number": 0.888,"unit":"M"},"description":"this is a description for a, annotation data on seq variant a"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "sequenceResidues":[
                        {
                            "code":"M",
                            "number":1,
                            "annotations":[
                                {"type":"Test 8", "group":"Serie 1324", "value":  { "AnnotationValueString": "test annotation API : first residue, seq variant a"}}
                            ]
                        },
                        {
                            "code":"E",
                            "number":3,
                            "annotations":[
                                {"type":"Test 8", "group":"Serie 1324", "value": { "AnnotationValueString": "test annotation API : third residue, seq variant a"}},
                                {"type":"User Annotation", "group":"Serie 1324", "value": { "AnnotationValueString": "test annotation API : third residue, seq variant a, second annot"}}
                            ]
                        }
                    ]
                },
                {
                    "sequence":"MPEETQTQDQPMEEEEVETFAFQAEIAQLMSLIINTFYSNKEIFLRELISNSSDALDKIRYESLTDPSKLDSGKELHINLIPNKQDRTLTIVDTGIGMTKADLINNLGTIAKYSAYLVAEKVTVITKHNDDEQYAWESSAGGSFTVRTDTGEPMGRGTKVILHLKEDQTEYLEERRIKEIVKKHSQFIGYPITLFVEKERDKEVSDDEAEEKEDKEEEKEKEEKESEDKPEIEDVGSDEEEEKKDGDKKKKKKIKEKYIDQEELNKTKPIWTRNPDDITNEEYGEFYKSLTNDWEDHLAVKHFSVEGQLEFRALLFVPRRAPFDLFENRKKKNNIKLYVRRVFIMDNCEELIPEYLNFIRGVVDSEDLPLNISREMLQQSKILKVIRKNLVKKCLELFTELAEDKENYKKFYEQFSKNIKLGIHEDSQNRKKLSELLRYYTSASGDEMVSLKDYCTRMKENQKHIYYITGETKDQVANSAFVERLRKHGLEVIYMIEPIDEYCVQQLKEFEGKTLVSVTKEGLELPEDEEEKKKQEEKKTKFENLCKIMKDILEKKVEKVVVSNRLVTSPCCIVTSTYGWTANMERIMKAQALRDNSTMGYMAAKKHLEINPDHSIIETLRQKAEADKNDKSVKDLVILLYETALLSSGFSLEDPQTHANRIYRMIKLGLGIDEDDPTADDTSAAVTEEMPPLEGDDDTSRMEEVD",
                    "description": "seq variant test with a small deletion inside, just for DEBUG purpose",
                    "annotations": [{"value":{ "AnnotationValueString": "test annotation from sequence variant b"}}],
                    "sequenceRegions":[
                        {
                            "start":2,
                            "end":2,
                            "number":[1,3],
                            "subsequence":"MPE",
                            "annotations":[
                                {
                                    "type":"User Annotation",
                                    "group":"Serie 1324",
                                    "value":{ "AnnotationValueString": "test annotation API : 3 first residues, seq variant b"}
                                }
                            ]
                        }
                    ],
                    "sequenceResidues":[
                        {
                            "code":"M",
                            "number":1,
                            "annotations":[
                                {
                                    "type":"Test 8",
                                    "group":"Serie 1324",
                                    "value": { "AnnotationValueString": "test annotation API : first residue, seq variant b"},
                                    "annotationData": [
                                                {"type": "Ki","label": "Inhibition DataBatch 1324234", "value": { "number": 0.1 ,"unit":"M"},"description":"this is a description, seq variant b"},
                                                {"type": "Ki","value": { "string": "nan"},"description":"this is a description (str entry)"},
                                                {"type": "Ki","label": "Inhibition DataBatch 1324235","value": { "string": "nan"},"description":"this is a description (str entry in a generic field), seq variant b"},
                                                {"type": "Ki","label": "Inhibition DataBatch 1324236","value": { "number": 0.1,"unit":"M" },"description":"this is a description (num entry in a generic field), seq variant b"},
                                                {"type": "Ki","label": "Inhibition DataBatch 1324237","value": { "number": 0.2,"unit":"M" },"description":"this is a description2, seq variant b", "referenceBiomoleculeSequenceId": 10834691},
                                                {"type": "IC50","label": "Inhibition DataBatch 1324238","value": { "number": 12,"unit":"%"},"description":"this is a description3, seq variant b", "referenceBiomoleculeSequence": "MPEETQTQDQPMEEEEVETFAFQAEIAQLMSLIINTFYSNKEIFLRELISNSSDALDKIRYESLTDPSKLDSGKELHINLIPNKQDRTLTIVDTGIGMTKADLINNLGTIAKSGTKAFMEALQAGADISMIGQFGVGFYSAYLVAEKVTVITKHNDDEQYAWESSAGGSFTVRTDTGEPMGRGTKVILHLKEDQTEYLEERRIKEIVKKHSQFIGYPITLFVEKERDKEVSDDEAEEKEDKEEEKEKEEKESEDKPEIEDVGSDEEEEKKDGDKKKKKKIKEKYIDQEELNKTKPIWTRNPDDITNEEYGEFYKSLTNDWEDHLAVKHFSVEGQLEFRALLFVPRRAPFDLFENRKKKNNIKLYVRRVFIMDNCEELIPEYLNFIRGVVDSEDLPLNISREMLQQSKILKVIRKNLVKKCLELFTELAEDKENYKKFYEQFSKNIKLGIHEDSQNRKKLSELLRYYTSASGDEMVSLKDYCTRMKENQKHIYYITGETKDQVANSAFVERLRKHGLEVIYMIEPIDEYCVQQLKEFEGKTLVSVTKEGLELPEDEEEKKKQEEKKTKFENLCKIMKDILEKKVEKVVVSNRLVTSPCCIVTSTYGWTANMERIMKAQALRDNSTMGYMAAKKHLEINPDHSIIETLRQKAEADKNDKSVKDLVILLYETALLSSGFSLEDPQTHANRIYRMIKLGLGIDEDDPTADDTSAAVTEEMPPLEGDDDTSRMEEVD"}
                                            ]
                                }
                            ]
                        },
                        {
                            "code":"E",
                            "number":3,
                            "annotations":[
                                {
                                    "type":"Test 8", "group":"Serie 1324", "value": { "AnnotationValueString": "test annotation API : third residue, seq variant b"}
                                },
                                {
                                    "type":"Test 8", 
                                    "group":"Serie 1324",
                                    "value": { 
                                        "AnnotationValueString": "test annotation API : third residue, annot2 on seq variant b"
                                    },
                                    "annotationData":[
                                        {
                                            "type": "Ki",
                                            "label": "Inhibition DataBatch 1324239",
                                            "value": { 
                                                "number": 0.1,
                                                "unit":"usi" 
                                            },
                                        "description":"this is a description (num entry in a generic field)"
                                        }
                                    ]
                                },
                                {
                                    "type":"User Annotation", 
                                    "group":"Serie 1324",
                                    "value": { "AnnotationValueString": "test annotation API : third residue , annot3 on seq variant b"}, 
                                    "data": []
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}




""")

    def tearDown(self):
        pass


    def test_biomolecule_annotation(self):
        """"""
        response=api.post_biomolecule_annotation(self.annotationJson)
        self.assertEqual(response.status_code,201)

    def test_biomolecile_annotation_post_2(self):
        response=api.post_biomolecule_annotation(self.annotationJson2)
        self.assertEqual(response.status_code,201)

    def test_biomolecile_annotation_post_3(self):
        response=api.post_biomolecule_annotation(self.annotationJson4)
        self.assertEqual(response.status_code,201)
        
    def test_biomolecule_annotation_failing(self):
        response=api.post_biomolecule_annotation(self.annotationJson3)
        self.assertEqual(response.status_code,404)

        
        
    