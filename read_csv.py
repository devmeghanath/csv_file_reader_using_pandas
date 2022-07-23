
# python csv file reader using pandas for big file processing


from platform import python_branch
import pandas as pd

file_path = input('enter your file path :')

read_file = pd.read_csv(file_path,encoding= 'unicode_escape') # encoding--> to fix  some string data in the dictionary that can't be encoded/decoded

even_rows = read_file.iloc[::2]
print(even_rows.to_string())




# core python



# file_path = input('enter your file path :')

# with open(file_path) as file_obj:
      

#     reader_obj = csv.reader(file_obj)

# # list comprehension method -------------------->>>>>
#     even_rows = [row for idx,row in enumerate(reader_obj) if idx%2==0]
#     print(even_rows)
      
# # Normal method------------------------->>>>


#     # for idx,row in enumerate(reader_obj):
#     #     if idx%2 ==0:
#     #         print(row)
        
    






