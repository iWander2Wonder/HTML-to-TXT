import os
from bs4 import BeautifulSoup


def convert_html_to_text(html_file_path, text_file_path):
   with open(html_file_path, 'r') as html_file:
       soup = BeautifulSoup(html_file, 'html.parser')


   with open(text_file_path, 'w') as text_file:
       for paragraph in soup.find_all('p'):
           text = paragraph.get_text()
           text_file.write(text + '\n')


if __name__ == '__main__':
   directory_path = 'html_files'  # Replace with your actual directory path
   text_directory_path = 'text_files'  # Replace with your desired output directory path
   os.makedirs(text_directory_path, exist_ok=True)


   for file in os.listdir(directory_path):
       html_file_path = os.path.join(directory_path, file)
       if file.endswith('.html'):
           text_filename = file.split('.')[0] + '.txt'
           text_file_path = os.path.join(text_directory_path, text_filename)
           convert_html_to_text(html_file_path, text_file_path)