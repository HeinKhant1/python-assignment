import json
with open ('D:\\bus-stop-data-by-id.js','r',encoding='UTF-8-sig') as bus_stop_data:
    with open ('D:\\bus-stop-ids-of-lines.js','r',encoding='UTF-8-sig') as bus_line_id:
        bus_stop=json.load(bus_line_id)
        bus_line=json.load(bus_stop_data)       
        
        for key,value in sorted(bus_line.items()):
            township=(value['township'])
            bus_stop_id=key            
            temp_tsp=township
            temp_key1=""
            count=0
            
            for key1,value1 in bus_stop.items():
                if(bus_stop_id in value1):
                    if(temp_tsp == township):
                        temp_key1 += key1+","                        
                        temp={temp_tsp:temp_key1}   
                        temp_tsp=township
            print(temp)           
            #result={}
            #for key,value in temp.items():
                #if key not in result.keys():
                    #result[key]=value
            #print(result)
            #for key in temp:
                #if temp[key] in result:
                    #result[temp[key]] +=1
                #else :
                    #result[temp[key]] =1
           # dups =[ key for key in result if result[key]>1]
            #if len(dups):
                #or dup in dups:
                   # print (dup)
           

                    


        

        
           
                            
        
                  
    
    
