from neo4j import GraphDatabase

class Neo4jConnection:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def run_query(self, query):
        with self.driver.session() as session:
            session.run(query)

    def close(self):
        self.driver.close()

if __name__ == "__main__":

    greeter = Neo4jConnection("bolt://localhost:7687", "user", "pass")
    query = '''
        MATCH (n)
        DETACH DELETE n
        '''
    greeter.run_query(query)
    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/covidtrial.csv' AS row
            MERGE (:Clinicaltrial {id:row.trial_id, name:row.trial_id, url:row.URL, study_type:row.study_type, phase:row.Phases, status:row.Status, title:row.Title, acronym:row.Acronym});
            '''
    greeter.run_query(query)
    print("covidtrial data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/location.csv' AS row
            MERGE (:Location {id:row.locationID, name:row.locationName});
            '''
    greeter.run_query(query)

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/loc_relation.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Location {id:row.locationID})
            MERGE (p1)-[:HAS_LOCATION]->(p2);
            '''
    greeter.run_query(query)
    print("location data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/sponsor.csv' AS row
            MERGE (:Sponsor {id:row.sponsorID, name:row.sponsorName});
            '''
    greeter.run_query(query)

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/sponsor_relation.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Sponsor {id:row.sponsorID})
            MERGE (p1)-[:HAS_SPONSOR]->(p2);
            '''
    greeter.run_query(query)
    print("sponsor data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/intervention.csv' AS row
            MERGE (:Intervention {id:row.interventionID, name:row.interventionName});
            '''
    greeter.run_query(query)

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/intervention_relation.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Intervention {id:row.interventionID})
            MERGE (p1)-[:HAS_INTERVENTION]->(p2);
            '''
    greeter.run_query(query)
    print("intervention data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/condition.csv' AS row
            MERGE (:Condition {id:row.conditionOMOPID, name:row.conditionOMOPName});
            '''
    greeter.run_query(query)

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/condition_relation_include.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Condition {id:row.conditionOMOPID})
            MERGE (p1)-[:INCLUDE_CONDITION]->(p2);
            '''
    greeter.run_query(query)
    print("condition inclusion data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/condition_relation_exclude.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Condition {id:row.conditionOMOPID})
            MERGE (p1)-[:EXCLUDE_CONDITION]->(p2);
            '''
    greeter.run_query(query)
    print("condition exclusion data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/procedure.csv' AS row
            MERGE (:Procedure {id:row.procedureOMOPID, name:row.procedureOMOPName});
            '''
    greeter.run_query(query)

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/procedure_relation_include.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Procedure {id:row.procedureOMOPID})
            MERGE (p1)-[:INCLUDE_PROCEDURE]->(p2);
            '''
    greeter.run_query(query)
    print("procedure inclusion data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/procedure_relation_exclude.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Procedure {id:row.procedureOMOPID})
            MERGE (p1)-[:EXCLUDE_PROCEDURE]->(p2);
            '''
    greeter.run_query(query)
    print("procedure exclusion data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/measurement.csv' AS row
            MERGE (:Measurement {id:row.measurementOMOPID, name:row.measurementOMOPName});
            '''
    greeter.run_query(query)

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/measurement_relation_include.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Measurement {id:row.measurementOMOPID})
            MERGE (p1)-[:INCLUDE_MEASUREMENT]->(p2);
            '''
    greeter.run_query(query)
    print("measurement inclusion data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/measurement_relation_exclude.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Measurement {id:row.measurementOMOPID})
            MERGE (p1)-[:EXCLUDE_MEASUREMENT]->(p2);
            '''
    greeter.run_query(query)
    print("measurement exclusion data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/observation.csv' AS row
            MERGE (:Observation {id:row.observationOMOPID, name:row.observationOMOPName});
            '''
    greeter.run_query(query)

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/observation_relation_include.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Observation {id:row.observationOMOPID})
            MERGE (p1)-[:INCLUDE_OBSERVATION]->(p2);
            '''
    greeter.run_query(query)
    print("observation inclusion data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/observation_relation_exclude.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Observation {id:row.observationOMOPID})
            MERGE (p1)-[:EXCLUDE_OBSERVATION]->(p2);
            '''
    greeter.run_query(query)
    print("observation exclusion data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/drug.csv' AS row
            MERGE (:Drug {id:row.drugOMOPID, name:row.drugOMOPName});
            '''
    greeter.run_query(query)

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/drug_relation_include.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Drug {id:row.drugOMOPID})
            MERGE (p1)-[:INCLUDE_DRUG]->(p2);
            '''
    greeter.run_query(query)
    print("drug inclusion data load done")

    query = '''
            LOAD CSV WITH HEADERS FROM 'file:///neo4j_data/drug_relation_exclude.csv' AS row
            MATCH (p1:Clinicaltrial {id:row.covidtrialID}), (p2:Drug {id:row.drugOMOPID})
            MERGE (p1)-[:EXCLUDE_DRUG]->(p2);
            '''
    greeter.run_query(query)
    print("drug exclusion data load done")