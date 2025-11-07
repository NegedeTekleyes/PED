import sys
if len(sys.argv) > 2 and sys.argv[1] == "created_db":
    database_name = sys.argv[2]
    print(f'Creating database {database_name}')
elif sys.argv[1] == 'created_table':
    table_name = sys.argv[2]
    print(f'Creating table {table_name}')

else:
    print("Plase enter a valid database name.")