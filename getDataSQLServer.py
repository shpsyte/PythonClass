import pypyodbc
connection_string ='Driver={SQL Server Native Client 11.0};Server=(localdb)\\MSSQLLocalDB;Database=IscoSistemasDW;'
connection = pypyodbc.connect(connection_string)



def load_data():
    X = []
    Y = []

    SQL = ' SELECT * FROM DimCategory '

    cur = connection.cursor()
    cur.execute(SQL)
    row = cur.fetchall() 

    for i in row:
        data = [i["descricao"].strip()]
        X.append(data)
        Y.append(i["cd_familia"])

   # while row: 
        # data = [int(row["risoto"])
        #      ,  int(row["noodle"])
        #      ,  int(row["spagethi"])
        #      ,  int(row["pizza"])
        #      ,  int(row["soup"]) 
        #      ,  int(row["hamburger"]) 
        #      ,  int(row["salad"])
        #      ,  int(row["coke"])
        #      ,  int(row["wine"])
        #      ,  int(row["soda"])]
    
        # X.append(data)
        # Y.append(int(buy))


    #row = cur.next()
    cur.close()
    connection.close()    
    return X, Y    


 
 