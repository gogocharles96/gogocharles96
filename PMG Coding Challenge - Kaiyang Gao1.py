
import pandas as pd

start = input("Please input the testing code:")
files=start.split(' ')

files_to_combine = files[2:-2]     # ['./fixtures/accessories.csv', './fixtures/clothing.csv']
output_name = files[-1]           # 'combined.csv'

output =pd.DataFrame()              # to save result

for file in files_to_combine:
    try:
        df_file = pd.read_csv(file)           # read dataset
        file_name=file.split('/')[-1]         # get file name to save
        df_file['filename']=file_name         # add the third column as the filename
        output = output.append(df_file)       # combining files to output dataframe
    except:
        print("There is an error with the (file path)/file itself!")

output.to_csv(output_name)                    # export
print(output)                                 # print combined