#connect
import nest_asyncio
nest_asyncio.apply()
#api connect
import os

os.environ["LLAMA_CLOUD_API_KEY"] = "llx-VheAT69M7ljNj142ZRpxxns2hEJrNrBn4H9YLMaW6NOoYhXP"
#load pdf for conversion
from llama_parse import LlamaParse

document = LlamaParse(result_type="markdown").load_data("/content/Mohan Vemulakonda (2).pdf")

print(document[0])
#check
print(document[0].text [:5000])
#file convert
file_name = "toolsunited.md"
with open(file_name, 'w') as file:
  file.write(document[0].text)
