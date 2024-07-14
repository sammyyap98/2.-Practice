def updateAverageBar(self):      
     
    plt = self.makeDefaultAverageBar()                   
    totalModelLen = len(self.categoryPrecDict.items()) - 1    
        
    for i, (k, _) in enumerate(self.categoryPrecDict.items()): 
        baseX = list(range(len(self.categoryDeltaList))) 
        keyIndex = self.findKeyIndex(modelVersion=k) 
          
        if keyIndex > len(self.barColorList) - 1:
            keyIndex = keyIndex % len(self.barColorList)


        X = list(np.array(baseX) + np.array([self.avgBarMarginTable[totalModelLen][i]]))
        upBar = pg.BarGraphItem(x = X, height = self.categoryRecallDict[k], 
                                width = self.avgBarWidth[totalModelLen], 
                                brush = self.barColorList[keyIndex][0], pen=self.barOutline, name=k + ' recall')
        plt.addItem(upBar)

        downBar = pg.BarGraphItem(x = X, height = [-y for y in self.categoryPrecDict[k]], 
                                width = self.avgBarWidth[totalModelLen], 
                                brush = self.barColorList[keyIndex][1], pen=self.barOutline, name=k + ' precision')
        plt.addItem(downBar)
        
    ax = plt.getAxis('bottom')
    ax.setTicks([[(index, value) for index, (_, value) in enumerate(self.categoryList)]])

    self.currentPlt = None
    for i in range(self.layout.count()):
        self.layout.itemAt(i).widget().deleteLater()

    self.currentPlt = plt
    self.layout.addWidget(plt)


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

 
 

 

 

 

 

 
 
