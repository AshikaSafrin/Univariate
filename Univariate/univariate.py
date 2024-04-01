class univariate():
    def QuanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            print(columnName)
            if(dataset[columnName].dtypes=='O'):
                print("Qual")
                qual.append(columnName)
            else:
                print("Quan")
                quan.append(columnName)
        return quan,qual