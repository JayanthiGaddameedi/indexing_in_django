# indexing_in_django


1. We can add Index in two ways 
   1. ```
       class Product(models.Model):
       name = models.CharField(max_length=255, null=True, blank=True)
       price = models.IntegerField(null=True, blank=True)
       created = models.DateTimeField(auto_now_add=True)

       class Meta:
           indexes = [
               Index(fields=['name'])
           ]
        ```
   2. ```
         class Product(models.Model):
              name = models.CharField(max_length=255, null=True, blank=True, db_index=True)
              price = models.IntegerField(null=True, blank=True)
              created = models.DateTimeField(auto_now_add=True)
      ```
2. Indexing in postgres 
   1. First, we need to install postgres using `pip install django psycopg2-binary`
   2. then enter the below commands to log in into postgres database and create a database. 
   
| terminal                                                              | 
|:----------------------------------------------------------------------|
| $ sudo -u postgres psql                                               |
| postgres=# CREATE DATABASE test_index;                                |     
| postgres=# CREATE USER test_index WITH PASSWORD 'test_index';         |     
| postgres=# ALTER ROLE test_index SUPERUSER;                           |     
| postgres=# GRANT ALL PRIVILEGES ON DATABASE test_index TO test_index; |

3. Now, we need to change our database to postgres & add these lines in our settings.py file.
   ```
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql_psycopg2",
           "NAME": "test_index",
           "USER": "test_index",
           "PASSWORD": "test_index",
           "HOST": "localhost",
           "PORT": "5432",
       }
   }
   ```
4. To know the list of database tables `\l`
5. If you want to connect to the desired database from the terminal ` \c test_index`
6. In the database to know the list of relations, we use `\d`
7. To know the  specific details of a particular table we use `\d datarepo_product`  # datarepo is the table name
8. To create an Index in postgres we use the below command
   ` CREATE INDEX product_name_idx ON product(name);`
9. To delete the index `DROP INDEX product_name_idx;`
10. Now test our index with the below command.
   `test_index=# EXPLAIN ANALYZE SELECT * FROM datarepo_product WHERE name='67677';`

check out the [blog](https://docs.google.com/document/d/1xE7_fP6744V3ZzbtatEfBqZkZjyAwsg1J0zrWnVKOQA/edit?usp=sharing) for more details