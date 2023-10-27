from neo4j import GraphDatabase

# class BioAssayGraphDatabase:
#     def __init__(self, uri, username, password):
#         self._driver = GraphDatabase.driver(uri, auth=(username, password))
    
#     def close(self):
#         self._driver.close()

#     def create_node(self, name, label, **attributes):
#         with self._driver.session() as session:
#             attributes['name'] = name
#             session.execute_write(self._create_node, label, attributes)
    
#     @staticmethod
#     def _create_node(tx, label, attributes):
#         query = f"CREATE (n:{label} $attributes)"
#         tx.run(query, attributes=attributes)

#     def create_relationship(self, name1, relationship_type, name2):
#         with self._driver.session() as session:
#             session.execute_write(self._create_relationship, name1, relationship_type, name2)
    
#     # @staticmethod
#     # def _create_relationship(tx, name1, relationship_type, name2):
#     #     query = "MATCH (a {name: $name1}), (b {name: $name2}) CREATE (a)-[r:{rel_type}]->(b)".format(rel_type=relationship_type)
#     #     tx.run(query, name1=name1, name2=name2)
#     @staticmethod
#     def _create_relationship(tx, name1, relationship_type, name2):
#         query = f"MATCH (a {{name: $name1}}), (b {{name: $name2}}) CREATE (a)-[r:{relationship_type}]->(b)"
#         tx.run(query, name1=name1, name2=name2)

class BioAssayGraphDatabase:
    def __init__(self, uri, username, password):
        self._driver = GraphDatabase.driver(uri, auth=(username, password))
    
    def close(self):
        self._driver.close()

    def create_node(self, name, label, **attributes):
        with self._driver.session() as session:
            attributes['name'] = name
            session.write_transaction(self._create_node, label, attributes)
    
    @staticmethod
    def _create_node(tx, label, attributes):
        query = f"CREATE (n:{label} $attributes)"
        tx.run(query, attributes=attributes)

    def create_relationship(self, name1, relationship_type, name2, attributes=None):
        if attributes is None:
            attributes = {}
        with self._driver.session() as session:
            session.write_transaction(self._create_relationship, name1, relationship_type, name2, attributes)

    @staticmethod
    def _create_relationship(tx, name1, relationship_type, name2, attributes):
        attributes_str = ', '.join(f"{key}: ${key}" for key in attributes.keys())
        query = f"""
        MATCH (a {{name: $name1}}), (b {{name: $name2}}) 
        CREATE (a)-[r:{relationship_type} {{{attributes_str}}}]->(b)
        RETURN r
        """
        tx.run(query, name1=name1, name2=name2, **attributes)





# # Usage Example:
# uri = "bolt://localhost:7687"  # Replace with your Neo4j URI
# username = "neo4j"  # Replace with your Neo4j username
# password = "root12345"  # Replace with your Neo4j password

# db = BioAssayGraphDatabase(uri, username, password)

# # Creating Nodes:
# db.create_node("BioAssay1", "BioAssay", attribute1="value1")
# db.create_node("Compound1", "Compound", attribute1="value1")
# db.create_node("Substance1", "Substance", attribute1="value1")
# #try catch on create relationship

# # Creating Relationships:
#db.create_relationship("Node1", "RELATED_TO", "Node2", attribute1="value1", attribute2="value2")

# # Closing the connection
# db.close()

