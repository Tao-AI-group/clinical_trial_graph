# COVID-19 Trial Graph
This repositry contains scripts and data files for manuscript 
"COVID-19 Trial Graph: A Linked Graph for COVID-19 Clinical Trials".

## Neo4j database import
Please download and install Neo4j Desktop from 
https://neo4j.com/download/ . All the data files (in csv format) for COVID-19 Trial Graph are provided
in the <em>neo4j_data folder</em>. To import the data to Neo4j database, please do the following steps:
1. Create a local database in Neo4j desktop and create your own user and password, 
which will be used to connect the database and load your data
2. Activate the database by clicking “Start” button.
3. Click three-dot button in your database and choose “manage”. 
Once the new page shows up, click “Open Folder” button, 
where you are going to put the csv data files
4. Copy <em>neo4j_data</em> folder into database’s import directory
5. Replace the user and password in <em>csv_to_neo4j.py</em> and run the script

Neo4j Python Driver is required:
```
pip install neo4j
```
## Cypher query evaluation
<em>Case query 1</em>

Retrieve all COVID-19 clinical trials that target “remdesivir”
as the intervention
```
match (c:Clinicaltrial)-[r:HAS_INTERVENTION]->(t:Intervention) 
where toLower(t.name) CONTAINS "remdesivir"
return(c)
```
<em>Case query 2</em>

Retrieve all COVID-19 clinical trials that target “remdesivir” as the intervention but
exclude pregnant women [OMOP ID: 4299535] from participating
```
match (c:Clinicaltrial)-[r:HAS_INTERVENTION]->(t:Intervention) 
where toLower(t.name) CONTAINS "remdesivir"
AND EXISTS {match (c)-[ic:EXCLUDE_CONDITION]->(condi:Condition) 
where condi.id = "4299535"}
return(c)
```
OR
```
match (c:Clinicaltrial)-[r:HAS_INTERVENTION]->(t:Intervention)
where toLower(t.name) CONTAINS "remdesivir"
AND EXISTS {match (c)-[ic:EXCLUDE_CONDITION]->(condi:Condition)
where condi.name = "Pregnant"}
return(c)
```

<em>Case query 3</em>

Retrieve all COVID-19 clinical trials that target “hydroxychloroquine” as the intervention and
allow patients with shortness of breath [OMOP ID: 312437] to participate
```
match (c:Clinicaltrial)-[r:HAS_INTERVENTION]->(t:Intervention) 
where toLower(t.name) CONTAINS "hydroxychloroquine"
AND EXISTS {match (c)-[ic:INCLUDE_CONDITION]->(condi:Condition) 
where condi.id = "312437"}
return(c)
```
OR
```
match (c:Clinicaltrial)-[r:HAS_INTERVENTION]->(t:Intervention)
where toLower(t.name) CONTAINS "hydroxychloroquine"
AND EXISTS {match (c)-[ic:INCLUDE_CONDITION]->(condi:Condition)
where condi.name = "Dyspnea"}
return(c)
```

<em>Case query 4</em>

Retrieve all COVID-19 clinical trials in the United States
that target “hydroxychloroquine” as the intervention
and allow patients with diabetes [OMOP ID: 312437] to participate
```
match (c:Clinicaltrial)-[r:HAS_INTERVENTION]->(t:Intervention) 
where toLower(t.name) CONTAINS "hydroxychloroquine"
AND EXISTS {match (c)-[rloc:HAS_LOCATION]->(loc:Location) 
where toLower(loc.name) = "united states"}  
AND EXISTS {match (c)-[ic:INCLUDE_CONDITION]->(condi:Condition) 
where condi.id = "45879799"}
return(c)
```
OR
```
match (c:Clinicaltrial)-[r:HAS_INTERVENTION]->(t:Intervention)
where toLower(t.name) CONTAINS "hydroxychloroquine"
AND EXISTS {match (c)-[rloc:HAS_LOCATION]->(loc:Location)
where toLower(loc.name) = "united states"}
AND EXISTS {match (c)-[ic:INCLUDE_CONDITION]->(condi:Condition)
where condi.name = "Diabetes"}
return(c)
```

We also provide eligibility criteria terms mapping file for the reference. Users can use this file 
<em>ec_terms_mapping.tsv</em> to look up clinical concepts and their OMOP IDs.

Please contact Jingcheng Du: Jingcheng.du@uth.tmc.edu, if you have any questions