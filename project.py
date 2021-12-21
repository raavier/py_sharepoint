from sharepoint import SharePoint

file_dir_path = r'C:\Users\flavi\OneDrive\Documentos\GitHub\py_sharepoint\sample.pdf'
file_name = 'sample1.pdf'
folder_name = '2020'

# upload file
SharePoint().upload_file(file_dir_path,file_name,folder_name)
