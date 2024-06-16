#testing     
def func():                                 
  return "test"                                                       
 
payload = {
  "model": "",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": prompt_text
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300,
  "temperature": 0.7,  
  "top_p": 0.9 
}
  

 
 

 

 

 

 

 
 
